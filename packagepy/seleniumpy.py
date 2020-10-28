#!python3
# -*- coding: utf-8 -*-
# automationpy/packagepy/seleniumpy
# 15 Oktober 2020 edit commen dan merapikan kode

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def cek_browser(choice, browser, url):
    # pengecekan browser yang digunakan
    if choice == 1:
        # open browser without handless
        if browser == 1:
            options = webdriver.ChromeOptions()
            options.add_argument("headless")
            driver = webdriver.Chrome(
                executable_path=r"/chromedriver.exe", options=options)
            driver.implicitly_wait(10)
            driver.get(url)
            title_page = "{}".format(driver.title)
            name_browser = "Open Browser Chrome Handless"
            return driver, title_page, name_browser
        else:
            options = webdriver.FirefoxOptions()
            options.add_argument("-headless")
            driver = webdriver.Firefox(
                executable_path=r"/geckodriver.exe", options=options)
            driver.implicitly_wait(10)
            driver.get(url)
            title_page = "{}".format(driver.title)
            name_browser = "Open Browser Firefox Handless"
            return driver, title_page, name_browser
    else:
        # open browser with handless
        if browser == 1:
            driver = webdriver.Chrome(executable_path=r"/chromedriver.exe")
            driver.implicitly_wait(10)
            driver.get(url)
            title_page = "{}".format(driver.title)
            name_browser = "Open Browser Chrome"
            return driver, title_page, name_browser
        else:
            driver = webdriver.Firefox(executable_path=r"/geckodriver.exe")
            driver.implicitly_wait(10)
            driver.get(url)
            title_page = "{}".format(driver.title)
            name_browser = "Open Browser Firefox"
            return driver, title_page, name_browser


def main():
    # testing
    pass


if __name__ == "__main__":
    pass
