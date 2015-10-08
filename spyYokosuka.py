from selenium import webdriver
import time
import winsound

driver = webdriver.Chrome()   #打开chrome浏览器
driver.implicitly_wait(10)

while True:
    driver.get('http://area599.blogspot.hk/?view=classic')   #chrome浏览器转至
    time.sleep(20)

    item = driver.find_element_by_class_name('article-header')
    title = item.find_element_by_tag_name('h1').text

    if 'FAY' in title:
        #publishInfo = item.find_element_by_class_name('publish-info')
        #timePublished = publishInfo.find_element_by_tag_name('abbr').get_attribute('title')
        alertWavFile = r'c:\a.wav'
        winsound.PlaySound(alertWavFile,winsound.SND_NODEFAULT)
        time.sleep(60*60*5)
    else:
        time.sleep(50)
