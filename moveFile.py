import os, shutil

dirPath = "/home/hp/Downloads"
os.chdir(dirPath)

folders = os.listdir()

for file in folders:
    if file.endswith(".pdf"):
        source = os.path.abspath(file)
        if os.path.isdir(dirPath + "/pythonPdf"):
            shutil.move(source, os.path.abspath("pythonPdf"))
        else:
            os.system("mkdir pythonPdf")
            shutil.move(source, os.path.abspath("pythonPdf"))

    if file.endswith(".zip"):
        source = os.path.abspath(file)
        if os.path.isdir(dirPath + "/zipFiles"):
            shutil.move(source, os.path.abspath("zipFiles"))
        else:
            os.system("mkdir zipFiles")
            shutil.move(source, os.path.abspath("zipFiles"))

    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
        source = os.path.abspath(file)
        if os.path.isdir(dirPath + "/picFiles"):
            shutil.move(source, os.path.abspath("picFiles"))
        else:
            os.system("mkdir picFiles")
            shutil.move(source, os.path.abspath("picFiles"))

    if file.endswith(".docx") or file.endswith(".xlsx"):
        source = os.path.abspath(file)
        if os.path.isdir(dirPath + "/docs"):
            shutil.move(source, os.path.abspath("docs"))
        else:
            os.system("mkdir docs")
            shutil.move(source, os.path.abspath("docs"))