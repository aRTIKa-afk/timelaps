import cv2
import time
from picamera.array import PiRGBArray
from picamera import PiCamera
#в строках 1-4 мы пдключаем библиотеки
print("enter name of file")
name=int(input())
print("enter the period of observation (second)")
period=int(input())
print("enter the videoTime (second)")
videoTime=int(input())
#в строках 6-11 вводим переменные для настройки времени работы


camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 24
raw = PiRGBArray(camera)
time.sleep(0.1)
#в строках 15-19 подключаем камеру для RPi 


fourcc = cv2.VideoWriter_fourcc(*'XVID')
vid = cv2.VideoWriter(name+'.avi',fourcc, 24.0, (640,480))
#в строках 23-24 настраиваем видеовыход


if(period<videoTime):
    print("error! videoTime > period")
    exit()
#в строках 28-30 проверяем правильность введенных переменных


for i in range(videoTime*24):
    time.sleep(0.04*float(period)/float(videoTime)) #задержка между снятием кадров
    camera.capture(raw, format="bgr") #получаем данные с камеры
    frame = raw.array #преобразовываем данные в картинку
    print("frame #"+i+" was made successfully") #выводим номер снятого кадра для дебага
    vid.write(frame) #записываем кадр в видос
#в строках 34-39 основная часть



vid.release()
cam.release()
cv2.destroyAllWindows()
#заканчиваем работу приложухи