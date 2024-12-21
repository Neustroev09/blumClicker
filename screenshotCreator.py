import pyautogui
import time

def create_screenshot():
    screen = pyautogui.screenshot('screenshot.png', region=(0, 65, 380, 590))
    return screen

def create_screenshot_for_dataset():
    counter = 110
    while (1):
        screenshot_name = f"screenshot_{counter}.png"
        screen = pyautogui.screenshot(screenshot_name, region=(0, 65, 380, 590))
        print(f"Сделан скриншот {screenshot_name}")
        counter += 1
        time.sleep(2)

