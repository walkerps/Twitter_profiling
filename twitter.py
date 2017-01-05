import tweepy
import json

consumer_key = "W2LFgW7iEJPdVr6nLZig8v9q4"

consumer_secret = "80XJb0JhLOpENx0DFA4tOLV6jdkIqW77DOyMKCaA9gIMFZETVn"

access_token = "401259377-KViYWHWhltzIiPwUlEfutUzJLsdxguZokygs3KBi"

access_token_secret = "TetB2nbJb0DVWIGx9MCCZ6G7da1AHtDCRwfLfsxdt3s5d" 

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)

auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

for tweet in public_tweets :
	print tweet.text
	print "\n"
user = api.get_user('Whitewalker_ps')

prafful_tweets = api.user_timeline('MehrotraPrafful')
prafful_user = api.get_user('MehrotraPrafful')
gaurav_tweets = api.user_timeline('scarredpegasus')
gaurav_user = api.get_user('scarredpegasus')
harsh_tweets = api.user_timeline('damnhd_')
harsh_user = api.get_user('damnhd_')
asai_tweets = api.user_timeline('asaiatin')
asai_user = api.get_user('asaiatin')

print user.screen_name
print user.followers_count
#for friends in user.friends():
#	print friends.screen_name

print "\n"

for tweet in prafful_tweets:
	print tweet.text

print "\n"

print prafful_user.screen_name
print prafful_user.name 
print prafful_user.followers_count
#print prafful_user.favourites_count
print prafful_user.time_zone
print prafful_user.description
print prafful_user.profile_image_url_https
print prafful_user.friends_count

for friends in prafful_user.friends():
	print friends.screen_name
print "\n"

followers_walker = api.followers('Whitewalker_ps')

followers_prafful = api.followers('MehrotraPrafful')
followers_harsh = api.followers('damnhd_')
followers_gaurav = api.followers('scarredpegasus')
followers_asai = api.followers('asaiatin')

print '\n'

for followers in followers_walker:
	print followers.name

class MyStreamListener(tweepy.StreamListener):
	def __init__(self,api=None):
		super(MyStreamListener,self).__init__()
		self.num_tweets = 0
		self.file = open('tweets.txt','w')

	def on_status(self,status):
		tweet =  status.text
		self.file.write(tweet)
		self.num_tweets += 1
		if self.num_tweets<300:
			return true
		else:
			return false
		self.close()
	def on_error(self,status):
		print (status+'Error')

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth,listener = MyStreamListener())

myStream.filter(track=['python'])
