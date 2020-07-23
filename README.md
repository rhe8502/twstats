# Twitter Stats

Twitter Stats is a small Python 3 program using Tweepy and the official Twitter API.

The program displays user name, current tweet count and followers (Subs) on the Display-O-Tron 3000. The bar light gives a visual notification if a new follower is gained.

![Twitter Stats](../res/twitter_stats.gif)

## Quickstart guide

Setup the Display-o-Tron by following the instructions on the Pimoroni site located [here](https://learn.pimoroni.com/tutorial/display-o-tron/getting-started-with-display-o-tron "Getting started with Display-o-Tron 3000").

For the impatient: 

    curl https://get.pimoroni.com/displayotron | bash

Install tweepy via pip:
    
    pip install tweepy


Configuration and account settings are stored in JSON format. Create the file **config.json** (see sample below) and place it in the same folder as **twitter_stats.py**. 

**config.json**
```json
{
    "api_key" : "API KEY" ,
    "api_secret" : "API SECRET",
    "access_token" : "ACCESS TOKEN",
    "access_token_secret" : "ACCESS TOKEN SECRET",
    "screen_name" : "TWITTER HANDLE"
}
```
Before using the Twitter API, sign-in to your Twitter Developer account, create a new application and generate API credentials for it.

Only **"Read-only"** access permission is required for this Python script.

**References:**
* [Twitter Developer Website](https://developer.twitter.com/)
* [Tweepy Documentation](http://docs.tweepy.org/en/latest/)
* [Pimoroni Display-o-Tron 3000 Reference](https://learn.pimoroni.com/tutorial/display-o-tron/getting-started-with-display-o-tron)
* [Display-o-Tron 3000 product reference on the PiHut](https://thepihut.com/products/pimoroni-display-o-tron-3000)
