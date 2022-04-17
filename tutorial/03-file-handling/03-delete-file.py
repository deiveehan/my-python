import os

fileName = "keerthana_grades.txt"
if(os.path.exists(fileName)):
    os.remove(fileName)
    print("file deleted !!")
else:
    print("The file does not exists")

