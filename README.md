# sunshine-reddit-shadowbannedbot
A basic Reddit bot to notify users that their posts are visible in /r/ShadowBanned

# Prerequisites
You'll need pip and PRAW installed for this script to work. In console type:

> sudo apt install python3-pip

> pip install praw

# OAuth Procedure
OAuth with PRAW is paramount to its function. Documentation is lacking in this respect, so I'll do my best to take you through the 3-step OAuth process simply. This process and these files can be used with ANY PRAW-using bot to authenticate it and get a permanent refresh token.


/OAuth/oauth1.py
------------------------------------------------

You should have your authentication values entered in praw.ini under the subheading [bot1]. However, when I configured this bot there must have been a bug related to praw.ini which prevented it from working. 
So, I have just included the variables in the code.

>    username="",
>
>    password="",
> 
>    client_id="",
> 
>    client_secret="",
> 
>    redirect_uri="http://localhost:8080",
> 
>    user_agent="",

username should be the account name you'll be using for API access. password is the password for that user account. client_id and client_secert are strings requested by that user account at the URL: https://www.reddit.com/prefs/apps 
There you'll agree that you're a developer and then you'll 'create a new app' This will give you your client_id and client_secert. user_agent is a unique string created by you and meant to be discriptinve about the function of your bot and it's version. Do not include words like "scraping" or "bot". Something like "python.post.responding.v0.1" would work, provided no one esle has used that before. Leave the redirect_url as it is, unless you know what you're doing and want to change it.

One important thing to mention here is 'scope.' Scope is the level of access you're bot is requesting to do whatever it is doing on reddit. I have included by default the level of access I thought best for my bot. These include "identity", "submit", "read", "privatemessages", "save", "mysubreddits", "history". You may need to add scopes to get your bot to do what you want. A list of posible options can be found at: https://praw.readthedocs.io/en/stable/tutorials/refresh_token.html#reddit-oauth2-scopes If you ever need to change your scopes you'll need to run the authentication process through all over again. If you want to just include all scopes you can replace all the individual strings with a single "*" though this is not really recommended.

Once you've gotten the client_ variables, inputted the values, and run the script the script will output two things. First is the Current Working Directory, which was included as a check for praw.ini. We're not using that so it's unimportant. Second is an authorization URL which should be pretty clear since it begins with https:// and ends with ... Copy the URL and be sure to include the ... Paste it in a browser and you should be directed to a page where you authorize access for your app. After visiting the url and approving the bots access you'll be redirected to a url. In the url address string there is a variable 'code'. Copy the 'code' string between the = and # for use in oauth2.py

<b>Errors</b>

You will recieve errors when running this script the first time regardless beasue your user is not authenticated with reddit's API, so don't sweat it. After you authorize the script correctly you can run it again and you should get no errors becasue you're now an authorized user. If the URL you visit just sends you to an error you've likely copied one of your authorization variables wrong (check that they're named correctly too), but it may also be you didn't copy the URL correctly. These are the two major potential mistakes with this step.


/OAuth/oauth2.py
------------------------------------------------

Copy your variables section from oauth1.py and (re)place it in oauth2.py. Take the 'code' you recieved in step 1 an copy it in between the brackets in the line print(reddit.auth.authorize("")) Run the script. This script will output a permenant refresh_token whcih will replace the password variable and allow you to post, comment, or whatever, more permanently.

<b>Errors</b>

The most likely error here will be that you didn't copy the 'code' in its entirety

/OAuth/oauth3.py
------------------------------------------------

Copy your variables section from oauth2.py and (re)place it in oauth3.py. You'll want to delete the 'password' line and uncomment the 'refresh_token' line. Place the refresh token you got as output in the prevoius step and put it in the refresh_token="" Run the script and check https://reddit.com/r/test You should see your post there if there were not errors. If it is posted, congrats! You're app is authenticated!

<b>Errors</b>

The most likely error(s) you recieve here will be HTTP 40X errors related to scope. Perhaps you messed up the scope list in step 1? Perhaps you need to try using a scope of "*"?

# Shadow Banned Bot

