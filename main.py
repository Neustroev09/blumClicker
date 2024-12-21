import pyautogui
from pyautogui import ImageNotFoundException
from screenshotCreator import create_screenshot,  create_screenshot_for_dataset
from predict import ObjectDetector
from clicker import clicker

def test():
    print(pyautogui.position())

if __name__ == '__main__':
    detector = ObjectDetector()
    while (1):
        screen = create_screenshot()
        try:
            main_window = pyautogui.locate('game_images/main_window.png', screen, confidence=0.75)
            pyautogui.scroll(-300)
            pyautogui.moveTo(310, 457, 1.5)
            pyautogui.click()
            print("Начать новую игру")
        except ImageNotFoundException as exc:
            pass

        try:
            game_over = pyautogui.locate('game_images/game_over.png', screen, confidence=0.75)
            pyautogui.moveTo(180, 600, 1.5)
            pyautogui.click()
            print("Повторить игру")
        except ImageNotFoundException as exc:
            pass

        screen = create_screenshot()
        objects = detector.find_object(screen)
        clicker(objects)


