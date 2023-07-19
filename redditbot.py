#!/usr/bin/python
import os
import praw
import re
import time

#This should pull your setting from the [bot1] section of your praw.ini
#NOTE: Currently cannot get praw.ini to work
#reddit = praw.Reddit("bot1")

#Now it should include your refresh token which should let us post from the bot.
#If you've no idea what's going on here refer to the OAuth subdirectory, 
#and the oauth*.py steps for PRAW and Reddit authentication.
reddit = praw.Reddit(
    username="",
    client_id="",
    client_secret="",
    refresh_token="",
    redirect_uri="http://localhost:8080",
    user_agent="",
)

#This is the message which will be submitted by the bot as a reply
bot_message = ("Beep, boop. This bot can read your post."
               "Which ultimately means you're NOT shadow banned. Be aware "
               "though, If you have low karma it may impact you posting "
               "in other places. What is considered *low* varies by subreddit."
               " Again, this action was performed by a bot. "
               "If you reply to this message you may not get a response.")

#This is the time to sleep, in seconds, between while-loop cycles
sleep_time = 300 #300 is 5 minutes

subreddit = reddit.subreddit("ShadowBanned")

while True:
    print("ShadowBanBot running - press [CTRL]-C to Exit")

    # Thanks to https://github.com/shantnu for the majority of this code
    # Check if a post_reply_history.txt file exists
    # If not, make it, If yes filter out previously replied to posts
    if not os.path.isfile("post_reply_history.txt"):
        post_reply_history = []
    else:
        # Read the file into a list and remove any empty values
        with open("post_reply_history.txt", "r") as f:
            post_reply_history = f.read()
            post_reply_history = post_reply_history.split("\n")
            post_reply_history = list(filter(None, post_reply_history))

    for submission in subreddit.new(limit=29):
        # If we haven't replied to this post before
        if submission.id not in post_reply_history:

            # Do a case insensitive search for any_char + anything_repeated
            if re.search(".?", submission.title, re.IGNORECASE):
                # Reply to the post
                submission.reply(bot_message)
                print("Bot replying to : ", submission.title)

                # Store the current id into our list
                post_reply_history.append(submission.id)

    # Write our updated list back to the file
    with open("post_reply_history.txt", "w") as f:
        for post_id in post_reply_history:
            f.write(post_id + "\n")

    #Wait between loops
    time.sleep(sleep_time)