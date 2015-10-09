from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
import time
import datetime
import winsound
import smtplib
from email.mime.text import MIMEText

driver = webdriver.Chrome()   #打开chrome浏览器
driver.implicitly_wait(20)

while True:
    openFlag = 1
    for i in range(5):
        try:
            driver.get('http://area599.blogspot.hk/?view=classic')   #chrome浏览器转至
            item = driver.find_element_by_class_name('article-header')
            openFlag = 1
            break
        except NoSuchElementException:
            #driver.get('http://area599.blogspot.hk/?view=classic')
            openFlag = 0
        except WebDriverException:
            openFlag = 0
        except:
            openFlag = 0
            break;
            
            
    if openFlag == 0:
        print("Can't open website!/n")
        driver.quit()
        
        #from email.mime.text import MIMEText
 
        msg = MIMEText("spy is down")
        msg['Subject'] = u'Alert'
        msg['From'] = "312487299@qq.com"
        msg['To'] = "zhangtao3601@gmail.com"
        
        smtp = smtplib.SMTP()
        smtp.connect('smtp.qq.com')
        smtp.login("312487299@qq.com", "tyxy13Z")
        smtp.sendmail("312487299@qq.com", "zhangtao3601@gmail.com", msg.as_string())
        smtp.quit()

        driver.close()
        exit()
    
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
