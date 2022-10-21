from cProfile import run
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
run_btn = pyautogui.locateOnScreen("play_icon.png", confidence=0.9) #90%
pyautogui.moveTo(run_btn)

# 자동화 대상이 바로 보여지지 않는 경우 
