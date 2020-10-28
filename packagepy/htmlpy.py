#!python3
# -*- coding: utf-8 -*-
# automationpy/packagepy/htmlpy
# salim suprayogi
# created 21 Oktober 2020
# create html with dominate

import dominate
from dominate.tags import *
import os
import io
import whatsapp


def nama_tester(tester="Salim Suprayogi"):
    # Function name tester
    nama_tester = tester
    return nama_tester


def htmlpy_one(data_all, line, title_page, browser_name, tester):
    # function create file html, each line/row of the csv file
    # if data_all["label{}".format(line)]:
    print(data_all["label{}".format(line)]["id"])
    # html title page
    deta = dominate.document(
        title="Test Automation {}".format(title_page))
    # html head
    with deta.head:
        meta(charset="UTF-8")
        meta_ctn = "width=device-width"
        meta_is = "initial-scale="
        meta_num = "1.0"
        meta_ctn_all = '{} {}{}'.format(
            meta_ctn, meta_is, meta_num)
        meta(content=meta_ctn_all, name="viewport")
        # css file
        # link(rel="stylesheet", href="./style.css")
        style(
            """\
            html {
            width: 100%;
            }

            body {
            font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
            font-size: small;
            box-sizing: border-box;
            }

            h1 {
            text-align: center;
            border: 2px solid whitesmoke;
            background-color: #4caf50;
            color: white;
            padding: 8px;
            box-shadow: 0px 0px 1px 0px grey;
            border-radius: 1px;
            margin-bottom: 15px;
            }

            .header {
            box-shadow: 0px 0px 1px 0px grey;
            border-radius: 1px;
            border: 1px solid whitesmoke;
            /* box-shadow: 0px 0px 1px 0px grey;
            border-radius: 1px; */
            padding: 8px;
            /* padding-bottom: 5px; */
            margin-bottom: 15px;
            text-align: justify;
            }

            .profile {
            /* box-shadow: 0px 0px 1px 0px grey;
            border-radius: 1px;
            text-align: left;
            border: 1px solid whitesmoke;
            background-color: #4caf50;
            color: white; */
            font-weight: normal;
            /* margin: 1px;
            padding: 8px; */
            }

            .header3,
            .paragraf {
            text-align: justify;
            /* border-bottom-style: solid; */
            /* border-bottom-color: #83c985; */
            /* margin: 2px; */
            /* padding: auto; */
            margin-top: 15px;
            }

            h2 {
            background-color: #4caf50;
            color: white;
            padding-top: 10px;
            padding-bottom: 10px;
            text-align: center;
            }

            h3,
            p {
            font-weight: normal;
            }

            #main {
            border-collapse: collapse;
            width: 100%;
            font-weight: normal;
            text-align: justify;
            }

            .container {
            box-shadow: 0px 0px 1px 0px green;
            border-radius: 1px;
            border: 1px solid whitesmoke;
            padding: 5px;
            padding-bottom: 20px;
            margin-bottom: 15px;
            }

            #main th {
            position: sticky;
            top: 0;
            }

            #main td,
            #main th {
            border: 1px solid #ddd;
            padding: 5px;
            }
            
            #main tr:hover {
            /*padding-top: 5px;
            padding-bottom: 5px;
            text-align: left;*/
            background-color: #4caf50;
            }
            
            #main th {
            padding-top: 5px;
            padding-bottom: 5px;
            text-align: left;
            background-color: #4caf50;
            color: white;
            }

            h4 {
            text-align: center;
            border: 2px solid whitesmoke;
            background-color: #ddd;
            color: darkslateblue;
            padding: 8px;
            margin-bottom: 15px;
            }

            .success {
            background-color: #4caf50;
            color: white;
            text-align: justify;
            }

            .failed {
            background-color: deeppink;
            color: white;
            text-align: justify;
            }
            """
        )
    with deta:
        # html report title
        h1("Test Report {}".format(title_page))
        with div():
            attr(cls="header")
            with p():
                p(
                    "Name : {}".format(nama_tester(tester)), cls="profile"
                )
                p(
                    "Date : {}".format(today_date), cls="profile"
                )
                p(
                    "Title Page : {}".format(title_page), cls="profile"
                )
                p(
                    "Browser Name : {}".format(browser_name), cls="profile"
                )
        # read result data test from dictionary
        with div(cls="container"):
            # data header csv
            # table html
            with table(id="main", cls="table-striped"):
                h2(
                    "Test Results Message {}".format(title_page), cls="header2"
                )
                # get no id csv
                h3(
                    "Id : {}".format(data_all["label{}".format(line)]["id"]), cls="header3"
                )
                # get topik csv
                p(
                    "Topic : {}".format(data_all["label{}".format(line)]["topik"]), cls="paragraf"
                )
                # get Category csv
                p(
                    "Category : {}".format(data_all["label{}".format(line)]["kategori"]), cls="paragraf"
                )
                # get name label csv
                p(
                    "Label : {}".format(data_all["label{}".format(line)]["nama_label"]), cls="paragraf"
                )
                br()
                # header table
                with thead():
                    # row header
                    with tr():
                        th("No")
                        th("Question")
                        th("Reply Chat") 
                        th("Answer")
                        th("Status Pass")
                        th("Status Failed")
                        th("Probability")
                for no_row, rows in enumerate(data_all["label{}".format(line)]["hasil"]):
                    no_row = str(no_row+1)
                    id = rows
                    # body table
                    with tbody():
                        # row table
                        with tr():
                            # no 1
                            with td():
                                p(id)
                            # question text
                            with td():
                                p(
                                    data_all["label{}".format(
                                        line)]["hasil"][no_row]["text"],
                                    cls="question-text"
                                )
                            # result bot
                            with td():
                                p(
                                    data_all["label{}".format(
                                        line)]["hasil"][no_row]["reply_chat"],
                                    cls="msg-body"
                                )
                            # answer
                            with td():
                                p(
                                    data_all["label{}".format(
                                        line)]["hasil"][no_row]["answer"]
                                )
                            # status
                            if "pass" in data_all["label{}".format(line)]["hasil"][no_row]["status"].lower().strip():
                                td(
                                    "PASS",
                                    cls="success"
                                )
                                td("-")
                            else:
                                # "failed" in if "pass" in data_all[no_label]["hasil"][no_row]["status"].lower().strip():
                                td("-")
                                td(
                                    "FAILED",
                                    cls="failed"
                                )
                            with td():
                                p(
                                    data_all["label{}".format(
                                        line)]["hasil"][no_row]["percentage"]
                                )
        # footer html
        with div():
            attr(cls='footer')
            h4(
                "@botika.online by salim suprayogi"
            )
    path_change = "data_report"
    extensi = "result_data_html{}.html".format(
        data_all["label{}".format(line)]["id"])
    print("########extensi##############################", extensi)
    # ..\automationpy\packagepy\htmlpy.py
    file_path = os.path.abspath(__file__)
    # ..\automationpy\packagepy
    file_dir = os.path.dirname(file_path)
    # ..\automationpy
    parent_dir = os.path.dirname(file_dir)
    # ..\automationpy\data_report\html.html
    path_location = os.path.join(parent_dir, path_change, extensi)
    with io.open(path_location, mode="w", encoding="utf-8") as filehtml:
        filehtml.write(deta.render())


