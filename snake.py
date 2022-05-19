import pyautogui
import time

gm = 2

if gm == 0:
    LONG = 0.5761                                                                           
    HALF = 0.25
    FULL1 = 0.721
    FULL2 = 0.686
    SPECIAL1 = 0.45
    SPECIAL2 = 0.105

elif gm == 1:
    # Medium
    LONG = 0.823
    HALF = 0.53
    FULL1 = 1.03
    FULL2 = 0.98
    SPECIAL1 = 0.71
    SPECIAL2 = 0.15

elif gm == 2:
    # Slow
    LONG = 1.184
    LONG = 1.2
    HALF = 0.67
    FULL1 = 1.42
    FULL2 = 1.38
    SPECIAL1 = 1.0
    SPECIAL2 = 0.195

def left():
    pyautogui.press('left')
def right():
    pyautogui.press('right')
def up():
    pyautogui.press('up')
def down():
    pyautogui.press('down')
def sleep(sec: float):
    time.sleep(sec)

def stan_up():
    left()
    up()
    sleep(LONG)
    
def stan_down():
    left()
    down()
    sleep(LONG)




def main():

    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')
    time.sleep(1)
    # for i in range(19):
    #     pyautogui.press('tab')
    pyautogui.press('enter')


    right()
    sleep(SPECIAL1)
    pyautogui.press('up')
    sleep(HALF)
    fullGame()


def fullGame():
    pyautogui.press('left')
    pyautogui.press('down')
    time.sleep(LONG)
    pyautogui.press('left')
    pyautogui.press('up')
    time.sleep(LONG)
    pyautogui.press('left')
    pyautogui.press('down')
    time.sleep(LONG)
    pyautogui.press('left')
    pyautogui.press('up')
    time.sleep(LONG)
    pyautogui.press('left')
    pyautogui.press('down')
    time.sleep(LONG)
    pyautogui.press('left')
    pyautogui.press('up')
    time.sleep(LONG)
    pyautogui.press('left')
    pyautogui.press('down')
    time.sleep(LONG)
    pyautogui.press('left')
    pyautogui.press('up')
    time.sleep(LONG)
    pyautogui.press('left')
    pyautogui.press('down')
    time.sleep(FULL1)
    pyautogui.press('right')
    time.sleep(FULL1)
    pyautogui.press('up')
    time.sleep(FULL2)
    fullGame()



if __name__ == "__main__":
    main()
