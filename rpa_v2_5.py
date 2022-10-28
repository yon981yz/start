from cProfile import run
from sqlite3 import Timestamp, TimestampFromTicks
import pyautogui

# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)
# pyautogui.click(file_menu)

# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)

# screen = pyautogui.locateOnScreen("screenshot.png")
# print(screen)

# for i in pyautogui.locateAllOnScreen("checkbox.png"):
#     print(i)
#     pyautogui.click(i, duration=0)

# for i in pyautogui.locateAllOnScreen("checkedbox.png"):
#     print(i)
#     pyautogui.click(i, duration=0)

# checkbox = pyautogui.locateOnScreen("checkbox.png")
# pyautogui.click(checkbox)

# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)

# 속도 개선
# 1. Grayscale

# trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True)
# pyautogui.moveTo(trash_icon)

# 2. 범위 지정

# trash_icon = pyautogui.locateOnScreen("trash_icon.png", region=(1702, 632, 207, 83))
# pyautogui.moveTo(trash_icon)

# pyautogui.mouseInfo()
# 1854,704 185,185,185 #B9B9B9
# 1690,632
# 1909,751

# 3. 정확도 조정
# run_btn = pyautogui.locateOnScreen("play_icon.png", confidence=0.9) #90%
# pyautogui.moveTo(run_btn)

# 자동화 대상이 바로 보여지지 않는 경우 

# file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# if file_menu_notepad:
#     pyautogui.click(file_menu_notepad)
# else:
#     print("발견 실패")
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     print("발견 실패")

# pyautogui.click(file_menu_notepad)

# 2. 일정 시간동안 기다리기 (TimeOut)
import time
import sys


timeout = 10
# start = time.time()
# file_menu_notepad = None 
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     end =  time.time()
#     if end - start > timeout:
#         print("시간 종료")
#         sys.exit()

def find_target(img_file, timeout=30):
    start = time.time()
    target = None 
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target

def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print("f[Timeout {timeout}s] Target not found ({img_file}). Terminate program")
        sys.exit()

# pyautogui.click(file_menu_notepad)

my_click("file_menu_notepad.png", 10)
