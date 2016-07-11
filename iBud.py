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


# урл для парсинга
#getdata = urllib.request.urlopen('http://www.yellowpages.com/search?search_terms=bank&geo_location_terms=Los+Angeles%2C+CA')
getdata = urllib.request.urlopen('http://www.3dnews.ru/software-news')

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
g_data = soup.find_all("div", {"class": "content-block-data white"})

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
myString = courses

tts = gTTS(text=str(myString), lang='ru')
tts.save("HelloWorld.mp3")
webbrowser.open("C:\py-code\HelloWorld.mp3")
flag = False
    
    
    
