#Importing the libraries
import webbrowser, pyautogui, os, time, threading
from time import sleep
import random 
from Utils.utils import *

#Getting the accounts information from the file
def getAccounts() :
    accounts = []
    path = os.path.join(os.getcwd(), 'Accounts', 'accounts.txt')
    with open(os.path.abspath(path) ,'r') as file :
        for line in file :
              t = tuple(el.strip() for el in line.split(','))
              accounts.append(t)
    return accounts


#Excluding the video that was uploaded in all accounts
def excludeUsedVideo(path) :
        os.remove(path)

def likeRandomVideo() : 
      x = random.randint(1,4)
      for _ in range(1,x) : 
            
            #Await for a sec
            if (int(time.time())%5 == 0) : awaitPure()
            else : randomAwait()

            #Like a video or do a random movement
            if(int(time.time())%3 == 0) : locateAndClick('like.png')
            else : randomMovement()

            pyautogui.scroll(-1100)
            sleep(random.randint(1,2))
            pyautogui.scroll(-1100)


def captchaThread() :
    global CAPTCHA
    global FLAG

    while (not CAPTCHA) and FLAG : 
        if pyautogui.locateOnScreen('Assets\Images\English\captcha.png') or pyautogui.locateOnScreen('Assets\Images\English\dragAndSlide.png') :
            CAPTCHA = True
        
        #Ousing the thread for 3 seconds
        sleep(3)

def captchaPresent() :
    global CAPTCHA
    if(CAPTCHA) :
          input('Captcha DETECTED, resolve mannually the captcha and after press "ENTER" to continue the program')
          CAPTCHA = False
          print('The program will continue in 30 seconds...')
          awaitPure()

def captchaWithOutThread() :
    randomAwait()
    if(pyautogui.locateOnScreen('Assets\Images\English\captcha.png') or 
       pyautogui.locateOnScreen('Assets\Images\English\dragAndSlide.png') or 
       pyautogui.locateOnScreen('Assets\Images\Portuguese\3D.png') or 
       pyautogui.locateOnScreen('Assets\Images\Portuguese\3D2.png')
       ):
        input('Captcha DETECTED, resolve mannually the captcha and after press "ENTER" to continue the program')
        print('The program will continue in 30 seconds...')
        awaitPure()

        
def randomMovement() :
      pyautogui.moveRel(random.randint(-100,100), random.randint(-100,100), duration = 0.5)

      
def awaitPure() :
    sleep(random.randint(15,20))


def main() :
    accounts = getAccounts()
    path = videoPath()
    if(path == 1) : 
          print('There is no video to upload')
          return    

    for account in accounts :

        #Browse to the tiktok page
        webbrowser.open('https://www.tiktok.com/')
        awaitPure()

        #Clicking on the login button
        locateAndClick('login.png')
        sleep(2)

        #Click in the button "Use phone/ email/ username"
        locateAndClick('phoneuseremail.png')

        #Click in log in with email or username
        locateAndClick('emailOrUsername.png')

        #Put the email
        pyautogui.moveRel(-20,45)
        pyautogui.click()
        pyautogui.typewrite(account[0], interval = 0.25)
        pyautogui.press('enter')

        #Put the password
        pyautogui.moveRel(0,55)
        pyautogui.click()
        pyautogui.typewrite(account[1], interval = 0.25)
        pyautogui.press('enter')
        awaitPure()

        #Check if there is a captcha
        captchaWithOutThread()

        #Possibly like a video
        likeRandomVideo()
        randomAwait()

        #Click in upload video
        locateAndClick('upload.png')
        awaitPure()

        #Check if there is a captcha
        captchaWithOutThread()
    
        #Click on "select file" button
        locateAndClick('selectFile.png')
        randomAwait()

        #Click on the search bar of the archive explorer
        pyautogui.click(505,657,duration = 1)

        #Put the path of the video
        pyautogui.typewrite(path, interval = 0.1)

        #Click in open
        pyautogui.click(1191,687,duration = 1)
        awaitPure()

        #Add captions
        locateAndClick('hashtag.png')
        deleteAutoGui()
        pyautogui.typewrite('test', interval = 0.1)
        randomAwait()

        #Add description here if necessary !!!!!!!!!
        
        #Scroll down to post the video
        pyautogui.scroll(-1000)
        randomAwait()

        #Click on the post button
        locateAndClick('post.png')
        awaitPure()
 
        #Check if there is a captcha
        captchaWithOutThread()

        #Click on the profile button
        locateAndClick('viewProfile.png')
        awaitPure()

        #Check if there is a captcha
        captchaWithOutThread()

        #Click on the log out button
        pyautogui.click(1332,115,duration = 1)
        pyautogui.click(1240,462,duration = 1)
        awaitPure()
        
        #Close the window
        pyautogui.hotkey('ctrl', 'w')
        
    excludeUsedVideo(path)
   

if __name__ == '__main__' :
    main()

#Para ver se o cara já tinha curtido o vídeo
#imagem = pyautogui.locateOnScreen('img.png')
#Pyautogui can press the keyboard keys
#too

