import os
import re
import json
import time
from tweepy import OAuthHandler, API
from scripts_for_data_extraction_and_preprocessing.preprocessing import keywords
import logging
from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(filename='errors.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)

consumer_key = os.environ.get('consumer_key')
consumer_secret = os.environ.get('consumer_secret')
access_token = os.environ.get('access_token')
access_token_secret = os.environ.get('access_token_secret')

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)


def remove_emoji_from_tweet(tweet):
    for emoji in keywords:
        if emoji in tweet:
            return tweet.replace(emoji, '').replace('  ', ' ')
        else:
            continue


def preprocess(tweet):
    # matches @username
    mentions = re.compile('(@.*?)(?=\\s|:)')
    # http://stackoverflow.com/questions/6038061/regular-expression-to-find-urls-within-a-string
    links = re.compile('(http|ftp|https)://([\\w_-]+((?:\\.[\\w_-]+)+))([\\w.,@?^=%&:/~+#-]*[\\w@?^=%&/~+#-])?')
    no_mentions = re.sub(mentions, "@USER", tweet)
    no_links = re.sub(links, "@URL", no_mentions)
    no_bom = re.sub(u"\ufeff", "", no_links)
    no_newline = re.sub('\n+', ' ', no_bom)
    return no_newline


def read_corpus(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    return data


def extract_tweets_from_id(id_corpus):

    sleep_time = 2
    training = {}

    for key, value in id_corpus.items():
        try:
            tweet_fetched = api.get_status(key)
            print(f"Tweet fetched: {tweet_fetched.text}")
            full_tweet = tweet_fetched.text
            clean_tweet = preprocess(full_tweet)
            training[key] = {'full_tweet': clean_tweet,
                             'no_emoji': remove_emoji_from_tweet(clean_tweet),
                             'label': value}
            time.sleep(sleep_time)
        except Exception as e:
            logger.error(f'{value}: {e}')
            continue
    return training


corpus_file = read_corpus("emoji_corpus_ids.json")

fetched = extract_tweets_from_id(corpus_file)
print(fetched)






