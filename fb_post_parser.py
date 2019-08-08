from bs4 import BeautifulSoup
import re


def parse_posts(post):
    soup = BeautifulSoup(post, "lxml")
    post_date_time = str(soup.find("abbr"))
    post_date_time = re.findall(r'<abbr>(.*)<\/abbr>', post_date_time)[0]
    post_str = str(soup.find("div", {"class": "_5rgt"}))
    post_str = BeautifulSoup(post_str, "lxml").text
    rnk_soup = BeautifulSoup(str(soup.find("div", {"class": "_rnk"})), "lxml")
    likes_str = BeautifulSoup(str(rnk_soup.find("div", {"class": "_1g06"})), "lxml").text
    likes_n = [int(s) for s in likes_str.split() if s.isdigit()]
    if len(likes_n) > 0:
        likes_n = likes_n[0]
    else:
        likes_n = 0
    shares_str = BeautifulSoup(str(rnk_soup.find("div", {"class": "_1fnt"})), "lxml").text
    shares_n = [int(s) for s in shares_str.split() if s.isdigit()]
    if len(shares_n) > 0:
        shares_n = shares_n[0]
    else:
        shares_n = 0
    if post_str:
        return {"datetime": post_date_time, "post": post_str, "likes": likes_n, "shares": shares_n}
    else:
        return ""
