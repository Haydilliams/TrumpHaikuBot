import tweepy as tp
import time
import os
import re
from haiku import haiku_finder

# credentials to login to twitter api
consumer_key = 'Jes3l4Bg6AunsjMNDuucv8vTv'
consumer_secret = 	'hzZhHG3NxmN5arHmJyKRHL4yXkxflHi2KIrHCsaHPfGlEtRH8P'
access_token = 	'959459566407864321-cLMRfe29OSpyYIopAKsq8tkNyY7C5jH'
access_secret = 'G1l4TLWUTtGnltAL0AljQRaInlnYQvdMNL49Kue88k9Mt'

# authorization details
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tp.API(auth)

# Trump twitter details
trump_id = 'realDonaldTrump'

# raw tweets
trumps_tweets_raw = api.user_timeline(screen_name = trump_id, count = 25, 
		include_rts = False, tweet_mode="extended")

# list of tweets in their full length
trumps_tweets_long = [tweet.full_text for tweet in trumps_tweets_raw]

# new list to be populated after filtering out urls
trumps_tweets = [] 

#tweets with text of any mentions removed
for tweet in trumps_tweets_long:
	trumps_tweets.append(re.sub('\s\W\S+|\s\d\S+|\shttps\S+', '', tweet))
	
haikus = []

for tweet in trumps_tweets:
	#haiku_finder(tweet,haikus)
	print(tweet)
	print ("----------------------------------------------------------")
