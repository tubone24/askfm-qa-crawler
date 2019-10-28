# coding:utf-8
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import codecs
from datetime import datetime

# FIXME: Your Driver Path
driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver\chromedriver.exe")

faces = set()

with open("data/face_list.txt", "r") as f:
    line = f.readline().replace("\n", "")
    while line:
        print(line)
        faces.add(line)
        line = f.readline().replace("\n", "")

faces.discard("")

for face in faces:
    driver.get("https://ask.fm/" + face)
    driver.execute_script("document.body.style.zoom='50%'")

    while True:
        scroll_h = driver.execute_script("var h = window.pageYOffset; return h")
        judge = driver.execute_script("var m = window.pageYOffset; return m")
        previous_h = driver.execute_script("var h = window.pageYOffset; return h")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(3)
        after_h = driver.execute_script("var h = window.pageYOffset; return h")
        if previous_h == after_h:
            break
    print("Scroll All Page {face} {time}".format(face=face, time=datetime.now()))

    page_source = driver.page_source

    qa_elements = driver.find_elements_by_class_name("streamItem-answer")

    print("QA content: {}".format(len(qa_elements)))

    # q_and_a = [(qa.find_element_by_class_name("streamItem_header").find_element_by_tag_name('h2').text,
    #             qa.find_element_by_class_name("streamItem_content").text) for qa in qa_elements]

    q_and_a = []
    for qa in qa_elements:
        try:
            q = qa.find_element_by_class_name("streamItem_header").find_element_by_tag_name('h2').text
        except (ElementNotVisibleException, NoSuchElementException) as e:
            print("ElementNotVisible: {}".format(e))
            continue
        try:
            a = qa.find_element_by_class_name("streamItem_content").text
        except (ElementNotVisibleException, NoSuchElementException) as e:
            try:
                print("Check Answer card...")
                a = qa.find_element_by_class_name("asnwerCard_text").text
            except (ElementNotVisibleException, NoSuchElementException) as e:
                print("ElementNotVisible: {}".format(e))
                continue
        q_and_a.append((q, a))

    with codecs.open("data/askfm_data/" + face + ".txt", "w", "utf-8") as f:
        for q, a in q_and_a:
            if q == '' or a == '' or 'http' in q or 'http' in a:
                continue
            q = q.replace('\n', '')
            a = a.replace('\n', '')
            f.write(q)
            f.write('\n')
            f.write(a)
            f.write('\n')
            f.write('\n')

driver.quit()
