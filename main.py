import config
import praw
import time
from instances import replying_jokes

reddit = praw.Reddit('prbot')
#reddit = praw.Reddit(client_id=config.CLIENT_ID,
	     #client_secret=config.CLIENT_SECRET,
	     #refresh_token=config.ACCESS_TOKEN,
	     #user_agent='testscript by /u/asdfg')

functions = [replying_jokes]
while True:
	subreddit = reddit.subreddit('iliekcomputers')
	posts = []
	for submission in subreddit.hot(limit=10):
		posts.append(submission)
	for f in functions:
		f(posts)
	time.sleep(5)