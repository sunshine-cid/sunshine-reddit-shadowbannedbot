#!/usr/bin/python
import os
import praw
import pdb
import re

reddit = praw.Reddit("bot1")

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

for submission in subreddit.new(limit=10):
    # If we haven't replied to this post before
    if submission.id not in posts_replied_to:

        # Do a case insensitive search
        if re.search("*", submission.title, re.IGNORECASE):
            # Reply to the post
            submission.reply("We can read your post. If you have low karma it may impact you posting in other places. This action was performed by a bot.")
            print("Bot replying to : ", submission.title)

            # Store the current id into our list
            posts_replied_to.append(submission.id)

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")