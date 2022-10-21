import pyautogui

# pyautogui.FAILSAFE = False
pyautogui.PAUSE = 1 # 모든 동작에 sleep 1 적용
# pyautogui.mouseInfo()

for i in range(10):
    pyautogui.move(100, 100)
    # pyautogui.sleep(1)