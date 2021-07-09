# Investigating Emoji Redundancy (Data and Code)  
This project includes data and code used in the following papers presented during EMNLP (Wassa workshop), 2017 and LREC, 2018:  
[Investigating Redundancy in Emoji Use](https://aclanthology.org/W17-5216.pdf)  
[Classifying the Informative Behaviour of Emoji in Microblogs](https://aclanthology.org/L18-1108.pdf)

## Dataset  
**emoji_corpus.json:**  
dataset in json format of tweets ids with the respective redundancy label.
The dataset was reconstructed from the original and currently includes only ids of tweets still available at the time of the rework
(2021). The dataset should be considered subject to degradation, since the currently included tweets may become unavailable at any time.
  
## Code  
###### emo_tweepy  
**extract_tweets_from_id.py**  
The script takes emoji_corpus.json as input, extracts the actual tweet text and generates a new json file with the corpus in the following format:  
*full_tweet*: preprocessed tweet text,  
*no_emoji*: preprocessed tweet without the emojis of interest,  
*label*: the redundancy value given by the annotators for the emoji in context  

###### scripts_for_data_extraction_and_preprocessing  
Includes the code originally used to scrape data from Twitter, sample, preprocess and collect the stats about the dataset.

#### Note
The code requires python 3.9 t run.  
The scraper requires [Tweepy](https://www.tweepy.org/).



  

