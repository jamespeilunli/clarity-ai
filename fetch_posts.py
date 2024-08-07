import re
import os
from dotenv import load_dotenv
from mastodon import Mastodon

load_dotenv()
MASTODON_EMAIL = os.environ.get('MASTODON_EMAIL')
MASTODON_PASSWORD = os.environ.get('MASTODON_PASSWORD')
client_id = os.environ.get('MASTODON_CLIENT_ID')
client_secret = os.environ.get('MASTODON_CLIENT_SECRET')
print(type(MASTODON_EMAIL), type(MASTODON_PASSWORD), type(client_id), type(client_secret))

if not client_id or not client_secret:
    client_id, client_secret = Mastodon.create_app(
        'pytooterapp', # should probably change these names sometime...
        api_base_url='https://mastodon.social',
        to_file=None
    )
    print("Server owner: please set the environment variables MASTODON_CLIENT_ID and MASTODON_CLIENT_SECRET!")
    print("To access them, go to the source code and print out `client_id` and `client_secret` right where these print statements are")
    quit()

# Log in
mastodon = Mastodon(
    client_id=client_id,
    client_secret=client_secret,
    api_base_url='https://mastodon.social'
)
access_token = mastodon.log_in(
    MASTODON_EMAIL,
    MASTODON_PASSWORD,
)

# Function to format username
def format_username(username):
    username = username.strip()
    if not username.startswith('@'):
        username = '@' + username
    if not username.endswith('@mastodon.social'):
        username = username + '@mastodon.social'
    return username

def is_valid_username(username):
    # Check if the username matches a valid pattern
    # Assume valid usernames contain only letters, numbers, underscores, or periods
    return re.match(r'^[a-zA-Z0-9_.]+$', username) is not None

def clean_post(text):
    # Extract href links from <a> tags, except preserve hastags and mentions
    href_pattern = re.compile(r'<a\s+[^>]*?href="([^"]*?)"[^>]*?>(.*?)</a>', re.IGNORECASE)
    def replace_with_href(match):
        href = match.group(1)
        inner_text = match.group(2)
        if inner_text.startswith('#') or inner_text.startswith('@'):
            return inner_text
        return href
    clean_text = href_pattern.sub(replace_with_href, text)
    
    clean_text = re.sub(r'</p>\s*<p>', '\n', clean_text) # Preserve <p> tags as newlines
    clean_text = re.sub(r'</span>\s*<span>', ' ', clean_text) # Preserve <span> tags as spaces
    clean_text = re.sub(r'<[^>]+>', '', clean_text) # Remove all other HTML tags
    clean_text = clean_text.strip() # Remove leading and trailing whitespace
    clean_text = clean_text.replace("&#39;", "'").replace("&quot;", '"') # Replace weird formatting

    return clean_text

# Function to fetch recent posts
def fetch_recent_posts(username, num_posts=60):
    username = format_username(username)

    mastodon = Mastodon(access_token=access_token, api_base_url="https://mastodon.social")

    # Extract user handle
    user_handle = username.strip('@').split('@')[0]

    if not is_valid_username(user_handle):
        raise ValueError(f"Invalid username format.")

    # Search for the user account
    accounts = mastodon.account_search(user_handle)
    print(user_handle, accounts)
    if not accounts:
        raise ValueError(f"User {username} not found.")

    user_id = accounts[0]['id']

    posts = []
    max_id = None
    while len(posts) < num_posts:
        fetched_posts = mastodon.account_statuses(user_id, limit=40, max_id=max_id) # Mastodon API gives you maximum of 40 posts per page
        if not fetched_posts:
            break

        posts.extend([post for post in fetched_posts if post['content'] != ""]) # Filter posts with non-empty content

        max_id = fetched_posts[-1]['id'] - 1 # Update max_id for pagination

    # Apply clean_post and return the exact number of posts needed
    cleaned_posts = [clean_post(post['content']) for post in posts[:num_posts]]

    return cleaned_posts

if __name__ == "__main__":
    username = input("Enter the Mastodon username: ")
    formatted_username = format_username(username)
    posts = fetch_recent_posts(formatted_username, 20)

    if posts:
        print(f"Recent posts from {formatted_username}:")
        for i, post in enumerate(posts, start=1):
            print(f"{i}. {post}")
    else:
        print("No posts found or unable to retrieve posts.")
