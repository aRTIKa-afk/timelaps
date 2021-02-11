import cv2
import time
#в строках 1-2 мы пдключаем библиотеки


print("enter name of file")
name=input()
print("enter the period of observation (second)")
period=int(input())
print("enter the videoTime (second)")
videoTime=int(input())
#в строках 6-11 вводим переменные для настройки времени работы


fourcc = cv2.VideoWriter_fourcc(*'XVID')
vid = cv2.VideoWriter(name+'.avi',fourcc, 24.0, (640,480))
#в строках 15-16 настраиваем видеовыход


if(period<videoTime):
    print("error! videoTime > period")
    exit()
#в строках 20-22 проверяем правильность введенных переменных


cam = cv2.VideoCapture(0)
#в строках 15-19 подключаем камеру для приложухи 


for i in range(videoTime*24):
    time.sleep(0.038*float(period)/float(videoTime)) #задержка между снятием кадров
    ret, frame = cam.read() #получаем данные с камеры
    print("frame #"+str(i)+" was made successfully") #выводим номер снятого кадра для дебага
    vid.write(frame)#записываем кадр в видос
#в строках 30-34 основная часть


vid.release()
cam.release()
#заканчиваем работу приложухи