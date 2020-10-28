#!python3
# -*- coding: utf-8 -*-
# automationpy/packagepy/datacsv
# salim suprayogi
# created 21 Oktober 2020

import os
import csv
import json


def data_csv(filename_csv):
    # function retrieve all csv file data
    file_data_csv = {}
    # direktori file csv
    path_change = "../automationpy_wa/data_csv"
    # path = "/users/smart/automationpy"
    # working directory
    working_dir = os.getcwd()
    # change new working directory
    os.chdir(path_change)
    # working directory [aktif]
    working_dir = os.getcwd()
    path_filename_csv = "{}\{}".format(working_dir, filename_csv)
    # encoding="utf-8" or encoding="cp1252"
    with open(path_filename_csv, "r", encoding="cp1252") as readers:
        file_csv = csv.reader(readers)
        # skip header / title
        # fields = next(berkas_csv)
        for row, line in enumerate(file_csv):
            file_data_csv["row{}".format(row)] = line

    path_change = "data_file"
    extensi = "{}.json".format(filename_csv)
    # ..\automationpy\packagepy\datacsv.py
    file_path = os.path.abspath(__file__)
    # ..\automationpy\packagepy
    file_dir = os.path.dirname(file_path)
    # ..\automationpy
    parent_dir = os.path.dirname(file_dir)
    # ..\automationpy\data_file\json.json
    path_location = os.path.join(parent_dir, path_change, extensi)
    json_object = json.dumps(file_data_csv, indent=4)
    with open(path_location, mode="w") as file_jason:
        file_jason.write(json_object)

    return file_data_csv  # return dictionary = {}


def data_header(filename_csv, ids, topik, category, label, answer, text1):
    # function read header csv file
    header_text = []
    datacsv = data_csv(filename_csv)
    for no in range(len(datacsv["row0"])):
        header_text.append(datacsv["row0"][no].lower().strip())
    # check title indeks csv, get coloumn data
    no_id = header_text.index(ids.strip().lower())
    no_topik = header_text.index(topik.strip().lower())
    no_category = header_text.index(category.strip().lower())
    no_label = header_text.index(label.strip().lower())
    no_answer = header_text.index(answer.strip().lower())
    no_text1 = header_text.index(text1.strip().lower())

    return no_id, no_topik, no_category, no_label, no_answer, no_text1, datacsv


def main():
    pass


if __name__ == "__main__":
    pass
