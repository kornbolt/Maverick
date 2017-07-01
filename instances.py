import praw
import pdb
import re
import json
import config
import os

def replying_jokes(posts, reddit):
	if not os.path.isfile(config.FILENAME):
		alreadyreplied = []
	else:
		with open(config.FILENAME,"r") as fi:
			alreadyreplied = fi.read()
			alreadyreplied = alreadyreplied.split("\n")
			alreadyreplied = list(filter(None, alreadyreplied))

	subreddit1 = reddit.subreddit('Jokes')
	for i in posts:
		if i.id not in alreadyreplied:
			if re.search("Joke please", i.title,re.IGNORECASE):
				for submission1 in subreddit1.hot(limit=1):
					sub1 = submission1.title
					sub2 = submission1.selftext
					i.reply("Maverick is here with a joke: "+ sub1 + " " + sub2)
			alreadyreplied.append(i.id)
	with open(config.FILENAME,"w") as fo:
		for posts in alreadyreplied:
			fo.write(posts + "\n")
