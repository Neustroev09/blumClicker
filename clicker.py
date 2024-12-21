import random
import pyautogui


def choose_object(objects):
    stars = objects.get("star", [])
    diamonds = objects.get("diamond", [])
    #dog = objects.get("dog", [])

    random_number = random.randint(0, 100)

    chosen_object = {}
    # if dog:
    #     chosen_object = dog[-1]
    # elif diamonds:
    if diamonds:
        if random_number < 90:
            chosen_object = diamonds[-1]
    elif stars:
        chosen_object = stars[-1]
    return chosen_object


def click_object(object):
    if object:
        position = object['xyxy']
        x = (position[0] + position[2]) / 2 + random.randint(-10, 10)
        y = 65 + (position[1] + position[3]) / 2 + random.randint(-10, 10)
        count_click = random.randint(1, 2)
        interval_click = random.randint(0, 5) / 100
        pyautogui.click(x, y, clicks=count_click, interval=interval_click)


def clicker(objects):
    object = choose_object(objects)
    click_object(object)

