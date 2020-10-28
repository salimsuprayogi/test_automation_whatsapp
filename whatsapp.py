#!python3
# -*- coding: utf-8 -*-
# automationpy/webchat
# salim suprayogi
# created 21 Oktober 2020

import time
import os
import packagepy
import json
import dominate
from dominate.tags import *
import os
import io
import datetime
import difflib
import response

# value element search text contact name
ele_side = '//div[@id="side"]'
side_text = 'div._3FRCZ.copyable-text.selectable-text'

# value textarea for writing message
ele_main = '//div[@id="main"]'
main_text = 'div._3FRCZ.copyable-text.selectable-text'
# value button click send message
ele_send = '//span[@data-testid="send"]'

# value element content list chat whatsapp
class_name = "z_tTQ"
content = "_2hqOq"
message_content = "_3Whw5"


def open_browser(choice, browser, url):
    pass


def to_days():
    # | function day %A,date %d,month %B,year %Y
    today_dates = datetime.datetime.now()
    today_date = today_dates.strftime("%A, %d %B %Y")
    print(today_date)
    return today_date


def contact_name(wait, ele_side, side_text, name_contact):
    # function search contact name
    stoper = True
    while stoper:
        try:
            # side = driver.find_element_by_xpath('//div[@id="side"]')
            side = wait.until(packagepy.EC.presence_of_element_located(
                (packagepy.By.XPATH, ele_side)))
            datab = side.find_element_by_css_selector(side_text)
            datab.send_keys(name_contact)
            time.sleep(2)
            datab.send_keys(packagepy.Keys.RETURN)
            print("ID Side Was Found")
            stoper = False
        except:
            print("wait @id='side' 1 seconds")
            time.sleep(1)


def text_area(wait, ele_main, main_text):
    # function check search textarea message
    stoper1 = True
    while stoper1:
        try:
            # main = driver.find_element_by_xpath('//div[@id="main"]')
            main_wait = wait.until(packagepy.EC.presence_of_element_located(
                (packagepy.By.XPATH, ele_main)))
            table = main_wait.find_element_by_css_selector(main_text)
            print("ID Main Was Found")
            stoper1 = False
        except:
            print("wait @id='menu' 1 seconds")
            time.sleep(1)


def textareas(wait, ele_main, main_text):
    # function was found textarea
    try:
        # main = driver.find_element_by_xpath('//div[@id="main"]')
        main = wait.until(packagepy.EC.presence_of_element_located(
            (packagepy.By.XPATH, ele_main)))
        table = main.find_element_by_css_selector(main_text)
        return main, table
    except:
        pass


def click_send(span_main):
    # fucntion clikc button send message
    stoper2 = True
    while stoper2:
        try:
            send = span_main.find_element_by_xpath(ele_send)
            send.click()
            print("The click button is displayed")
            stoper2 = False
        except:
            print("wait @data-testid='send' 1 seconds")
            time.sleep(1)


def menu_profil(profiling, wait, text_field, span_main, driver, class_name, content, message_content):
    print("====profiling====")
    for profil in profiling:
        try:
            text_field.send_keys(profil)
            click_send(span_main)
        except:
            pass
        msgs = profil
        response.waiting(driver, class_name, content,
                         msgs, message_content)
    to_days()
    print("====profiling====")


