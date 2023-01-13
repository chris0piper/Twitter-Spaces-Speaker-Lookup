
import re
import logging
from typing import Dict, List
import logging
import re
from time import sleep
import json
import threading
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.remote.file_detector import LocalFileDetector
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException

import threading

# path to firefox.exe
FIREFOX_BINARY_LOCATION = r'/Applications/Firefox.app/Contents/MacOS/firefox-bin'

class Twitter_Spaces:
    """
    A class for monitoring a if a user hosts or speaks in a twitter space
    """
    # def __init__(self, binary):
    #     FIREFOX_BINARY_LOCATION = r'/Applications/Firefox.app/Contents/MacOS/firefox-bin'

    def domain_to_url(self, domain: str) -> str:
        if domain.startswith("."):
            domain = "www" + domain
        return "http://" + domain

    def login_using_cookie_file(self, driver: WebDriver, cookie_file: str):
        """Restore auth cookies from a file. Does not guarantee that the user is logged in afterwards.
        Visits the domains specified in the cookies to set them, the previous page is not restored."""
        domain_cookies: Dict[str, List[object]] = {}
        with open(cookie_file) as file:
            cookies: List = json.load(file)
            # Sort cookies by domain, because we need to visit to domain to add cookies
            for cookie in cookies:
                try:
                    domain_cookies[cookie["domain"]].append(cookie)
                except KeyError:
                    domain_cookies[cookie["domain"]] = [cookie]

        for domain, cookies in domain_cookies.items():
            driver.get(self.domain_to_url(domain + "/robots.txt"))
            for cookie in cookies:
                cookie.pop("sameSite", None)  # Attribute should be available in Selenium >4
                cookie.pop("storeId", None)  # Firefox container attribute
                try:
                    driver.add_cookie(cookie)
                except:
                    print(f"Couldn't set cookie {cookie['name']} for {domain}")


    def monitor_user_for_spaces(self, twitter_handle, spaces_callback):
        """
        Monitors a Twitter user's profile for new Spaces activity (hosting or speaking in a space).
        
        Parameters:
            - twitter_handle (str): The Twitter handle of the user to monitor.
            - callback (function): A function to be called when a new Space is detected. The function should accept a single argument, the ID of the Space.
        """

        # This inner function is a wrapper for the provided callback function,
        # allowing it to be run in a separate thread.
        def thread_wrapper(spaces_id):
            spaces_callback(spaces_id)

        # Setup firefox driver
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("intl.accept_languages", "en-us")
        firefox_profile.update_preferences()
        options = Options()
        options.binary_location = FIREFOX_BINARY_LOCATION
        options.headless = True
        driver = webdriver.Firefox(firefox_profile, options=options)
        driver.set_window_size(1920, 1080)

        # Use login.json to inject cookies, loging you into twitter
        self.login_using_cookie_file(driver, cookie_file='login.json')

        # Go to the twitter profile
        driver.get("https://twitter.com/{}".format(twitter_handle))

        # Keep track of which Spaces have already been seen,
        # to avoid calling the callback function multiple times for the same Space.
        seen_spaces = set()

        while(True):
            # To see if the user is a speaker for or hosting a space, search the page for this url format
            # https://twitter.com/i/spaces/1mrGmkbmMRVxy/peek
            # If it exists, pass the inner id to callback. If not, sleep and refresh
            try:
                element = driver.find_element("xpath", "//*[contains(@*, '/i/spaces/') and contains(@*, '/peek')]")
                if element:
                    # Extract the Space's ID from the element's URL.
                    url = element.get_attribute('href')
                    result = re.search(r'\/(\w+)\/peek', url)
                    if result:
                        extracted_string = result.group(1)
                        # If this Space has not been seen before, call the callback function in a separate thread.
                        if(extracted_string not in seen_spaces):
                            t = threading.Thread(target=thread_wrapper(extracted_string))
                            t.start()
                            seen_spaces.add(extracted_string)
            except NoSuchElementException:
                pass
            # If the element was not found, that means the user is not speaking in or hosting a Space at the moment.
            # Sleep for 15 seconds and then refresh the page again.
            sleep(15)
            



