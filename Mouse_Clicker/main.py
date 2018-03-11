import pyautogui as p
from time import sleep


def main():
    sleep(4)
    pos = (1122, 747)
    p.moveTo(pos)
    for i in range(1, 885):
        if i % 100 == 0:
            p.keyDown('ctrl')
            p.keyDown('r')
            p.keyUp('r')
            p.keyUp('ctrl')
            sleep(2)
            p.moveTo(pos)
        sleep(0.3)
        p.click()
        p.scroll(-1)
        p.moveRel(0, +1)


if __name__ == '__main__':
    main()