def message_csv(filename_csv, ids, topik, category, label, answer, text1, driver, title_page, browser_name, profiling, tester, name_contact, choice, browser, url):
    # save all test results at data_all folder 
    data_all = {}
    # save all successful and failed test results
    data_status = {}
    # log
    data_id = []
    data_topik = []
    data_category = []
    data_label = []

    wait = packagepy.WebDriverWait(driver, 20)

    contact_name(wait, ele_side, side_text, name_contact)

    text_area(wait, ele_main, main_text)

    span_main, text_field = textareas(wait, ele_main, main_text)

    no_id, no_topik, no_category, no_label, no_answer, no_text1, data_csv = packagepy.data_header(
        filename_csv, ids, topik, category, label, answer, text1
    )

    # | read all file csv
    for line in range(len(data_csv)):
        # | read row from file csv [ 1-n ]
        read_rowcsv = data_csv["row{}".format(line)]
        # | read len from total data every line in file csv
        len_rowcsv = len(read_rowcsv)
        # | if line equal nol, then call function menu_profil()
        if line == 0:
            # | continue for the next line from csf, from number 1 untul number N
            menu_profil(
                profiling, wait, text_field, span_main,
                driver, class_name, content, message_content
            )
            continue

        # | read key dict from csv file, which has been converted to a data type dictionary with key row1-rowN
        row = "row{}".format(line)
        # | read key dict from csv file, which has been converted to a data type dictionary with key label1-labelN
        label = "label{}".format(line)
        # get text no id from csv
        getcsv_id = data_csv[row][no_id]
        # | log
        data_id.append(getcsv_id)
        # get text name topik from csv
        getcsv_topik = data_csv[row][no_topik]
        # | log
        data_topik.append(data_topik)
        # get text name categori from csv
        getcsv_category = data_csv[row][no_category]
        # | log
        data_category.append(getcsv_category)
        # get text label from csv
        getcsv_label = data_csv[row][no_label]
        # | log
        data_label.append(getcsv_label)
        # get text name answer result from csv
        getcsv_answer = data_csv[row][no_answer]

        # | temporary storage of failed or successful test results
        data_status[row] = {}  # data_status ={"row1":}

        # get all question from csv with indeks
        getcsv_question = data_csv[row][no_text1:len_rowcsv]

        # | Loop to read all messages that will be sent from the CSV file to the chat
        for no_text, texts in enumerate(getcsv_question):
            # | The message text from the CSV file is converted to lowercase and remove unnecessary front and back spaces
            text = texts.lower().strip()
            if text == "":
                # | jif the csv text file is empty, it will continue the message text data from the next csv
                # | log
                print("Question Kosong {}".format(no_text+1))
                continue
            # | Change text from csv to utf-8 encode
            bytes_encoded_text = text.encode(encoding='utf-8')
            str_decoded_msg_text = bytes_encoded_text.decode()

            print("\n@Send Question {} label...${}$".format(
                no_text+1, str_decoded_msg_text))

            try:
                text_field.send_keys(str_decoded_msg_text)
                click_send(span_main)
            except:
                pass

            msgs = str_decoded_msg_text

            response.waiting(driver, class_name, content,
                             msgs, message_content)
            time.sleep(1)

            reply = response.get_reply_chat(
                driver, class_name, content, msgs, message_content)

            print("@please wait, get chat reply...")
            get_reply = "\n".join(reply)

            # | take the first list to compare the results with csv data
            result_reply_chat = reply[0]

            bytes_encoded_reply = result_reply_chat.encode(encoding='utf-8')
            str_decoded_reply = bytes_encoded_reply.decode()

            get_csv = getcsv_answer.strip().lower()
            bytes_encoded_csv = get_csv.encode(encoding='utf-8')
            str_decoded_csv = bytes_encoded_csv.decode()

            # | check if the result of the chat reply is the same as the answer in the csv file
            percentage = difflib.SequenceMatcher(
                None, str_decoded_reply, str_decoded_csv).ratio()
            probability = round(percentage, 2)
            if percentage >= 0.92:
                # log
                print("percentage:", probability)
                status = "pass"
                print("@reply chat : {}".format(get_reply))
                print("@answer : {}".format(str_decoded_csv))
                print("@status test: {}".format(status))
                # | temporary storage of failed or successful test results
                data_status[row][str(no_text+1)] = {
                    "text": str_decoded_msg_text,
                    "answer": str_decoded_csv,
                    "reply_chat": get_reply,
                    "status": status,
                    "percentage": probability
                }
            else:
                # log
                print("percentage:", probability)
                status = "failed"
                print("@reply chat : {}".format(get_reply))
                print("@answer : {}".format(str_decoded_csv))
                print("@status test: {}".format(status))
                # | temporary storage of failed or successful test results
                data_status[row][str(no_text+1)] = {
                    "text": str_decoded_msg_text,
                    "answer": str_decoded_csv,
                    "reply_chat": get_reply,
                    "status": status,
                    "percentage": probability
                }
                # if chat reply failed, send message cancel
                try:
                    cancel = "batal"
                    try:
                        text_field.send_keys(cancel)
                        click_send(span_main)
                    except:
                        pass
                    msgs = cancel
                    response.waiting(driver, class_name,
                                     content, msgs, message_content)
                except:
                    time.sleep(2)

        # | Store all failed or successful test data results with categories based on column header in the CSV file
        data_all[str(label)] = {
            "id": getcsv_id,
            "topik": getcsv_topik,
            "kategori": getcsv_category,
            "nama_label": getcsv_label,
            "hasil": data_status[str(row)]
        }
        # | to save test results based on each row into json format
        dict_one = {}
        dict_one[list(data_all)[-1]] = data_all["label{}".format(line)]

        path_change = "data_file"
        extensi = "result_data_json{}.json".format(
            data_all["label{}".format(line)]["id"])
        # log
        print("##########extensi############################", extensi)
        # ..\automationpy\webchat.py
        file_path = os.path.abspath(__file__)
        # ..\automationpy
        file_dir = os.path.dirname(file_path)
        # ..\automationpy\data_file\json.json
        path_location = os.path.join(file_dir, path_change, extensi)
        # make the file into json
        json_object = json.dumps(dict_one, indent=4)
        with open(path_location, mode="w") as file_jason:
            file_jason.write(json_object)
        # | call function htmlpy_one() to create an html file one line at a time
        packagepy.htmlpy_one(data_all, line, title_page, browser_name, tester)

    path_change = "data_file"
    extensi = "result_data_all.json"
    print("######################################", extensi)
    # ..\automationpy\webchat.py
    file_path = os.path.abspath(__file__)
    # ..\automationpy
    file_dir = os.path.dirname(file_path)
    # ..\automationpy\data_file\json.json
    path_location = os.path.join(file_dir, path_change, extensi)
    json_object = json.dumps(data_all, indent=4)
    with open(path_location, mode="w") as file_jason:
        file_jason.write(json_object)

    return data_all, data_status, title_page, browser_name


def main():
    pass


if __name__ == "__main":
    pass
