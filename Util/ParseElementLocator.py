#-*- coding: utf-8 -*-
from configparser import ConfigParser
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait


class ParseConfigFile:
    def __init__(self, driver, page_element_locator):
        self.driver = driver
        self.cf = ConfigParser()
        self.cf.read(page_element_locator, encoding='utf-8')

    def get_items_section(self, section_name):
        options_dict = dict(self.cf.items(section_name))
        return options_dict

    def get_option_value(self, section_name, option_name):
        value = self.cf.get(section_name, option_name)
        return value

    def get_element_location(self, section_name, option_name, timeout):
        driver = self.driver
        location = self.get_option_value(section_name, option_name)
        location_type = location.split('>')[0]
        location_value = location.split('>')[1]
        print('读取到的定位类型为：' + location_type + '\t读取到的定位信息为：' + location_value)
        try:
            element = WebDriverWait(driver, timeout)\
                .until(lambda x: x.find_element(by=location_type, value=location_value))
            return element
        except Exception as e:
            print('定位元素超过' + str(timeout) + '秒，详情异常信息如下：')
            raise e

    def highlight_element(self, driver, element):
        driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",element,"background:yellow;border:2px solid red;")