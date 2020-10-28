#!python3
# -*- coding: utf-8 -*-
# automationpy/main
# salim suprayogi
# created 21 Oktober 2020

import time
import packagepy
import whatsapp
import datetime
import json
import os


def log_testing(mulai, choice, browser, profiling, url, filename_csv, file_html, tester, name_contact, selesai):
    # function for history testing
    choice = int(choice)
    browser = int(browser)
    # checking the browser used
    if choice == 1:
        # open browser without handless
        if browser == 1:
            choice = "ifif/{}/open browser at terminal chrome".format(choice)
            browser = "else/{}/open browser at terminal chrome".format(browser)
        else:
            choice = "ifelse/{}/open browser at terminal firefox".format(
                choice)
            browser = "ifelse/{}/open browser at terminal firefox".format(
                browser)
    else:
        # open browser with handless
        if browser == 1:
            choice = "elseif{}/open browser chrome UI/UX".format(choice)
            browser = "elseif{}/open browser chrome UI/UX".format(browser)
        else:
            choice = "elseelse{}/open browser firefox UI/UX".format(choice)
            browser = "elseelse{}/open browser firefox UI/UX".format(browser)

    data_log = {
        "nama_tester": tester,
        "mulai_test": mulai,
        "choice": choice,
        "browser": browser,
        "profiling": profiling,
        "url": url,
        "nama_file_csv": filename_csv,
        "nama_file_html": file_html,
        "name_contact": name_contact,
        "selesai_testing": selesai
    }
    waktus = str(datetime.datetime.now())
    waktu_list = waktus[11:]
    replace_pertama = waktu_list.replace(".", "_")
    hasil_replace = replace_pertama
    replace_kedua = hasil_replace.replace(":", "_")
    log_testing = "log_testing_{}.json".format(replace_kedua)\
    # log
    print("{##########log_testings############################}", log_testing)
    folder_automationpy = os.getcwd()
    print("{folder_automationpy}", folder_automationpy)
    os.chdir("../../automationpy_wa")
    curent_dir = os.getcwd()
    path_location = os.path.join(curent_dir, log_testing)
    print("{path_location}", path_location)

    json_object = json.dumps(data_log, indent=4)
    with open(path_location, mode="w") as file_jason:
        file_jason.write(json_object)


def main(filename_csv, file_html, ids, topik, category, label, answer, text1, choice, browser, url, profiling, tester, name_contact):
    driver, title_page, browser_name = packagepy.cek_browser(
        choice, browser, url)
    driver.set_window_size(1000, 720)
    data_all, data_webchat, title_page, browser_name = whatsapp.message_csv(
        filename_csv, ids, topik, category, label,
        answer, text1, driver, title_page, browser_name,
        profiling, tester, name_contact, choice, browser,
        url
    )
    # call function htmlpy()
    packagepy.htmlpy(
        data_all, data_webchat, title_page, browser_name, file_html, tester
    )


if __name__ == "__main__":
    # run program main function main()
    print("_MULAI_")
    # | time
    mulai = str(datetime.datetime.now())
    # | contact name
    name_contact = "salim_im3"
    # | tester name
    tester = "Salim Suprayogi"

    # | input cloumn name header from file data_csv
    ids = "no"
    topik = "topic"
    category = "categori"
    label = "label"
    answer = "answer"
    text1 = "question 1"

    # | choice pilih 1 = open browser handless chrome, choise pilih 0/else = open browser handless firefox
    # | browser pilih 1 = open chrome, browser pilih 0/else = open firefox
    choice = 0
    browser = 1

    # | target website address
    url = "https://web.whatsapp.com/"

    # | read file name csv
    filename_csv = "test_automation_data.csv"

    # | title name file report format html
    file_html = "result_data_html_all".strip().lower()

    # | if there is an intro
    profiling = ["halo"]

    # call function main()
    main(
        filename_csv, file_html, ids, topik, category,
        label, answer, text1, choice, browser,
        url, profiling, tester, name_contact
    )

    print("_SELESAI_")
    selesai = str(datetime.datetime.now())
    print("***", mulai)
    print("***", selesai)

    # call function log_testing()
    log_testing(
        mulai, choice, browser, profiling, url,
        filename_csv, file_html, tester, name_contact, selesai
    )
