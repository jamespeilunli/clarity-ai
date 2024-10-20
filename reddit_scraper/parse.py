import re
from bs4 import BeautifulSoup

REPEATED_SPACES = re.compile(r"\s{2,}")

with open("reddit_user_page.html", "r") as f:
    page_source= f.read()

soup = BeautifulSoup(page_source, "html.parser")


for e1 in soup.find_all("div", {"id": "-post-rtjson-content"}):
    visible_text = re.sub(REPEATED_SPACES, " ", e1.getText()).strip()
    print(visible_text)
    print()
