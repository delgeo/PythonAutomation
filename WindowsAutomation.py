import pyautogui # capturing the mouse movements
from win32api import GetSystemMetrics
import os
import time

print ("SalesMate + Backup Manu Test")
print ("Create a Database Backup directory called SMP")
path="G:/SMP"
if not os.path.exists(path):
    os. makedirs (path)

#get the width and height of the monitor
width= GetSystemMetrics(0)
height=GetSystemMetrics(1)

#click on the botton left to launch the start menu
print ("click on the botton left to launch the start menu")
pyautogui.hotkey('win')

print ("Select the SalesMate + Application")
pyautogui. typewrite("SalesMate +")
print ("Press Enter Key to Launch SalesMate + Application and wait for 10 Sec")
pyautogui.press("enter",1,10)

#Sometimes SalesMate + might take 10 seconds to load it . So 10 sec delay
print ("Press Enter Key again to close the Tip of the Day Dialog")
pyautogui. press ("enter")

print ("Now alt and f shortcut key in Salesmate + to invoke the File Root menu")
pyautogui.press(['alt', 'f'])
print ("Now press 'b' to invoke the Bacuup Folder Dialog")
pyautogui.press("b")

print ("Go to D Drive")
pyautogui.press("d",1,1)
print ("Now press Right arrow Key to Expand the Tree")
pyautogui.press("right",1,1)
print ("Go to SMP Folder")
pyautogui.typewrite("smp")

print ("Press Enter Key to Backuup Data")
pyautogui.press("enter",1,2)
print("press Enter Again to close the OK Button")
pyautogui.press("enter")


print ("Now alt and e shortcut key in Salesmate + to invoke the Setup Root menu")
pyautogui.press(['alt', 'e'])
print ("Now press 'down' to invoke the 'Service Master'")
for _ in range(3):
        pyautogui.press('down')
        time.sleep(0.5)
print("press Enter")
pyautogui.press("enter")

print("Press 'Tab' to get 'New' item")
pyautogui.press('tab')
pyautogui.press("enter",1,2)

print("Press 'Tab' to get 'New' item")
pyautogui.press('tab')

print("Adding new item details")
pyautogui.typewrite("Team Meeting cards")
pyautogui.press('tab')
pyautogui.typewrite("50 cards")
pyautogui.press('tab')
pyautogui.typewrite("5.00")
pyautogui.press('tab')
pyautogui.typewrite("0.15")

print("Press Enter to save the added item")
pyautogui.press('tab')
pyautogui.press("enter",1,2)

print("Press OK to the dialog box")
pyautogui.press("enter",1,2)

print("Press Esc to close 'Service Master'")
pyautogui.press('esc',1,2)

print("Close Salesmate +")
pyautogui.hotkey('alt', 'f4')
