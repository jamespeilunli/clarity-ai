import time
import requests
import msgspec
import pandas as pd
from fake_useragent import UserAgent

i = 0

times = []

ski = []

def scrape_user(username, count=50, sort="new"):
        global i, times
        reddit_url = f"https://www.reddit.com/user/{username}/comments.json?count={count}&show=given&sort={sort}"
        print(f"INFO: {i} SCRAPING USER {username}")
        i += 1

        r = requests.get(reddit_url)


        if r.status_code == 200:
            json = msgspec.json.decode(r.text)

            try:
                for post in json["data"]["children"]:
                    try:
                        yield [
                            post["data"]["author"],
                            post["data"]["body"],
                            post["data"]["link_title"],
                            post["data"]["is_submitter"],
                            post["data"]["subreddit"],
                            post["data"]["score"],
                            post["data"]["created_utc"]
                        ]
                    except Exception as e:
                        print("ERROR: ", e)
            except Exception as e:
                print("ERROR: ", e)
        else:
            print(f"ERROR: response {r.status_code}: {r.text}")



def getUserPosts(username):
    User = list(scrape_user(username))
    userPosts = []
    for post in User:
        userPosts.append(post[1])
    return userPosts

print(getUserPosts("PresidentObama"))