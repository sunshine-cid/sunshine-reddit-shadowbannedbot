#!/usr/bin/python
import os
import praw

print("The next line outputs the current working directory. Be sure your praw.ini is configured and in the right place/n")
print(os.getcwd())

#This should pull your setting from the [bot1] section of your praw.ini
reddit = praw.Reddit("bot1")

print("/nThe next line is a url you'll need to copy and visit in a browser which is logged in as the username you configured in praw.ini/n")
#For the string on the next line under 'scope' I have included some default access privelages. 
#You may replace them all with a * in order to include everything. 
#Only do this is you think your scope is the reaon you're getting 403 errors.
print(reddit.auth.url(scopes=["identity", "submit", "read", "privatemessages", "save", "mysubreddits", "history"], state="...", duration="permanent"))
print("/nafter visiting the url and approving the bots access you'll be redirected to a url. In the url address string there is a variable 'code'."
print("Copy the string between the = and # for use in oauth2.py")

#Always checking that the settings in praw.ini are not the reason something isn't working
print("/nThe next lines should be your praw.ini configured username and user agent string/n")
print(reddit.user.me())
print(reddit.config.user_agent)