import praw
import pdb
import re


alreadyreplied=[] 		#Contains the submission ID of the submissions to which the bot has already replied to

def get_jokes(subreddit1,subreddit):
	for submission in subreddit.hot(limit=10):
		if submission.id not in alreadyreplied:
			if re.search("Joke please", submission.title,re.IGNORECASE):
				for submission1 in subreddit1.hot(limit=1):
					#payload = {submission1.title,submission1.selftext.lower()}
					sub1 = submission1.title
					sub2 = submission1.selftext
					submission.reply("Maverick is here with a joke: "+ sub1 + " " + sub2)
		alreadyreplied.append(submission.id)
