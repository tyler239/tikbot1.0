#Importing the libraries
import webbrowser, pyautogui
from Utils.utils import *

#Put here the (x,y) location of the required elements
profile_icon = (1332,115)
logout_location = (1240,462)
search_bar = (505,657)
open_button_of_search_bar = (1191,687)


def main() :
    accounts = getAccounts()
    path = getVideoPath() 

    for account in accounts :

        #Browse to the tiktok page
        webbrowser.open('https://www.tiktok.com/')
        awaitPure()

        #Clicking on the login button
        try : locateAndClick('login.png')
        except : logout(profile_icon, logout_location)
        randomAwait()

        #Click in the button "Use phone/ email/ username"
        locateAndClick('phoneuseremail.png')
        randomAwait()

        #Click in log in with email or username
        locateAndClick('emailOrUsername.png')
        randomAwait()

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
        try : locateAndClick('upload.png')
        except : logout(profile_icon, logout_location)

        awaitPure()

        #Check if there is a captcha
        captchaWithOutThread()
    
        #Click on "select file" button
        try : locateAndClick('selectFile.png')
        except : logout(profile_icon, logout_location)

        randomAwait()

        #Click on the search bar of the archive explorer
        pyautogui.click(search_bar ,duration = 1)

        #Put the path of the video
        pyautogui.typewrite(path, interval = 0.1)

        #Click in open
        pyautogui.click(open_button_of_search_bar,duration = 1)
        awaitPure()

        #Add captions
        try : locateAndClick('hashtag.png')
        except : logout(profile_icon, logout_location)

        deleteAutoGui()
        pyautogui.typewrite(account[2], interval = 0.1)
        randomAwait()

        #Add description here if necessary !!!!!!!!!
        
        #Scroll down to post the video
        pyautogui.scroll(-1000)
        randomAwait()

        #Click on the post button
        try : locateAndClick('post.png')
        except : logout(profile_icon, logout_location)
             
        awaitPure()
 
        #Check if there is a captcha
        captchaWithOutThread()

        #Click on the profile button
        try : locateAndClick('viewProfile.png')
        except : logout(profile_icon, logout_location)
             
        awaitPure()

        #Check if there is a captcha
        captchaWithOutThread()

        #Click on the log out button
        logout(profile_icon, logout_location)
        
        #Close the window
        pyautogui.hotkey('ctrl', 'w')
        
   

if __name__ == '__main__' :
    main()