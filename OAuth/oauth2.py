#!/usr/bin/python
import os
import praw

print("The next line outputs the current working directory. Be sure your praw.ini is configured and in the right place/n")
print(os.getcwd())

#This should pull your setting from the [bot1] section of your praw.ini
#NOTE: Currently cannot get praw.ini to work
#reddit = praw.Reddit("bot1")

reddit = praw.Reddit(
    username="",
    password="",
    client_id="",
    client_secret="",
#    refresh_token="",
    redirect_uri="http://localhost:8080",
    user_agent="",
)

#This is where you put the 'code' string from oauth1.py instert it in between the double quotes.
print("/nThe next line, if run properly, will output your refresh_token which needs to be included in your praw.ini in order to permenantly access reddit/n")
print(reddit.auth.authorize(""))

#Always checking that the settings in praw.ini are not the reason something isn't working
print("/nThe next lines should be your praw.ini configured username and user agent string/n")
print(reddit.user.me())
print(reddit.config.user_agent)