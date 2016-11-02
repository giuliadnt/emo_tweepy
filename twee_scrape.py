#!/usr/bin/python
# -*- coding: <utf8> -*-

__author__ = 'GiuliaDnt'


import time
from httplib import IncompleteRead
from tweepy import Stream, OAuthHandler
from tweepy.streaming import StreamListener
import sys
import demjson
import codecs

# API Keys
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# List of emoji of interest (Unicode from http://unicode.org/emoji/charts/full-emoji-list.html)
keywords = [u'\U0001F3F0', u'\U0001F3EB', u'\U0001F3E1', u'\U00002615', u'\U0001F355',
            u'\U0001F369', u'\U0001F3C0', u'\U0001F3C6', u'\U0001F3CA', u'\U0001F3A4 ',
            u'\U0001F3B8', u'\U0001F3B6', u'\U0001F3A8', u'\U0001F4FA', u'\U0001F4DA',
            u'\U0001F436', u'\U0001F341 ', u'\U00002744', u'\U0001F393', u'\U0001F389',
            u'\U0001F383', u'\U0001F46B', u'\U0001F64B', u'\U0001F6B6', u'\U0001F622',
            u'\U0001F612', u'\U0001F60D', u'\U00002708 ', u'\U0001F697', u'\U000026F5' ]


class Listener(StreamListener):

    counter = 0
    # Desired amount
    limit = 500000

    def on_data(self, data):
        # Do nothing if no data was received
        if data is None:
            time.sleep(5)
            return

        # Turn Unicode strings to dictionaries
        store_data = demjson.decode(data, encoding="utf32")

        if self.counter < self.limit:

            try:
                out_file = codecs.open("datafile.json","a", encoding="utf32")
                print store_data['text'], '\n', self.counter
                # Write only the text of the tweet to file
                out_file.write(store_data['text'] + '\n')
                out_file.close()
            #possibly replace with KeyError
            except Exception as e:
                print e.message


        elif self.counter>=self.limit:
            print "Done! Finally! I am really exhausted..."
            return False

        self.counter += 1


    def on_error(self, status_):

        print >> sys.stderr, 'Encountered error with status code:', status_
        return True



# OAuth object
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# Initialize Stream object
twitter_stream = Stream(auth, Listener())


# Call the stream listener
# Handle Protocol Error
try:
    twitter_stream.filter(track=keywords, languages=['en'], async=True)
except IncompleteRead:
    print "Connection broken"
