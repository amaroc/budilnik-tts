# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from gtts import gTTS 
import webbrowser
import ntplib
from time import ctime
import urllib
from urllib import request
from bs4 import BeautifulSoup
import cssselect

class MP3_alarm:
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
                courses = []
                getdata = urllib.request.urlopen('http://www.3dnews.ru/')    
                dataread = getdata.read()
                soup = BeautifulSoup(dataread, "html.parser")   
                soup.prettify()    
                g_data = soup.find_all("li", {"class": "header"})    
                #print(g_data)                
                for news in g_data:
                    say = ()                    
                    new = news.cssselect('li')[1]
                    getnews = new.text
                    #print(getnews)
                    course = {'item': getnews}
                    print(course)                    
                    courses.append(course)
                tts = gTTS(text=course, lang='ru')
                tts.save("HelloWorld.mp3")
                webbrowser.open("C:\py-code\HelloWorld.mp3")
                flag = False

alarm = MP3_alarm(hour=10, minutes=58)
alarm.setAlarm()




def Checktime():
    c = ntplib.NTPClient()
    response = c.request('europe.pool.ntp.org', version=3)
    print(ctime(response.tx_time))
    print(ctime(response.orig_time))

Checktime();


#class MP3_alarm:
#    def __init__(self, hour, minutes):
#        self.hour = int(hour)
#        self.minutes = int(minutes)
#    def setAlarm(self):
#        import time
#        flag = True
#        while flag:
#            if self.hour ==list(time.localtime())[3:4][0] and \
#            self.minutes ==list(time.localtime())[4:5][0]:
#                print("TaramMAAMAMMAMAMAMma")
#                courses = []
#                getdata = urllib.request.urlopen('http://www.yellowpages.com/search?search_terms=bank&geo_location_terms=Los+Angeles%2C+CA')    
#                dataread = getdata.read()
#                soup = BeautifulSoup(dataread, "html.parser")   
#                soup.prettify()    
#                g_data = soup.find_all("div", {"class": "info"})    
#                for item in g_data:
#                    say = ()                    
#                    print(item.contents[0].text)
#                    course = {'item': item.contents[0].text}
#                    print(course)                    
#                    courses.append(course)
#                tts = gTTS(text=course, lang='ru')
#                tts.save("HelloWorld.mp3")
#                webbrowser.open("C:\py-code\HelloWorld.mp3")
#                flag = False