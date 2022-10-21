import pyautogui
# pyautogui.sleep(3) # 3초 대기
# print(pyautogui.position())

# pyautogui.click(63,12, duration=1) # 1초동안 (64, 17) 좌표로 이동후 클릭

# pyautogui.click()
# pyautogui.mouseDown()
# pyautogui.mouseUp

# pyautogui.doubleClick()
# pyautogui.click(clicks=500)

# pyautogui.moveTo(200,200)
# pyautogui.mouseDown()
# pyautogui.moveTo(300,300)
# pyautogui.mouseUp()

pyautogui.sleep(3)
# pyautogui.rightClick()
# pyautogui.middleClick()

# print(pyautogui.position())
# pyautogui.moveTo(819, 470)
# pyautogui.drag(100, 0) #현재 위치기준으로 x 100 만큼 y 0 만큼 드래그
# pyautogui.drag(100, 0, duration=1)
# pyautogui.drag(-100, 0, duration=1)
# pyautogui.dragTo(1319,470, duration=0.25)# 절때 좌표 기준 드래그

pyautogui.scroll(-800) #위반향으로 300 스크롤 밑은 -300
