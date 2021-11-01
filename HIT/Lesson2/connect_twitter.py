from twython import Twython
from credentials import *

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET)
tag = '#100DaysofCode'
result = twitter.search(q=tag, tweet_mode="extended")
print(result)