def htmlpy(data_all, data_webchat, title_page, browser_name, file_html, tester):
    # function create html file from all data test
    # data_webchat = dictionary hasil test ,pass,failed,question,reply chat,answer

    # data_all[str(label)==label1] = {
    #     "id": getcsv_id,
    #     "topik": getcsv_topik,
    #     "kategori": getcsv_category,
    #     "nama_label": getcsv_label,
    #     "hasil": data_status[str(row)==row1{}]
    # }
    # data_all[label1]["id"]
    # data_all[label1]["topik"]
    # data_all[label1]["kategori"]
    # data_all[label1]["nama_label"]
    # data_all[label1]["hasil"]

    # html title page
    deta_all = dominate.document(title="Test Automation {}".format(title_page))
    # html head
    with deta_all.head:
        meta(charset="UTF-8")
        meta_ctn = "width=device-width"
        meta_is = "initial-scale="
        meta_num = "1.0"
        meta_ctn_all = '{} {}{}'.format(meta_ctn, meta_is, meta_num)
        meta(content=meta_ctn_all, name="viewport")
        # css file
        # link(rel="stylesheet", href="./style.css")
        style(
            """\
            html {
            width: 100%;
            }

            body {
            font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
            font-size: small;
            box-sizing: border-box;
            }

            h1 {
            text-align: center;
            border: 2px solid whitesmoke;
            background-color: #4caf50;
            color: white;
            padding: 8px;
            box-shadow: 0px 0px 1px 0px grey;
            border-radius: 1px;
            margin-bottom: 15px;
            }

            .header {
            box-shadow: 0px 0px 1px 0px grey;
            border-radius: 1px;
            border: 1px solid whitesmoke;
            /* box-shadow: 0px 0px 1px 0px grey;
            border-radius: 1px; */
            padding: 8px;
            /* padding-bottom: 5px; */
            margin-bottom: 15px;
            text-align: justify;
            }

            .profile {
            /* box-shadow: 0px 0px 1px 0px grey;
            border-radius: 1px;
            text-align: left;
            border: 1px solid whitesmoke;
            background-color: #4caf50;
            color: white; */
            font-weight: normal;
            /* margin: 1px;
            padding: 8px; */
            }

            .header3,
            .paragraf {
            text-align: justify;
            /* border-bottom-style: solid; */
            /* border-bottom-color: #83c985; */
            /* margin: 2px; */
            /* padding: auto; */
            margin-top: 15px;
            }

            h2 {
            background-color: #4caf50;
            color: white;
            padding-top: 10px;
            padding-bottom: 10px;
            text-align: center;
            }

            h3,
            p {
            font-weight: normal;
            }

            #main {
            border-collapse: collapse;
            width: 100%;
            font-weight: normal;
            text-align: justify;
            }

            .container {
            box-shadow: 0px 0px 1px 0px green;
            border-radius: 1px;
            border: 1px solid whitesmoke;
            padding: 5px;
            padding-bottom: 20px;
            margin-bottom: 15px;
            }

            #main th {
            position: sticky;
            top: 0;
            }

            #main td,
            #main th {
            border: 1px solid #ddd;
            padding: 5px;
            }
            
            #main tr:hover {
            /*padding-top: 5px;
            padding-bottom: 5px;
            text-align: left;*/
            background-color: #4caf50;
            }
            
            #main th {
            padding-top: 5px;
            padding-bottom: 5px;
            text-align: left;
            background-color: #4caf50;
            color: white;
            }

            h4 {
            text-align: center;
            border: 2px solid whitesmoke;
            background-color: #ddd;
            color: darkslateblue;
            padding: 8px;
            margin-bottom: 15px;
            }

            .success {
            background-color: #4caf50;
            color: white;
            text-align: justify;
            }

            .failed {
            background-color: deeppink;
            color: white;
            text-align: justify;
            }
            """
        )
    with deta_all:
        # html report title
        h1("Test Report {}".format(title_page))
        with div():
            attr(cls="header")
            with p():
                p(
                    "Name : {}".format(nama_tester(tester)), cls="profile"
                )
                p(
                    "Date : {}".format(today_date), cls="profile"
                )
                p(
                    "Title Page : {}".format(title_page), cls="profile"
                )
                p(
                    "Browser Name : {}".format(browser_name), cls="profile"
                )
        # read result data test from dictionary
        for no_label in data_all:
            with div(cls="container"):
                # data header csv
                # table html
                with table(id="main", cls="table-striped"):
                    h2(
                        "Test Results Message {}".format(title_page), cls="header2"
                    )
                    # get no id csv
                    # data_all[label1==no_label]["id"]
                    h3(
                        "Id : {}".format(data_all[no_label]["id"]), cls="header3"
                    )
                    # get topik csv
                    p(
                        "Topic : {}".format(data_all[no_label]["topik"]), cls="paragraf"
                    )
                    # get category csv
                    p(
                        "Category : {}".format(data_all[no_label]["kategori"]), cls="paragraf"
                    )
                    # get name label csv
                    p(
                        "Label : {}".format(data_all[no_label]["nama_label"]), cls="paragraf"
                    )
                    br()
                    # header table
                    with thead():
                        # row header
                        with tr():
                            th("No")
                            th("Question")
                            th("Reply Chat")
                            th("Answer")
                            th("Status Pass")
                            th("Status Failed")
                            th("Probability")
                    for no_row, rows in enumerate(data_all[no_label]["hasil"]):
                        no_row = str(no_row+1)
                        id = rows
                        # body table
                        with tbody():
                            # row table
                            with tr():
                                # no 1
                                with td():
                                    p(id)
                                # question text
                                with td():
                                    p(
                                        data_all[no_label]["hasil"][no_row]["text"],
                                        cls="question-text"
                                    )
                                # reply_chat
                                with td():
                                    p(
                                        data_all[no_label]["hasil"][no_row]["reply_chat"],
                                        cls="msg-body"
                                    )
                                # answer
                                with td():
                                    p(
                                        data_all[no_label]["hasil"][no_row]["answer"]
                                    )
                                # status
                                # data_all[label1]["hasil"]
                                if "pass" in data_all[no_label]["hasil"][no_row]["status"].lower().strip():
                                    td(
                                        "PASS",
                                        cls="success"
                                    )
                                    td("-")
                                else:
                                    # "failed" in if "pass" in data_all[no_label]["hasil"][no_row]["status"].lower().strip():
                                    td("-")
                                    td(
                                        "FAILED",
                                        cls="failed"
                                    )
                                with td():
                                    p(
                                        data_all[no_label]["hasil"][no_row]["percentage"]
                                    )
        # footer html
        with div():
            attr(cls='footer')
            h4(
                "@botika.online by salim suprayogi"
            )

    path_change = "data_report"
    extensi = "{}.html".format(file_html)
    print("########extensi##############################", extensi)
    # ..\automationpy\packagepy\htmlpy.py
    file_path = os.path.abspath(__file__)
    # ..\automationpy\packagepy
    file_dir = os.path.dirname(file_path)
    # ..\automationpy
    parent_dir = os.path.dirname(file_dir)
    # ..\automationpy\data_report\html.html
    path_location = os.path.join(parent_dir, path_change, extensi)
    with io.open(path_location, mode="w", encoding="utf-8") as filehtml:
        filehtml.write(deta_all.render())


today_date = whatsapp.to_days()


def main():
    pass


if __name__ == "__main__":
    pass
