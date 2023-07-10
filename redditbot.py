#!/usr/bin/python
import os
import praw
import pdb
import re

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

subreddit = reddit.subreddit("ShadowBanned")

# Check if a post_reply_history.txt file exists
# If not, make it, If yes filter out previously replied to posts
# Thanks to https://github.com/shantnu for the majority of this code
if not os.path.isfile("post_reply_history.txt"):
    posts_replied_to = []
else:
    # Read the file into a list and remove any empty values
    with open("post_reply_history.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

for submission in subreddit.new(limit=29):
    # If we haven't replied to this post before
    if submission.id not in posts_replied_to:

        # Do a case insensitive search for any_non_whitespace_char + anything_wildcard
        if re.search("\S?", submission.title, re.IGNORECASE):
            # Reply to the post
            submission.reply("This bot can read your post. Which ultimately means you're NOT shadow banned. Be aware though, If you have low karma (it varies by subreddit) it may impact you posting in other places. Again, this action was performed by a bot. If you reply to this message you may not get a response.")
            print("Bot replying to : ", submission.title)

            # Store the current id into our list
            posts_replied_to.append(submission.id)

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")