#!/usr/bin/python
import os
import praw

print("The next line outputs the current working directory. Be sure your praw.ini is configured and in the right place")
print(os.getcwd())

#This should pull your setting from the [bot1] section of your praw.ini
#NOTE: Currently cannot get praw.ini to work
#reddit = praw.Reddit("bot1")

#Now it should include your refresh token which should let us post from the bot.
reddit = praw.Reddit(
    username="",
    client_id="",
    client_secret="",
    refresh_token="",
    redirect_uri="http://localhost:8080",
    user_agent="",
)

#The next line submits a 'test' post to the 'test' subreddit. 
#Visit https://www.reddit.com/r/test/ to check to see if your post made it.
#If it did, congratulations, you're all configured for using reddit with your bot!

reddit.subreddit("test").submit("Test Submission", url="https://reddit.com")

#Always checking that the settings in praw.ini are not the reason something isn't working
print("The next lines should be your praw.ini configured username and user agent string. Though they may error if you're not authenticated.")
print(reddit.user.me())
print(reddit.config.user_agent)