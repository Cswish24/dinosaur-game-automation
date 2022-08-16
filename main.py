import pyautogui
import PIL
import time

import numpy as np

time.sleep(3)
pyautogui.press('up')

while True:
    dino_loc = pyautogui.locateOnScreen('dino.png', region=(
        620, 450, 50, 50), grayscale=True)

    cacti_loc = pyautogui.locateOnScreen('cactipic.png', region=(
        642, 470, 350, 30), grayscale=True)

    cacti_loc2 = pyautogui.locateOnScreen('cactipic.png', region=(
        950, 470, 250, 30), grayscale=True)

    if cacti_loc and dino_loc and cacti_loc2:
        distance = cacti_loc[0] - dino_loc[0]
        distance2 = cacti_loc2[0] - cacti_loc[0]
        print(f"cacti_loc={cacti_loc}")
        print(f"cacti_loc2={cacti_loc2}")
        print(f"dino_loc={dino_loc}")
        print(distance)
        print(distance2)
        if distance2 < 355:
            if distance < 250:
                pyautogui.press('up')
        elif distance2 < 250:
            if distance < 350:
                pyautogui.press('up')
        elif distance < 180:
            pyautogui.press('up')

    elif cacti_loc and dino_loc:
        distance = cacti_loc[0] - dino_loc[0]
        print(f"cacti_loc={cacti_loc}")
        print(f"dino_loc={dino_loc}")
        print(distance)
        if distance < 180:
            pyautogui.press('up')
