# -*- coding: utf-8 -*-
"""
Change log:
v0.1.1
    1. Добавлен интерфейс.
    2. Галка для 3Dnews - не работает. 
        Это заготовка на будущее, где 
        можно будет выбирать ресурсы для парсинга.
        
    3. Изменен путь к mp3-файлу с абсолютного
       на относительный (создается в корне с .py файлом)
   
TO-DO:
v0.1.2
    1. Выбор имени владельца будильника.
    2. Запуск из exe файла.
v0.2.0    
    1. Выбор ресурсов для Parsing`a.
v0.3.0
    1. Очистить текст от мусора, типа "апастроф, открывающаяся фигурная скобка"
    2. Разобраться как сделать так что бы русский диктор нормально читал английский текст.

"""

import sys
import PyQt4
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.uic import *

import urllib
from urllib import request
from bs4 import BeautifulSoup
from gtts import gTTS 
import webbrowser
import ntplib
from time import ctime
import urllib
from urllib import request
from bs4 import BeautifulSoup
import cssselect
import datetime

app = QApplication(sys.argv)
w = loadUi("ibud.ui")

"""
VERSION 2 TEST
"""

class MP3_alarm:
    print("MP3_alarm class says: Time is seting to ")# + hour + " " + minutes)
    def __init__(self, hour, minutes):
        self.hour = int(hour)
        self.minutes = int(minutes)
    def setAlarm(self):
        import time
        flag = True
        while flag:
            if self.hour ==list(time.localtime())[3:4][0] and \
            self.minutes ==list(time.localtime())[4:5][0]:
                print("TaramMAAMAMMAMAMAMma")
                # урл для парсинга
                #getdata = urllib.request.urlopen('http://www.yellowpages.com/search?search_terms=bank&geo_location_terms=Los+Angeles%2C+CA')
                getdata = urllib.request.urlopen('http://www.3dnews.ru/software-news/rss')
                
                #читаем дату
                dataread = getdata.read()
                soup = BeautifulSoup(dataread, "html.parser")
                #украшаем гавно
                soup.prettify()
                #search = soup.find_all('a')
                #for link in search:
                    #print(link.get("href"))
                    #print(link.text)
                    #print(link.text , link.get("href"))
                g_data = soup.find_all("item", {"title": ""})
                
                courses = []
                for item in g_data:
                    try:    
                        print(item.contents[1].text)
                        # добавить добавление в словарь                
                        course = {item.contents[1].text.replace("\n" , "").replace("\xa0" , "").replace("..:..", "").split(",")[0]}
                        print(course)                    
                        courses.append(course)
                    except IndexError:
                        print("Index Fucking Error")      
                
                
                
                minutes =str(time.strftime('%M', time.localtime()))
                now_date = datetime.date.today()
                cur_month = now_date.month # Месяц текущий
                cur_day = now_date.day # День текущий
                
                
                month_names = [
                    u'Января',
                    u'Февраля',
                    u'Марта',
                    u'Апреля',
                    u'Мая',
                    u'Июня',
                    u'Июля',
                    u'Августа',
                    u'Сентября',
                    u'Октября',
                    u'Ноября',
                    u'Декабря',    
                ]
                
                month = datetime.date.today().month
                
                        
                timenow = ("Сегодня "+ str(cur_day) + " " + month_names[month - 1] + " , "  + str(hour) + " часов " + str(minutes) + " минут")
                print(timenow)
                
                privet = str("Доброе утро Станислав!"+ timenow + " Последние новости от сайта ТриДэНьуз:")
                myString = [privet, courses]
                
                tts = gTTS(text=str(myString), lang='ru')
                tts.save("HelloWorld.mp3")
                webbrowser.open("HelloWorld.mp3")
                flag = False

#alarm = MP3_alarm(hour=8, minutes=1)
#alarm.setAlarm()
#global hour
#global minutes

def setTime():
   # print(self.hbox.value() + " " + w.self.mbox.value())
    print("Что то произошло...")
    global hour 
    hour = w.hbox.value()
    global minutes
    minutes = w.mbox.value()
    alarm = MP3_alarm(hour, minutes)
#    print("Time is seting to " + hour + " " + minutes)
    alarm.setAlarm()

w.connect(w.setTimeButton, SIGNAL("clicked()"), setTime)


def Checktime():
    c = ntplib.NTPClient()
    response = c.request('europe.pool.ntp.org', version=3)
    print(ctime(response.tx_time))
    print(ctime(response.orig_time))

Checktime();

print(w.hbox.value())
print( w.mbox.value())
w.show()
sys.exit(app.exec_()) 

    
    

