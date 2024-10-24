import re
import requests
import json

def is_valid_username(username):
    return re.match(r"^[a-zA-Z0-9_-]{3,20}$", username) is not None

def clean_username(username_input):
    username = username_input.lower().replace("u/", "").strip()
    if not is_valid_username(username):
        raise ValueError(f"Invalid username {username}.")
    return username

def fetch_recent_posts(username_input, num_posts=50):
    username = clean_username(username_input)

    reddit_url = f"https://www.reddit.com/user/{username}/comments.json?count={num_posts}&show=given&sort=new"
    r = requests.get(reddit_url)

    if r.status_code == 200:
        json_data = json.loads(r.text)
        posts = [post["data"]["body"] for post in json_data["data"]["children"]]
        if len(posts) == 0:
            raise RuntimeError("no posts found!")
        return posts
    elif r.status_code == 429:
        raise ValueError(f"rate limited by Reddit, please try again.")
    elif r.status_code == 404:
        raise ValueError(f"no username found!")
    else:
        raise RuntimeError(f"response {r.status_code}: {r.text}")

# Test code
if __name__ == "__main__":
    username_input = input("Enter the Reddit username: ")
    posts = fetch_recent_posts(username_input, 50)

    if posts:
        print(f"Recent posts from {username_input}:")
        for i, post in enumerate(posts, start=1):
            print(f"{i}. {post}")
    else:
        print("No posts found or unable to retrieve posts.")
