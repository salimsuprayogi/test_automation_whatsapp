#!python3
# -*- coding: utf-8 -*-
# automationpy/response
# salim suprayogi
# created 21 Oktober 2020

import time


def waiting(driver, class_name="z_tTQ", content="_2hqOq", msgs="hello", message_content="_3Whw5"):
    # function for waiting reply chat
    print("````1 stoper````")
    send_msgs = msgs
    stoper = True
    while stoper:
        try:
            len_last_chat = driver.find_element_by_class_name(class_name)
            elem_last_chat = len_last_chat.find_elements_by_class_name(
                content)[-1]
            elem_next_text = elem_last_chat.find_elements_by_class_name(
                message_content)
            # log
            # len_msg_content = len(elem_next_text)
            # print("len_msg_content:", len_msg_content)
            reply = []
            for i, val in enumerate(elem_next_text):
                time.sleep(0.5)
                text_list = val.text
                reply.append(text_list)
            get_reply = "\n".join(reply)
            # log
            # print("elem_text:", get_reply)
            # print("profile:", send_msgs)
            try:
                if get_reply.lower().strip() == send_msgs.lower().strip():
                    # print("Please wait....!!!")
                    pass
                elif get_reply.lower().strip() == "":
                    # print("Please wait....!!!")
                    pass
                else:
                    if get_reply.lower().strip() == "menu":
                        stoper = False
                    else:
                        stoper = False
            except:
                pass
        except:
            pass
    print("````2 stoper````")


