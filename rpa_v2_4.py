import  pyautogui
#스샷 찍기

# img = pyautogui.screenshot()
# img.save("screenshot.png")

# pyautogui.mouseInfo()
# 18,12 41,126,183 #297EB7

pixel = pyautogui.pixel(18, 12)
print(pixel)

# print(pyautogui.pixelMatchesColor(18, 12, (41, 126, 183)))
# print(pyautogui.pixelMatchesColor(18, 12, pixel))
print(pyautogui.pixelMatchesColor(18, 12, (41, 126, 184)))
