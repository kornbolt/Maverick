import config
import praw

def get_token():
	client_auth = requests.auth.HTTPBasicAuth(config.CLIENT_ID, config.CLIENT_SECRET)
	post_data = {"grant_type": "password", "username": "qwert", "password": "wert"}
	headers = {"User-Agent": "ChangeMeClient/0.1 by YourUsername"}
	response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
	r=response.json()
	return(r)

def get_instances():
	reddit = praw.Reddit(client_id=config.CLIENT_ID,
                     client_secret=config.CLIENT_SECRET,
                     refresh_token=config.ACCESS_TOKEN,
                     user_agent='testscript by /u/asdfg')
	return(reddit.auth.scopes())
