#!python3
# -*- coding: utf-8 -*-
# automationpy/main
# created 21 Oktober 2020

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import response
from datetime import datetime


url = "https://web.whatsapp.com/"

driver = webdriver.Chrome(executable_path=r"/chromedriver.exe")
driver.set_window_size(1000, 720)
driver.implicitly_wait(10)
driver.get(url)
title_page = "{}".format(driver.title)
print(title_page)
name_browser = "Open Browser Chrome"
print(name_browser)

wait = WebDriverWait(driver, 20)

# text_search = "salim_im3"
# text_search = "Viola"
text_search = "irfans_dua"
# profiling = ["halo mas, mintol dibalas ya ini hehehe", "udah makan belum mas", "selamat ulang tahun mas e", "chat terkahir dibalas ya mas hehehe"]
profiling = ["pesan pertama", "pesan kedua", "pesan ketiga", "chat terkahir dibalas ya mas hehehe"]

# value element content list chat whatsapp
class_name = "z_tTQ"
content = "_2hqOq"
message_content = "_3Whw5"

stoper = True
while stoper:
    try:
        # side = driver.find_element_by_xpath('//div[@id="side"]')
        side = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//div[@id="side"]')))
        datab = side.find_element_by_css_selector(
            'div._3FRCZ.copyable-text.selectable-text')
        datab.send_keys(text_search)
        time.sleep(2)
        datab.send_keys(Keys.RETURN)
        print("ID Side Findind")
        stoper = False
    except:
        print("wait @id='side' 1 seconds")
        time.sleep(1)

stoper1 = True
while stoper:
    try:
        # main = driver.find_element_by_xpath('//div[@id="main"]')
        main_wait = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//div[@id="main"]')))
        table = main_wait.find_element_by_css_selector(
            'div._3FRCZ.copyable-text.selectable-text')
        print("ID Main Findind")
        stoper1 = False
    except:
        print("wait @id='menu' 1 seconds")
        time.sleep(1)

try:
    # main = driver.find_element_by_xpath('//div[@id="main"]')
    main = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//div[@id="main"]')))
    table = main.find_element_by_css_selector(
        'div._3FRCZ.copyable-text.selectable-text')
except:
    pass

# for profil in range(20):
#     print("\n")
#     print("====mulai====")

#     today = str(datetime.now())
#     no = 1 + profil
#     # msg_wa = f"similitiki-{no:03}-{today}"
#     msg_wa = f"similitiki-{no:03}-{today}"
#     time.sleep(1)
for profil in profiling:
    print("\n")
    print("====mulai====")

    today = str(datetime.now())
    time.sleep(1)

    try:
        table.send_keys(profil)
    except:
        pass

    stoper2 = True
    while stoper2:
        try:
            send = main.find_element_by_xpath('//span[@data-testid="send"]')
            send.click()
            print("Tombol klik sudah muncul")
            stoper2 = False
        except:
            print("wait @data-testid='send' 1 seconds")
            time.sleep(1)

    msgs = profil

    response.waiting(driver, class_name, content, msgs, message_content)
    time.sleep(1)

    reply = response.get_reply_chat(
        driver, class_name, content, msgs, message_content)
    time.sleep(1)

    print(reply)
    get_reply = "\n".join(reply)
    print("Balasan Chat hanya satu:\n---\n",
          get_reply.strip(), "\n---")
    print("====selesai====")
