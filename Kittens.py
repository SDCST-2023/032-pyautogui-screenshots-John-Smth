#!python3
import pyautogui
import time
import pyperclip
pyautogui.PAUSE =.00001
numclicks = 5000
Woodclicks = 5

time.sleep(2)

print('looking for icon on whole screen')


start = time.time()
x = pyautogui.locateCenterOnScreen('GaNIP.png')
if x != None:
    for i in range(numclicks):
        pyautogui.click(x)

pyautogui.click(699,221)

time.sleep(.5)

y = pyautogui.locateCenterOnScreen('ReX100NIP.png',confidence=0.95)
print(y)
if y != None:
    for i in range(Woodclicks):
        pyautogui.click(961,221)

pyautogui.click(699,221)

time.sleep(.5)

z = pyautogui.locateCenterOnScreen('ObservetheskyNIP',confidence=0.95)
print(z)
if z != None:
    for i in range(1):
        pyautogui.click(z)

pyautogui.click(699,221)

time.sleep(.5)

S = pyautogui.locateCenterOnScreen('SendHunterNIP.png',confidence=0.95)
print(S)
if S != None:
    for i in range(1):
        pyautogui.click(S)


