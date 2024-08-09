import re
import os
from dotenv import load_dotenv
from mastodon import Mastodon

load_dotenv()
MASTODON_EMAIL = os.environ.get("MASTODON_EMAIL")
MASTODON_PASSWORD = os.environ.get("MASTODON_PASSWORD")
client_id = os.environ.get("MASTODON_CLIENT_ID")
client_secret = os.environ.get("MASTODON_CLIENT_SECRET")

if not client_id or not client_secret:
    client_id, client_secret = Mastodon.create_app(
        "pytooterapp",  # should probably change these names sometime...
        api_base_url="https://mastodon.social",
        to_file=None,
    )
    print("Server owner: please set the environment variables MASTODON_CLIENT_ID and MASTODON_CLIENT_SECRET!")
    print("To access them, go to the source code and print out `client_id` and `client_secret` right where these print statements are")
    quit()

# Retrieve access token
mastodon = Mastodon(
    client_id=client_id,
    client_secret=client_secret,
    api_base_url="https://mastodon.social",
)
access_token = mastodon.log_in(
    MASTODON_EMAIL,
    MASTODON_PASSWORD,
)

def is_valid_username(username):
    return re.match(r"^[a-zA-Z0-9_. ]+$", username) is not None
def is_valid_instance(instance):
    return re.match(r"^[\w-]+(?:\.[\w-]+)+\/?$", instance) is not None

def extract_user_info(username_input):
    """
    Extracts username as well as Mastodon instance from a username input.

    Valid inputs:
    "username" (instance defaults to mastodon.social)
    "@username" (instance defaults to mastodon.social)
    "@username@instance.social"
    "username@instance.social"
    """

    username_input = username_input.strip()
    if not username_input.startswith("@"):
        username_input = "@" + username_input
    parts = username_input.split("@")
    if len(parts) == 2:
        return parts[1], "mastodon.social"
    elif len(parts) == 3:
        return parts[1], parts[2]
    else:
        raise ValueError("Invalid username format.")

def clean_post(text):
    # Extract href links from <a> tags, except preserve hastags and mentions
    href_pattern = re.compile(r'<a\s+[^>]*?href="([^"]*?)"[^>]*?>(.*?)</a>', re.IGNORECASE)
    def replace_with_href(match):
        href = match.group(1)
        inner_text = match.group(2)
        if inner_text.startswith("#") or inner_text.startswith("@"):
            return inner_text
        return href

    clean_text = href_pattern.sub(replace_with_href, text)
    clean_text = re.sub(r'</p>\s*<p>', '\n', clean_text) # Preserve <p> tags as newlines
    clean_text = re.sub(r'</span>\s*<span>', ' ', clean_text) # Preserve <span> tags as spaces
    clean_text = re.sub(r'<[^>]+>', '', clean_text) # Remove all other HTML tags
    clean_text = clean_text.strip() # Remove leading and trailing whitespace
    clean_text = clean_text.replace("&#39;", "'").replace("&quot;", '"') # Replace weird formatting

    return clean_text

def get_user_id(username_input):
    username, instance = extract_user_info(username_input)
    if not is_valid_username(username):
        raise ValueError(f"Invalid characters in username {username}.")
    if not is_valid_instance(instance):
        raise ValueError(f"Invalid characters in instance {instance}.")

    mastodon = Mastodon(
        access_token=access_token, api_base_url=f"https://mastodon.social"
    )

    print(username, instance)
    accounts = mastodon.account_search(username)
    print(accounts)
    for account in accounts:
        if account.acct == username or account.acct == f"{username}@{instance}":
            return account["id"]
    raise ValueError(f"User {username} not found.")

def fetch_recent_posts(username_input, num_posts=60):
    user_id = get_user_id(username_input)

    posts = []
    max_id = None
    while len(posts) < num_posts:
        fetched_posts = mastodon.account_statuses(
            user_id, limit=40, max_id=max_id
        )  # Mastodon API gives you maximum of 40 posts per page
        if not fetched_posts:
            break

        posts.extend(
            [post for post in fetched_posts if post["content"] != ""]
        )  # Filter posts with non-empty content

        max_id = fetched_posts[-1]["id"] - 1  # Update max_id for pagination

    cleaned_posts = [clean_post(post["content"]) for post in posts[:num_posts]]

    return cleaned_posts

# Test code
if __name__ == "__main__":
    username_input = input("Enter the Mastodon username: ")
    posts = fetch_recent_posts(username_input, 60)

    if posts:
        print(f"Recent posts from {username_input}:")
        for i, post in enumerate(posts, start=1):
            print(f"{i}. {post}")
    else:
        print("No posts found or unable to retrieve posts.")
