<!-- tag line -->
<h3 align='center'> Stay up to date with Twitter Spaces </h3>

<!-- primary badges -------------------------------------->
<p align="center">
  <!-- version -->
  <img src='https://img.shields.io/pypi/v/Twitter-Spaces-Speaker-Lookup' />
  <!-- size -->
  <img src='https://img.shields.io/github/repo-size/chris0piper/Twitter-Spaces-Speaker-Lookup' />
  <!-- forks  -->
  <img src='https://img.shields.io/github/forks/chris0piper/Twitter-Spaces-Speaker-Lookup?style=social' />
  <!-- stars -->
  <img src='https://img.shields.io/github/stars/chris0piper?style=social' />
  <!-- languages -->
  <img src='https://img.shields.io/github/languages/top/chris0piper/Twitter-Spaces-Speaker-Lookup' />
</p>
<br/>

## Explination

This tool uses Selenium Firefox webdriver to grab the spaces ID's which a specified user is speaking at or hosting. There are currently no unauthenticated api endpoints (both public or private) which allow you to view when a user is speaking in a space. For this reason, this library requires a twitter login to run.

It runs selenium in headless mode and scrapes from a users profile page.

The original motivation for this tool is to monitor users and make trades based on what they say in twitter spaces, but saw others online asking how to get these space ids so decided to share! Hope you enjoy.

<br/>

## Explination

This tool uses Selenium Firefox webdriver to grab the spaces ID's which a specified user is speaking at or hosting. There are currently no unauthenticated api endpoints (both public or private) which allow you to view when a user is speaking in a space. For this reason, this library requires a twitter login to run.

It runs selenium in headless mode and scrapes from a users profile page.

The original motivation for this tool is to monitor users and make trades based on what they say in twitter spaces, but saw others online asking how to get these space ids so decided to share! Hope you enjoy.

<br/>

## Installation

To install, you must have firefox downloaded on your computer. (Any error involving geckodriver means firefox is not in your path)

```bash
pip install Twitter-Spaces-Speaker-Lookup
```

Create a blank file called "login.json"

Open up firefox and log into twitter and navigate into your profile page.

Download a cookie grabbing extension (I use EditThisCookie2 for firefox) and copy all cookies.

Paste these cookies into login.json and you're good to go!
<br/>



### Example:

```py
import importlib  
speaker_lookup = importlib.import_module("Twitter-Spaces-Speaker-Lookup.speaker_lookup")
ts = speaker_lookup.Twitter_Spaces()

# Create a callback function which takes in a twitter_spaces_id to be run for each space the target user joins or 
def example_callback(spaces_id):
    print(f"New Space: '{spaces_id}'!")

monitor_user = 'elon2doge'
ts.monitor_user_for_spaces(monitor_user, example_callback)

// Whenever the monitored user speaks at or hosts a twitter space, your callback function will be called.
```

## 💙 Contributing

PR's are welcome !

Found a Bug ? Create an Issue.

<br/>


## 💖 Like this project ?

Leave a ⭐ If you think this project is cool.

<br/>




## 👨‍💻 Author

### Chris Piper

[Twitter](https://twitter.com/elon2doge "Chris Piper")

<br/>




## 🍁 Licence

**ISC**