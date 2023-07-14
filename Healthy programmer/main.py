from pygame import mixer
from datetime import datetime
from time import time

def musicPLay(file , stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break


def logMsg(msg):
    with open("python\projects\Healthy programmer\log.txt" , "a") as f:
        f.write(f"{msg} {datetime.now()} \n")

if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    water_limit = 5
    eyes_limit = 10
    exercise_limit = 20
    
    # a = time() - init_water
    # print(a)
    
    while True:
        if time() - init_water > water_limit:
            print("Water Drinking time. Enter 'drank' to stop the alarm")
            musicPLay("python\projects\Healthy programmer\water.mp3", "drank")
            init_water = time()
            logMsg("Drank water at :")

        if time() - init_eyes > eyes_limit:
            print("Eyes Exercise time. Enter 'done' to stop the alarm")
            musicPLay("python\projects\Healthy programmer\eyes.mp3", "done")
            init_eyes = time()
            logMsg("Eyes relaxed at :")
            
        if time() - init_exercise > exercise_limit:
            print("Physical Activity time. Enter 'complete' to stop the alarm")
            musicPLay("python\projects\Healthy programmer\exer.mp3", "complete")
            init_exercise = time()
            logMsg("Physical movement at :")

        
