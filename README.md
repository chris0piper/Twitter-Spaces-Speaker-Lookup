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

## Installation

To install, you must have firefox downloaded on your computer

```bash
pip install Twitter-Spaces-Speaker-Lookup
```

Create a blank file called "login.json"

Open up firefox and log into twitter and navigate into your profile page.

Download a cooking grabbing extension (I use EditThisCookie2 for firefox) and copy all cookies.

Paste these cookies into login.json and you're good to go!
<br/>



### Example:

```py
ts = Twitter_Spaces()

// Create a callback function which takes in a twitter_spaces_id to be run for each space the target user joins or 
def example_callback(spaces_id):
    print(f"New Space: '{spaces_id}'!")

monitor_user = 'elonmusk'
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