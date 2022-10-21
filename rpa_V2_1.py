# import pyautogui

# size = pyautogui.size()
# print(size)

# #size[0] : width
# #size[1] : height

###############################################################################################

#마우스 자동화
import pyautogui

# 가로 x 세로 y
# pyautogui.moveTo(100,100)

# pyautogui.moveTo(100,200, duration=5) #5초동안 머문다 

# pyautogui.moveTo(100, 100,duration=0.25)
# pyautogui.moveTo(200, 200,duration=0.25)
# pyautogui.moveTo(300, 300,duration=0.25)

#상대 좌표로 마우스 이동 (현재 커서가 있는 위치로부터)
pyautogui.moveTo(100, 100,duration=0.25)
print(pyautogui.position())
pyautogui.move(100, 100,duration=0.25) #100, 100기준으로 +100, +100 -> 200, 200
print(pyautogui.position())
pyautogui.move(100, 100,duration=0.25) #200, 200기준으로 +100, +100 -> 300, 300
print(pyautogui.position())

p = pyautogui.position()
print(p[0], p[1])
print(p.x, p.y)
