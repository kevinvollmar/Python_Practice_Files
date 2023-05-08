import pyautogui
import time

# Give python file time before continuing
time.sleep(3)

'''
# Print resolution of the screen using PyAutoGUI
print(pyautogui.size())

# Print the current position of mouse using PyAutoGUI
print(pyautogui.position())

# Move the mouse over time (moves to position 100, 100 on screen over period of 2 seconds)
pyautogui.moveTo(100, 100, 2)

# Move the mouse relative to current positions (moves 100 x 100 pixels away from current position over 2 seconds)
pyautogui.moveRel(100, 100, 2)

# Perform a click with PyAutoGUI (left click at position 100, 100 one time after moving there over span of 2 seconds)
pyautogui.click(100, 100, 1, 2, button='left')

# Scrolls down 500 pixels using PyAutoGUI
pyautogui.scroll(-500)
'''

# Create a spiral box in MS Paint using PyA
# Remember to open MS Paint before running this code

distance = 300

while distance > 0:
    pyautogui.dragRel(distance, 0, 1, button='left')
    distance = distance - 20
    pyautogui.dragRel(0, distance, 1, button='left')
    pyautogui.dragRel(-distance, 0, 1, button='left')
    distance = distance - 20
    pyautogui.dragRel(0, -distance, 1, button='left')
    time.sleep(2)
