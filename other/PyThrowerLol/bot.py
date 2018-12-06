#!/usr/bin/python3

import math
import pyautogui
from xinput import operate_xinput_device, MODE_ENABLE, MODE_DISABLE
print("Hold your pokeball at the right bottom corner and press TAB to start.")
print("Then, press Space to when to shoot")
#import time

pyautogui.MINIMUM_DURATION = 0.000000
pyautogui.MINIMUM_SLEEP = 0.0001
pyautogui.PAUSE = 0.0
n_dots = 100
r = 30


def startHoldingPokeball():
    #operate_xinput_device(MODE_DISABLE, 'Logitech M510')
    pyautogui.mouseDown(duration=0.1)


def spinPokeball():
    x0, y0 = pyautogui.position()
    step = math.pi * 2 / n_dots
    angles = [n * step for n in range(n_dots)]
    coords = [(int(x0 + r * math.cos(t)), int(y0 + r * math.sin(t))) for t in angles]
    pyautogui.mouseDown(coords[0])
    print(pyautogui.position())
    print(coords[0])

    # for x in range(1, 5):
    #     for coord in coords:
    #         #print(coord)
    #         pyautogui.moveTo(x=coord[0], y=coord[1], duration=0.0001)

    for loop in range(1, 3):
        for n, coord in enumerate(coords):
            print(n, coord)
            if loop < 3:
                pyautogui.moveTo(x=coord[0], y=coord[1], duration=0.01)
            else:
                if n < 50:
                    pyautogui.moveTo(x=coord[0], y=coord[1], duration=0.01)
                else:
                    break



    pyautogui.MINIMUM_SLEEP = 0.001
    pyautogui.moveTo(293, 654, duration=0.1)
    pyautogui.MINIMUM_SLEEP = 0.0001
    #pyautogui.mouseUp()


def throwPokeball(startPosition):
    x0, y0 = (startPosition[0], startPosition[1])
    step = math.pi * 2 / n_dots
    angles = [n * step for n in range(n_dots)]
    coords = [(int(x0 + r * math.cos(t)), int(y0 + r * math.sin(t))) for t in angles]

    for x in range(1, 2):
        for coord in coords:
            #print(coord)
            pyautogui.moveTo(x=coord[0], y=coord[1])

    pyautogui.moveTo(293, 694, duration=0.002, tween=pyautogui.easeInExpo)
    #pyautogui.mouseUp()
    #operate_xinput_device(MODE_ENABLE, 'Logitech M510')


#startHoldingPokeball()
spinPokeball()
#throwPokeball(pyautogui.position())
