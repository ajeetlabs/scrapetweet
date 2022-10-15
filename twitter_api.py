import configparser
import tweepy
from csv import DictWriter


config = configparser.ConfigParser(interpolation=None)
config.read('config.ini')
api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']
bearer_token = config['twitter']['bearer_token']

client = tweepy.Client(bearer_token,api_key,api_key_secret,access_token,access_token_secret)
#datas = client.get_users_tweets(18839785,tweet_fields=['created_at','context_annotations','geo','entities','author_id','public_metrics'])
columns = ['created_at','author_id', 'tweet', 'context_annotations', 'geo', 'entities', 'public_metrics']

for response in tweepy.Paginator(client.get_users_tweets, 18839785, tweet_fields=['created_at','context_annotations','geo','entities','author_id','public_metrics']):
    for tweet in response.data:
        dict = {'created_at': tweet.created_at,
        'author_id': tweet.author_id,
        'tweet': tweet.text,
        'context_annotations': tweet.context_annotations,
        'geo': tweet.geo,
        'entities': tweet.entities,
        'public_metrics': tweet.public_metrics
        }
        with open('export.csv', 'a') as f_obj:
            dict_obj = DictWriter(f_obj, fieldnames=columns)
            dict_obj.writerow(dict)

