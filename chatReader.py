from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from timeit import default_timer
import time
import pyttsx3

import simpleaudio as sa


url = "streamlabs URL"
resetComment = 30


from selenium import webdriver
# Set up the driver (e.g. Chrome)
driver = webdriver.Chrome()
# Navigate to the website
engine = pyttsx3.init()
engine.setProperty("rate", 150)

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[2].id)  # this is female voice in spanish in my system, change it depending on your installed voices. 



driver.get(url)
hashOfComments = []
k = 1

while k < resetComment:
    body = driver.find_elements(By.ID, "log")

    for i in body:
        comments = i.text.split('\n')
        if comments == ['']:
            comments = []
        for comment in comments:
            if hash(comment) not in hashOfComments:
                hashOfComments.append(hash(comment))

                ##GENERATE COMMNET
                commentAuthor = comment.split(' ')[0] 
                commentComment = comment.split(' ')[1:]
                
                commentString = ''
                for words in commentComment:
                    commentString = commentString + words + ''


                finalComment = commentAuthor + '  Dice    ' + commentString
                print(finalComment)
                

                engine.save_to_file(finalComment, finalComment + '.mp3')
                engine.say(finalComment)
                engine.runAndWait()

                
    time.sleep(1)
    #reset comments
    if k == (resetComment - 1):
        hashOfComments = []
        k = 0
        driver.get(url)
    k+=1


