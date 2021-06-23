import numpy as np
from preprocessing import *
import codecs

def main():

    with codecs.open('datafile.json', 'r', encoding='utf32') as f:
        myfile = f.readlines()
    unique = list(set(myfile))
    print('\n')
    print(f"The length of the original file is: {len(myfile)} tweets", '\n')
    print(f"The length of the file with no duplicates is: {len(unique)} tweets", '\n')
    lengths = np.array([len(i) for i in clean_tweets(unique)])
    mu = np.mean(lengths)
    std = np.std(lengths)
    print(f"The mean length in the collection of cleaned tweets is: %d characters {mu}", '\n')
    print(f"The standard deviation is: {std}", '\n')
    print("The amount of cleaned tweets with more than 140 characters is: %d" % len([i for i in clean_tweets(unique) if len(i) > 140]), '\n')
    print("The amount of cleaned tweets with less than 10 characters is: %d" % len([i for i in clean_tweets(unique) if len(i)<10]), '\n')
    print("Maximum tweet length found is: %d characters" % max([len(i) for i in clean_tweets(unique)]), '\n')
    print("Minimum tweet length found is: %d characters" % min([len(i) for i in clean_tweets(unique)]), '\n')
    print("Removing tweets above 140 characters and below 10 characters...", '\n')
    cleaned = [tweet for tweet in clean_tweets(unique) if 140 >= len(tweet) >= 10]
    print("Creating list of keeywords' lists...", '\n')
    key_lists = create_classes_lists(cleaned, keywords)
    print("Creating a triple including a list of pairs (keyword name : num. of instances)...", '\n')
    d, minpair, maxpair = get_name_with_length(key_lists)
    print(f"The least represented keyword is {minpair[0]} with {minpair[1]} instances", '\n')
    print(f"The best represented keyword is: {maxpair[0]} with {maxpair[1]} instances")


if __name__ == '__main__':
    main()

