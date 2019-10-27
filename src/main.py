# coding:utf-8
from selenium import webdriver
# from selenium.common.exceptions import ElementNotVisibleException
from time import sleep
import codecs

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
    print('Last page')

    page_source = driver.page_source

    questions = driver.find_elements_by_class_name("streamItem_header")
    answers = driver.find_elements_by_class_name("streamItem_content")

    q_and_a = [(q.find_element_by_tag_name('h2').text, a.text) for q, a in zip(questions, answers)]

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