def get_reply_chat(driver, class_name="z_tTQ", content="_2hqOq", messages="hai", message_content="_3Whw5"):
    # function get reply chat
    message = messages
    print("$ 1 Retrieve Text Reply Chat")
    # if there is 1 chat reply
    reply = []
    try:
        len_last_second = driver.find_element_by_class_name(class_name)
        elem_last_second = len_last_second.find_elements_by_class_name(
            content)[-2]
        elem_second_text = elem_last_second.find_elements_by_class_name(
            message_content)
        # log
        # len_msg_content = len(elem_second_text)
        # print("len_msg_content:", len_msg_content)
        reply_text = []
        for i, val in enumerate(elem_second_text):
            time.sleep(0.5)
            text_list = val.text
            reply_text.append(text_list)
        get_reply_text = "\n".join(reply_text)
        # jika elemen kedua terakhir sama dengan text yang dikirim
        # if last second element equals the sent text
        if get_reply_text.lower().strip() == message.lower().strip():
            # if there is 1 chat reply
            try:
                time.sleep(0.5)
                first_text = driver.find_element_by_class_name(class_name)
                elem_last_first = first_text.find_elements_by_class_name(
                    content)[-1]
                elem_first_text = elem_last_first.find_elements_by_class_name(
                    message_content)
                # log
                # len_msg_content = len(elem_first_text)
                # print("len_msg_content:", len_msg_content)
                # reply = []
                for i, val in enumerate(elem_first_text):
                    time.sleep(0.5)
                    text_list = val.text
                    reply.append(text_list)
                    # log
                    # print("text_data {} :".format(i), text_list)
                # log
                # print(reply)
                # get_reply = "\n".join(reply)
                # print("Balasan Chat hanya satu:\n---\n",
                #       get_reply.strip(), "\n---")
                print("+1 One chat reply")
            except:
                pass
        else:
            pass
    except:
        pass
    # if there is 2 chat reply
    try:
        len_last_third = driver.find_element_by_class_name(class_name)
        elem_last_third = len_last_third.find_elements_by_class_name(
            content)[-3]
        elem_last_third = elem_last_third.find_elements_by_class_name(
            message_content)
        # log
        # len_msg_content = len(elem_last_third)
        # print("len_msg_content:", len_msg_content)
        reply_text = []
        for i, val in enumerate(elem_last_third):
            time.sleep(0.5)
            text_list = val.text
            reply_text.append(text_list)
        get_reply_text = "\n".join(reply_text)
        # jika elemen ketiga terakhir sama dengan text yang dikirim
        if get_reply_text.lower().strip() == message.lower().strip():
            try:
                # reply = []
                loop = -2  # -2,-1 < 0
                while loop < 0:
                    try:
                        time.sleep(0.5)
                        first_text = driver.find_element_by_class_name(
                            class_name)
                        elem_last_first = first_text.find_elements_by_class_name(content)[
                            loop]
                        elem_first_text = elem_last_first.find_elements_by_class_name(
                            message_content)
                        # log
                        # len_msg_content = len(elem_first_text)
                        # print("len_msg_content:", len_msg_content)
                        for i, val in enumerate(elem_first_text):
                            time.sleep(0.5)
                            text_list = val.text
                            reply.append(text_list)
                            # log
                            # print("text_data {} :".format(i), text_list)
                        loop += 1
                        # jika 0 < 0 = Flase [stop]
                    except:
                        pass
                # log
                # print(reply)
                # get_reply = "\n".join(reply)
                # print("Balasan Chat Ada 2:\n---\n",
                #       get_reply.strip(), "\n---")
                print("+2 Two chat reply")
            except:
                pass
        else:
            pass
    except:
        pass
    # if there is 3 chat reply
    try:
        len_last_third = driver.find_element_by_class_name(class_name)
        elem_third_text = len_last_third.find_elements_by_class_name(
            content)[-4]
        elem_last_third = elem_third_text.find_elements_by_class_name(
            message_content)
        # len_msg_content = len(elem_last_third)
        # print("len_msg_content:", len_msg_content)
        reply_text = []
        for i, val in enumerate(elem_last_third):
            time.sleep(0.5)
            text_list = val.text
            reply_text.append(text_list)
        get_reply_text = "\n".join(reply_text)
        # jika elemen keempat terakhir sama dengan text yang dikirim
        if get_reply_text.lower().strip() == message.lower().strip():
            try:
                # reply = []
                loop = -3  # -2,-1 < 0
                while loop < 0:
                    try:
                        time.sleep(0.5)
                        first_text = driver.find_element_by_class_name(
                            class_name)
                        elem_last_first = first_text.find_elements_by_class_name(content)[
                            loop]
                        elem_first_text = elem_last_first.find_elements_by_class_name(
                            message_content)
                        # log
                        # len_msg_content = len(elem_first_text)
                        # print("len_msg_content:", len_msg_content)
                        for i, val in enumerate(elem_first_text):
                            time.sleep(0.5)
                            text_list = val.text
                            reply.append(text_list)
                            # log
                            # print("text_data {} :".format(i), text_list)
                        loop += 1
                        # jika 0 < 0 = Flase [stop]
                    except:
                        pass
                # log
                # print(reply)
                # get_reply = "\n".join(reply)
                # print("Balasan Chat Ada 3:\n---\n",
                #       get_reply.strip(), "\n---")
                print("+3 Three chat reply")
            except:
                pass
        else:
            pass
    except:
        pass
    # if there is 4 chat reply
    try:
        len_last_forth = driver.find_element_by_class_name(class_name)
        elem_forth_text = len_last_forth.find_elements_by_class_name(
            content)[-5]
        elem_last_forth = elem_forth_text.find_elements_by_class_name(
            message_content)
        len_msg_content = len(elem_last_forth)
        # print("len_msg_content:", len_msg_content)
        reply_text = []
        for i, val in enumerate(elem_last_forth):
            time.sleep(0.5)
            text_list = val.text
            reply_text.append(text_list)
        get_reply_text = "\n".join(reply_text)
        # jika elemen keempat terakhir sama dengan text yang dikirim
        if get_reply_text.lower().strip() == message.lower().strip():
            try:
                # reply = []
                loop = -4  # -2,-1 < 0
                while loop < 0:
                    try:
                        time.sleep(0.5)
                        first_text = driver.find_element_by_class_name(
                            class_name)
                        elem_last_first = first_text.find_elements_by_class_name(content)[
                            loop]
                        elem_first_text = elem_last_first.find_elements_by_class_name(
                            message_content)
                        # log
                        # len_msg_content = len(elem_first_text)
                        # print("len_msg_content:", len_msg_content)
                        for i, val in enumerate(elem_first_text):
                            time.sleep(0.5)
                            text_list = val.text
                            reply.append(text_list)
                            # log
                            # print("text_data {} :".format(i), text_list)
                        loop += 1
                        # jika 0 < 0 = Flase [stop]
                    except:
                        pass
                # log
                # print(reply)
                # get_reply = "\n".join(reply)
                # print("Balasan Chat Ada 4:\n---\n",
                #       get_reply.strip(), "\n---")
                print("+4 Four chat reply")
            except:
                pass
        else:
            pass
    except:
        pass
    # if there is 5 chat reply
    try:
        len_last_five = driver.find_element_by_class_name(class_name)
        elem_five_text = len_last_five.find_elements_by_class_name(content)[-5]
        elem_last_five = elem_five_text.find_elements_by_class_name(
            message_content)
        len_msg_content = len(elem_last_five)
        # print("len_msg_content:", len_msg_content)
        reply_text = []
        for i, val in enumerate(elem_last_five):
            time.sleep(0.5)
            text_list = val.text
            reply_text.append(text_list)
        get_reply_text = "\n".join(reply_text)
        # jika elemen keempat terakhir sama dengan text yang dikirim
        if get_reply_text.lower().strip() == message.lower().strip():
            try:
                # reply = []
                loop = -5  # -2,-1 < 0
                while loop < 0:
                    try:
                        time.sleep(0.5)
                        first_text = driver.find_element_by_class_name(
                            class_name)
                        elem_last_first = first_text.find_elements_by_class_name(content)[
                            loop]
                        elem_first_text = elem_last_first.find_elements_by_class_name(
                            message_content)
                        # log
                        # len_msg_content = len(elem_first_text)
                        # print("len_msg_content:", len_msg_content)
                        for i, val in enumerate(elem_first_text):
                            time.sleep(0.5)
                            text_list = val.text
                            reply.append(text_list)
                            # log
                            # print("text_data {} :".format(i), text_list)
                        loop += 1
                        # jika 0 < 0 = Flase [stop]
                    except:
                        pass
                # log
                # print(reply)
                # get_reply = "\n".join(reply)
                # print("Balasan Chat Ada 5:\n---\n",
                #       get_reply.strip(), "\n---")
                print("+5 Five chat reply")
            except:
                pass
        else:
            pass
    except:
        pass
    # log
    # print(reply)
    print("$ 2 Retrieve Text Reply Chat")

    return reply
