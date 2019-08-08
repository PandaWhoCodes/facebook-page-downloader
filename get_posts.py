from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from yaspin import yaspin, Spinner  # terminal spinner
import getpass
import time
import re
import pandas as pd
from fb_post_parser import parse_posts


def get_web_driver(path):
    return webdriver.Chrome(path)


def goto_(link, browser):
    browser.get(link)


def login_to_fb(browser):
    if "https://m.facebook.com" not in browser.current_url:
        goto_("https://m.facebook.com", browser)
        time.sleep(1)
    email = browser.find_element_by_id("m_login_email")
    password = browser.find_element_by_id("m_login_password") or browser.find_element_by_name("pass")
    email.send_keys(login)
    password.send_keys(passw, Keys.RETURN)
    time.sleep(2)


if __name__ == '__main__':
    number_of_posts = 500
    sp = Spinner(["😸", "😹", "😺", "😻", "😼", "😽", "😾", "😿", "🙀"], 200)
    login = "emailaddress@gmail.com"
    passw = "password"
    browser = get_web_driver("C:/xampp/chromedriver.exe")
    goto_("https://m.facebook.com/", browser)
    login_to_fb(browser)
    browser.get("https://m.facebook.com/login/save-device/cancel/?flow=interstitial_nux&amp;nux_source=regular_login")
    # print("Click on 'Not now'.")
    # key = input("Page unique identifier: ")

    key = "kcg.college"
    time.sleep(1)
    goto_(f'https://m.facebook.com/{key}/posts/', browser)
    parsed_posts = []
    with yaspin(sp, text="Gathering posts."):
        try:
            for _ in range(number_of_posts):
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(.5)

                posts = browser.find_elements_by_class_name("_3drp")
                for post in posts:
                    try:
                        parsed = parse_posts(post.get_attribute("innerHTML"))
                        if parsed:
                            parsed_posts.append(parsed)
                    except Exception as e:
                        print(e, "\n", post.get_attribute("innerHTML"))
                browser.execute_script(
                    "let posts = document.querySelectorAll('._3drp'); for (i of posts){ console.log(i); i.remove()}")
        finally:
            pd.DataFrame(parsed_posts).to_csv(key + ".csv")
