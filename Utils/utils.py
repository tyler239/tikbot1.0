import random, os, pyautogui, re
from time import sleep


#Random wait time for actions --->Both
randomAwait = lambda : sleep(random.randint(3,5))

#Random wait time for typing --->Both
randomTypeAwait = lambda : sleep(random.randint(1,2)/10)

#Wait time for page to load --->Both
awaitPage = lambda driver : driver.implicity_wait(20)   


#--->Pureautogui.py
def deleteAutoGui() :
       for _ in range(3) : pyautogui.hotkey('ctrl', 'right')
       for _ in range(50) : pyautogui.press('backspace')

#--->Pureautogui.py
def locateAndClick(image) :
        p = os.path.join(os.getcwd(), 'Assets', 'Images', 'English',  image)

        for i in range(3) :
                c = 0.9 - (i/10 if i != 0 else 0)
                t = pyautogui.locateCenterOnScreen(p, grayscale=False, confidence=c)
                if(t) :
                      pyautogui.click(t, duration = random.randint(1,3))

#Selecting which video to upload, returning the path to upload it --->Both
def videoPath() :
        numbers = []
        path = os.path.join(os.getcwd(), '..', 'Assets', 'Videos')
        for filename in os.listdir(path) :
                numbers.append(re.search(r'\d+', filename).group())
        if len(numbers) == 0 : return 1
        return os.path.join(os.getcwd(), '..', 'Assets', 'Videos', 'video' + min(numbers) + '.mp4')



