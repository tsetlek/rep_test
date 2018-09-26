from selenium import webdriver
import re
import os
import shutil
import time

web=webdriver.Chrome('C:/chromedriver/chromedriver.exe')

web.get('http://moodle.hku.hk/course/view.php?id=55854')

contents=web.find_elements_by_class_name('content')
print(len(contents))

chps=[]

for content in contents:
    name= content.text
    if re.search('Chapter \d+:\s',name) is not None:
        chps.append(content)
rootpath='C:/Users/Kelvin Cheung/Downloads'
chps=chps[:10]

for chp in chps:
    name=chp.find_element_by_class_name('sectionname').text
    links=chp.find_elements_by_class_name('activityinstance')
    for i,link in enumerate(links):
        link.click()
        'wait for 30 sec'
        time.sleep(30)
        filename = max([rootpath + "/" + f for f in os.listdir(rootpath)], key=os.path.getctime)
        newfilename="/".join(filename.split('/')[:-1]) + '/' + name.replace(':','') + ' - ' +str(i).zfill(2) + ' ' + filename.split('/')[-1]
        shutil.move(filename,newfilename)
        print(newfilename)



from bs4 import BeautifulSoup
import requests
from codecs import decode


google_url = 'https://www.dianping.com/hongkong/food/p'

names=[]
address=[]
features=[]
for i in range(10):
    r=requests.get(google_url + str(i+1))
    soup=BeautifulSoup(r.text,'html.parser')

    if r.status_code == requests.codes.ok:
        restaurants = soup.find_all('ul', class_='detail')

        for res in restaurants:
            names.append(res.find('a',class_='BL').text)
            address.append(re.search('[\u4e00-\u9fff:\d\w-]+',res.find('li',class_='address').text).group(0))


restaurants[0].find('a',class_='BL')['title']

a=restaurants[0].find('li',class_='address').text
a
re.search('[\u4e00-\u9fff:\d\w]+',a)


