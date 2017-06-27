import config
import praw
import instances as i

#reddit = praw.Reddit('prbot')
reddit = praw.Reddit(client_id=config.CLIENT_ID,
	     client_secret=config.CLIENT_SECRET,
	     refresh_token=config.ACCESS_TOKEN,
	     user_agent='testscript by /u/asdfg')

subreddit1 = reddit.subreddit('Jokes')
subreddit = reddit.subreddit('iliekcomputers')

i.get_jokes(subreddit1,subreddit)