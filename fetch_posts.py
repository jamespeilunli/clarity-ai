import re
import os
from dotenv import load_dotenv
from mastodon import Mastodon

load_dotenv()
MASTODON_EMAIL = os.getenv('MASTODON_EMAIL')
MASTODON_PASSWORD = os.getenv('MASTODON_PASSWORD')

# Run this once
Mastodon.create_app(
    'pytooterapp', # should probably change these names sometime...
    api_base_url='https://mastodon.social',
    to_file='pytooter_clientcred.secret'
)

# Uncomment the code below to log in and save the user credentials (run this once)
mastodon = Mastodon(client_id='pytooter_clientcred.secret')
mastodon.log_in(
    MASTODON_EMAIL,
    MASTODON_PASSWORD,
    to_file='pytooter_usercred.secret'
)

# Function to format username
def format_username(username):
    if not username.startswith('@'):
        username = '@' + username
    if not username.endswith('@mastodon.social'):
        username = username + '@mastodon.social'
    return username

def clean_post(text):
    # Extract href links from <a> tags, except preserve hastags and mentions
    href_pattern = re.compile(r'<a\s+[^>]*?href="([^"]*?)"[^>]*?>(.*?)</a>', re.IGNORECASE)
    def replace_with_href(match):
        href = match.group(1)
        inner_text = match.group(2)
        if inner_text.startswith('#') or inner_text.startswith('@'):
            return inner_text
        return href
    text_with_hrefs = href_pattern.sub(replace_with_href, text)
    
    text_with_newlines = re.sub(r'</p>\s*<p>', '\n', text_with_hrefs) # Preserve <p> tags as newlines
    clean_text = re.sub(r'<[^>]+>', ' ', text_with_newlines) # Replace all other HTML tags with spaces
    clean_text = clean_text.strip() # Remove leading and trailing whitespace
    clean_text = clean_text.replace("&#39;", "'").replace("&quot;", '"') # Replace weird formatting

    return clean_text

# Function to fetch recent posts
def fetch_recent_posts(username, num_posts=20):
    mastodon = Mastodon(access_token='pytooter_usercred.secret')

    # Extract user handle
    user_handle = username.strip('@').split('@')[0]

    # Search for the user account
    accounts = mastodon.account_search(user_handle)
    if not accounts:
        print(f"Error: User {username} not found.")
        return []

    user_id = accounts[0]['id']

    # Fetch recent posts
    posts = mastodon.account_statuses(user_id, limit=num_posts)
    recent_posts = [clean_post(post['content']) for post in posts if post['content'] != ""]

    return recent_posts

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
