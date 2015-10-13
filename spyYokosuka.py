from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
import time
import datetime
import winsound
import smtplib
from email.mime.text import MIMEText
import logging

logging.basicConfig(
                    level    = logging.DEBUG,
                    format   = 'LINE %(lineno)-4d  %(levelname)-8s %(message)s',
                    datefmt  = '%m-%d %H:%M',
                    filename = "程序日志.log",
                    filemode = 'w')
# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter('LINE %(lineno)-4d : %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

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
        except NoSuchElementException as err1:
            #driver.get('http://area599.blogspot.hk/?view=classic')
            if i == 4:
                logging.warning(format(err1))
                openFlag = 0
        except WebDriverException as err2:
            if i == 4:
                logging.warning(format(err2))
                openFlag = 0
        except:
            openFlag = 0
            raise()
            break
            
            
    if openFlag == 0:
        logging.error("Can't open website!/n")
        driver.quit()
        
        #from email.mime.text import MIMEText
 
        msg = MIMEText("spy is down at " +datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        msg['Subject'] = u'Alert'
        msg['From'] = "3159933284@qq.com"
        msg['To'] = "312487299@qq.com"
        
        smtp = smtplib.SMTP()
        smtp.connect('smtp.qq.com')
        smtp.login("3159933284@qq.com", "r5383234")
        smtp.sendmail("3159933284@qq.com", "312487299@qq.com", msg.as_string())
        smtp.quit()

        errWavFile = r'c:\b.wav'
        #winsound.PlaySound(errWavFile,winsound.SND_NODEFAULT)
        winsound.PlaySound(errWavFile,winsound.SND_NODEFAULT|winsound.SND_LOOP|winsound.SND_ASYNC)
        input('请输入任意键后回车停止播放声音\n')
        winsound.PlaySound(None,0)
        
        exit()
    
    title = item.find_element_by_tag_name('h1').text

    if 'FAY' in title:
        publishInfo = driver.find_element_by_class_name('publish-info')
        timePublishedstr = publishInfo.find_element_by_tag_name('abbr').get_attribute('title')
        timePublishedCut = timePublishedstr[:10]+' '+timePublishedstr[11:19]
        timePublished = datetime.datetime.strptime(timePublishedCut,"%Y-%m-%d %H:%M:%S")
        if datetime.datetime.now()-timePublished < datetime.timedelta(hours = 8,minutes = 20):
            alertWavFile = r'c:\a.wav'
            winsound.PlaySound(alertWavFile,winsound.SND_NODEFAULT|winsound.SND_LOOP|winsound.SND_ASYNC)
            logging.info('at ')
            logging.info(datetime.datetime.now())
            logging.info(' found')
            input('请输入任意键后回车停止播放声音\n')
            winsound.PlaySound(None,0)
            time.sleep(60*60*8)
        else:
            logging.info(datetime.datetime.now())
            time.sleep(50)
    else:
        logging.info(datetime.datetime.now())
        time.sleep(50)

