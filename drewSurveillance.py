import pygame
import KeyPressModule as kp
from time import sleep

kp.init()

tello = Tello()
tello.connect()
print(tello.get_battery())

def init():
    pygame.init()
    win = pygame.display.set_mode((400,400))

def getKey(keyName):
    ans = False

    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans
        
def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("w"): ud = speed
    elif kp.getKey("s"): ud = -speed

    if kp.getKey("a"): yv = -speed
    elif kp.getKey("d"): yv = speed

    if kp.getKey("q"): tello.land()
    if kp.getKey("e"): tello.takeoff()

    return [lr, fb, ud, yv]

if __name__ == '__main__':
    init()
    while True:
        vals = getKeyboardInput();
        tello.send_rc_control(vals[0], vals[1], vals[2], vals[3]);
        getKey();
        sleep(0.05)
