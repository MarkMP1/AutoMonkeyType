from bs4 import BeautifulSoup
import pyautogui
from selenium import webdriver
import time
pyautogui.FAILSAFE = False


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)
browser.get('http://monkeytype.com/')
timeToStop = time.time() + 33
lol = 0
lastword = ""
lol100 = False
firstTime = True




time.sleep(3)




while time.time() < timeToStop:
    if lol == 100:
        pageSource = browser.execute_script("return document.documentElement.outerHTML;")
        lol100 = True
        lol = 0
    pageSource = browser.execute_script("return document.documentElement.outerHTML;")
    soup = BeautifulSoup(pageSource, "html.parser")
    words = soup.findAll("div", {"class": "word"})
    if firstTime:
        firstTime = False
        type = ""
        for item in words:
            type += item.text
            lastword = item.text
            type += " "
            lol+= 1
        pyautogui.write(type)
    else:
        for item in words:
            if(time.time() >  timeToStop):
                break
            if(lol100 == True):
                if(item.text == lastword):
                    lol100 = False
                    continue
            if lol100 == False:
                pyautogui.write(item.text + " ")
                lol += 1
                lastword = item.text
print("Finished.")