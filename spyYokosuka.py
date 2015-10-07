from seliunums import webdriver
import time
import datetime
import winsound

url = "http://book.douban.com/review/1003727/" #需更改为实际网站
driver = webdriver.Chrome()

while True
  driver.get(url)
  driver.find_element
  timePublishedstr = soup.                    #读取特定文本内容
  
  timePublished = datetime.datetime.strptime(timePublishedstr,"%Y-%m-%d-%H:%M:%S")  #转化为时间
  if(datetime.datetime.now()-timePublished < datetime.timedelta(minutes = 5)):  #如果发布时间与当前时间相差小于5分钟，那么播放
    sound = r'c:\Python34\My program\a.wav'                                     #提醒声音，并暂停10个小时。
    winsound.PlaySound(sound,winsound.SND_NODEFAULT)
    sleep(60*60*10)
  else:                                                                         #如果大于5分钟，那么说明帖子时间较旧，暂停100秒
    sleep(100)                                                                  #后再次查找。
