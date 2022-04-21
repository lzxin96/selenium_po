#encoding=utf-8
from selenium import webdriver
from time import sleep
from time import ctime
def start_chrome():
    print('starting chrome browser now! %s'%ctime())
    chrome_driver = webdriver.Chrome()
    chrome_driver.get('http://www.baidu.com')
    sleep(2)
    chrome_driver.quit()

def start_firefox():
    print('starting firefox browser now! %s'%ctime())
    fire_driver = webdriver.Firefox()
    fire_driver.get('http://www.baidu.com')
    sleep(2)
    fire_driver.quit()


if __name__ == '__main__':
    start_chrome()
    start_firefox()
    print(u'全部结束%s'%ctime())