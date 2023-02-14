#!/usr/bin/env python3

# Display-O-Tron 3000 specific libraries - Install instructions https://tinyurl.com/y653jp56
from dot3k import lcd
from dot3k import backlight
from dot3k import joystick as nav

# Standard Python specific libraries
from time import sleep
import math
import signal
import sys

# Library required to access Twitter API (pip install)
import tweepy

# Configuration file is in JSON format, hence we require JSON support
import json

# Set Joystick action
@nav.on(nav.BUTTON)
def handle_button(pin):
    """Joystick push action"""
    
    if status:
        screen_light(False)
    else:
        screen_light(True)

def screen_light(switch):
    """Switch Background light on, or off"""

    global status
    status=switch
  
    if status:
        backlight.rgb(50, 255, 50)
    else:
        backlight.off()

def set_graph():
    """Visual notification, illuminate Bargraph"""

    for i in range(100):
        backlight.set_graph(i / 100.0)
    for i in reversed(range(100)):
        backlight.set_graph(i / 100.0)

def twitter_auth():
    """Load configuration from JSON file and authenticate against Twitter API""" 
    
    try:
        with open('config.json') as config_file:
            data = json.load(config_file)
    except:
        print('Configuration file "config.json" not found.')
        display_init()
        sys.exit()

    api_key = data['api_key']
    api_secret = data['api_secret']
    access_token = data['access_token']
    access_token_secret = data['access_token_secret']
    screen_name = data['screen_name']

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Create API object
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
    except:
        print('Can\'t authenticate to the Twitter API, check your API credentials.')
        display_init()
        sys.exit()
    
    return api, screen_name

def twitter_stats(api, screen_name):
    """Fetch Twitter stats and display on the Display-O-Tron 3000"""
        
    # We need a baseline before entering the loop
    user = api.get_user(screen_name)
    prev_followers_count = user.followers_count

    # Fetch Twitter stats every 60 seconds. Adjust "sleep(60)" if you want a different interval
    while True:
        try:
            user = api.get_user(screen_name)
        except:
            # We don't want the program to exit when the connection goes down, so we keep on trying and inform the user.
            print('I encountered a problem fetching data from Twitter, please check your Internet connection.')

        lcd.set_cursor_position(0,0)
        lcd.write(f"User  : {user.screen_name}")
        lcd.set_cursor_position(0,1)
        lcd.write(f"Tweets: {user.statuses_count}")
        lcd.set_cursor_position(0,2)
        lcd.write(f"Subs  : {user.followers_count}")

        if user.followers_count  >  prev_followers_count:
            set_graph()
        elif user.followers_count  <  prev_followers_count:
            digits = int(math.log10(user.followers_count))+1
            lcd.set_cursor_position(digits + 8,2)
            lcd.write(" ")
            set_graph()

        prev_followers_count=user.followers_count
        sleep(60)
       
def display_init():
    """Initialize Display-O-Tron (Always a good thing to do)"""
    backlight.set_graph(0) 
    lcd.set_contrast(50)
    backlight.off()
    lcd.clear()

def sig_hand(sig, frame):
    """Ensure a clean exit with CTRL+C"""
    display_init()
    sys.exit(0)

def main():
    signal.signal(signal.SIGINT, sig_hand)
    display_init()
    screen_light(True)
    api, screen_name = twitter_auth()
    twitter_stats(api, screen_name)
   
if __name__ == "__main__":
    main()