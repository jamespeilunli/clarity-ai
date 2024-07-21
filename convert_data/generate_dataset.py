import os
import orjson as json
import csv

def parse_tweets(depressed_label):
    for tweet_file in os.listdir("tweet"):
        with open("tweet/" + tweet_file) as f:
            tweet_json = json.loads(f.read())
            if tweet_json["lang"] == "en":
                yield (tweet_json["text"], depressed_label)

def parse_timelines(depressed_label):
    for tweet_file in os.listdir("timeline"):
        with open("timeline/" + tweet_file) as f:
            for tweet in f.read().split("\n"):
                try:
                    tweet_json = json.loads(tweet)
                except json.JSONDecodeError:
                    continue
                try:
                    if tweet_json["lang"] == "en":
                        yield (tweet_json["text"], depressed_label)
                except (TypeError, IndexError):
                    continue

def convert(depressed_label, parse_functions=(parse_tweets,)):
    with open("out.csv", 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(("text","label"))
    
    for function in parse_functions:
        with open("out.csv", 'a') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
            for line in function(depressed_label):
                writer.writerow(line)

if __name__ == "__main__":
    convert(1, (parse_timelines,parse_tweets)) # not sure if the tweets in timelines are identical to the tweets in tweets
