import praw
import pdb
import re
import json
import config
import os,sys
import random,time
from praw.models import MoreComments

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
		for post in alreadyreplied:
			fo.write(post + "\n")

def news(posts, reddit):
	if not os.path.isfile(config.FILENAME):
		alreadyreplied = []
	else:
		with open(config.FILENAME,"r") as fi:
			alreadyreplied = fi.read()
			alreadyreplied = alreadyreplied.split("\n")
			alreadyreplied = list(filter(None, alreadyreplied))
	subreddit2 = reddit.subreddit('indianews')
	for i in posts:
		if i.id not in alreadyreplied:
			if re.search("news headlines", i.title,re.IGNORECASE):
				for submission2 in subreddit2.new(limit=5):
					sub1 = submission2.title
					i.reply("Maverick with a news current update: "+ sub1 + "\n")-
				alreadyreplied.append(i.id)
	with open(config.FILENAME,"w") as fo:
		for post in alreadyreplied:
			fo.write(post + "\n")


def tictactoe(posts,reddit):
	if not os.path.isfile(config.FILENAME):
		alreadyreplied = []
	else:
		with open(config.FILENAME,"r") as fi:
			alreadyreplied = fi.read()
			alreadyreplied = alreadyreplied.split("\n")
			alreadyreplied = list(filter(None, alreadyreplied))

	for i in posts:
		if i.id not in alreadyreplied:
			if re.search("game1", i.title,re.IGNORECASE):
				alreadycommented=[]
				choosen = []
				board = {
			             1:' ', 2:' ', 3:' ',
			             4:' ', 5:' ', 6:' ',
			             7:' ', 8:' ', 9:' '
			            }  

				def winningchances(ch) :
				    winwin = [(1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7)]
				    for x in winwin :
				        if (board[x[0]] == ch and board[x[1]] == ch and board[x[2]] == ch) :
				            return True
				    return False

				def choose():
					place = random.randint(1,9)
					if place in choosen:
					        choose()
					else:
					    return place

				def play():
				    i.reply("Let's play the game of TicTacToe\n"+"The board positions are as follows : \n"+
				    		"___|___|___\n" + " 1 | 2 | 3 \n"
				            "___|___|___\n" +"___|___|___\n"
				            " 4 | 5 | 6 \n" +"___|___|___\n"
				            "___|___|___\n"+" 7 | 8 | 9 \n" +
				            "___|___|___\n"+
				            "You have to select any one position (from 1 to 9) for your move. \n"+
				    		"You got the first chance\n")
				    chance = 1    
				    moves = 0
				    while moves < 9 :
				        if(chance==1):
				            i.reply("The present board: \n" + "   |   |   \n"+
				    				" "+board[1]+" | "+board[2]+" | "+board[3]+" \n"+
				    				"___|___|___\n"+
				    				"   |   |   \n"+
				    				" "+board[4]+" | "+board[5]+" | "+board[6]+" \n"+
				    				"___|___|___\n"+
				    				"   |   |   \n"+" "+board[7]+" | "+board[8]+" | "+board[9]+" \n" + 
				    				"   |   |   \n"+
				    				"Enter the position to move : \n")
				            time.sleep(10)
				            for comment in i.comments:
				            	if comment.id not in alreadycommented:
				            		for second_level_comment in comment.replies:
				            			r=second_level_comment.body
				            			place = int(r)
				            		alreadycommented.append(comment.id)

				        else:
				            place = choose()

				        if (place <1 or place > 9) :
				            if chance==1:
				                i.reply("Invalid move! Move again")
				            moves-=1
				        elif (place in choosen) :
				            if chance==1:
				                i.reply("You have already choosen that move. Move again")
				            moves-=1
				        else :
				            choosen.append (place)
				            chx = ' '
				            if chance == 1 :
				                board[place] = 'O'
				                chance = 2
				                chx = 'O'
				            else :
				                board[place] = 'X'
				                chance = 1
				                chx = 'X'
				            if winningchances(chx) :
				                if chance == 1 :
				                	i.reply("The present board: \n" + "   |   |   \n"+
				    				" "+board[1]+" | "+board[2]+" | "+board[3]+" \n"+
				    				"___|___|___\n"+
				    				"   |   |   \n"+
				    				" "+board[4]+" | "+board[5]+" | "+board[6]+" \n"+
				    				"___|___|___\n"+
				    				"   |   |   \n"+" "+board[7]+" | "+board[8]+" | "+board[9]+" \n" + 
				    				"   |   |   \n"+
				    				"Enter the position to move : \n"+"You LOSE :(")
				                    #print ("You LOSE :(")
				                else :
				                	i.reply("The present board: \n" + "   |   |   \n"+
				    				" "+board[1]+" | "+board[2]+" | "+board[3]+" \n"+
				    				"___|___|___\n"+
				    				"   |   |   \n"+
				    				" "+board[4]+" | "+board[5]+" | "+board[6]+" \n"+
				    				"___|___|___\n"+
				    				"   |   |   \n"+" "+board[7]+" | "+board[8]+" | "+board[9]+" \n" + 
				    				"   |   |   \n"+
				    				"Enter the position to move : \n"+"Congratulations, You WON!!")
				                    #print ("Congratulations, You WON!!")
				                #print ("The present board: ")
				                #draw_board()    
				                sys.exit()
				        moves += 1
				    i.reply("The present board: \n" + "   |   |   \n"+
				    				" "+board[1]+" | "+board[2]+" | "+board[3]+" \n"+
				    				"___|___|___\n"+
				    				"   |   |   \n"+
				    				" "+board[4]+" | "+board[5]+" | "+board[6]+" \n"+
				    				"___|___|___\n"+
				    				"   |   |   \n"+" "+board[7]+" | "+board[8]+" | "+board[9]+" \n" + 
				    				"   |   |   \n"+
				    				"Enter the position to move : \n"+"Oh, It's a draw!!")

				play()
				alreadyreplied.append(i.id)
	with open(config.FILENAME,"w") as fo:
		for post in alreadyreplied:
			fo.write(post + "\n")


				