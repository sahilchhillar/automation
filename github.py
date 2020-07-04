from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os, sys


def browseGit(username, password, repoName):
    driver = webdriver.Chrome()
    driver.get('https://github.com/login')
    python_button = driver.find_elements_by_xpath("//*[@id='login_field']")[0]
    python_button.send_keys(username)

    python_button = driver.find_elements_by_xpath("//*[@id='password']")[0]
    python_button.send_keys(password)

    python_button = driver.find_elements_by_xpath("//*[@id='login']/form/div[4]/input[9]")[0]
    python_button.click()

    driver.get('https://github.com/new')
    python_button = driver.find_elements_by_xpath("//*[@id='repository_name']")[0]
    python_button.send_keys(repoName)

    python_button = driver.find_element_by_css_selector('button.first-in-line')
    python_button.submit()

    
    os.system("git init")
    os.system("git remote add origin https://github.com/sahilchhillar/" + repoName + ".git")
    os.system("touch README.md")
    os.system("git add .")
    os.system('git commit -m "first commit"')
    os.system("git push -u origin master")

    browser.quit()


def createFolder(projectLocation, projectName):
    exist = os.path.isdir(projectLocation + "/" + projectName)
    if exist:
        os.chdir(projectName)
    else:
        projectNameCommand = "mkdir " + projectName
        os.system(projectNameCommand)
        os.chdir(projectName)

projectLocation = "/home/hp/Documents"
os.chdir(projectLocation)

projectName = str(input("Enter the project name:"))

createFolder(projectLocation, projectName)

username = '<username>'
password = '<password>'
repoName = str(input("Enter the repository name:"))

browseGit(username, password, repoName)
