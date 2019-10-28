# coding:utf-8
from selenium import webdriver
# from selenium.common.exceptions import ElementNotVisibleException
from time import sleep
import sys

args = sys.argv
count = args[1]

# FIXME: Your Driver Path
driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver\chromedriver.exe")

faces = set()

with open("data/face_list.txt", "r") as f:
    line = f.readline()
    while line:
        print(line)
        faces.add(line.replace("\n", ""))
        line = f.readline()

for i in range(int(count)):
    driver.get("https://ask.fm")
    face_tablet = driver.find_elements_by_class_name("faces")[0].find_elements_by_tag_name('a')
    tmp_faces = {f.text for f in face_tablet}
    faces = faces | tmp_faces
    print("face_length: {}".format(len(faces)))
    sleep(2)
    if i // 10 == 0:
        driver.refresh()

print(faces)

faces.discard("")

with open("data/face_list.txt", "w") as f:
    for face in faces:
        f.write(face)
        f.write("\n")

driver.quit()
