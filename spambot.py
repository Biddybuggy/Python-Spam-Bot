import time
import pyautogui
    
needed_time = int(input("How many seconds do you think you would need to prepare? "))

print(f"You got {needed_time} seconds to prepare...")
time.sleep(needed_time)
print("Spamming NOW")

f = open('insert path here')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press('enter')

