import pyautogui
import time

choice = int(input("1. Rickroll \n2. Jebait \n3. Shipping \nYour input: "))
if choice == 1:
    print("\n")
    counter = 5
    for u in range(5):
        print(counter)
        counter -= 1
        time.sleep(1)
    print("\nSpamming now!")
    f = open("insert a path to a file with the rickroll lyrics", 'r')
    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
    print("I'm done spamming!")

elif choice == 2:
    print("\n")
    counter = 5
    for u in range(counter):
        print(counter)
        counter -= 1
        time.sleep(1)
    print("\nSpamming now!")
    f = open("insert a path to a file with the jebaited lyrics", 'r')
    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
    print("I'm done spamming!")

elif choice == 3:
    print("\n")
    counter = 5
    for u in range(5):
        print(counter)
        counter -= 1
        time.sleep(1)
    print("\nSpamming now!")
    for u in range(10):
        pyautogui.typewrite("(insert name) likes (insert another name)")
        pyautogui.press("enter")
    print("I'm done spamming!")

else:
    print("\nInvalid input.")
