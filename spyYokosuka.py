from selenium import webdriver
import time
import datetime
import winsound

driver = webdriver.Chrome()   #打开chrome浏览器
driver.implicitly_wait(10)

while True:
    driver.get('http://area599.blogspot.hk/?view=classic')   #chrome浏览器转至
    time.sleep(20)

    item = driver.find_element_by_class_name('article-header')
    title = item.find_element_by_tag_name('h1').text

    if 'FAY' in title:
        publishInfo = driver.find_element_by_class_name('publish-info')
        timePublishedstr = publishInfo.find_element_by_tag_name('abbr').get_attribute('title')
        timePublishedCut = timePublishedstr[:10]+' '+timePublishedstr[11:19]
        timePublished = datetime.datetime.strptime(timePublishedCut,"%Y-%m-%d %H:%M:%S")
        if datetime.datetime.now()-timePublished < datetime.timedelta(hours = 8,minutes = 20):
            alertWavFile = r'c:\a.wav'
            winsound.PlaySound(alertWavFile,winsound.SND_NODEFAULT)
            print('at ')
            print(datetime.datetime.now())
            print(' found');
            time.sleep(60*60*5)
        else:
            print(datetime.datetime.now())
            time.sleep(50)
    else:
        print(datetime.datetime.now())
        time.sleep(50)

