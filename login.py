from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome()

service = Service(executable_path=r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe")
wd = webdriver.Chrome(service=service)
wd.get("http://kc.jxjypt.cn/classroom/start?scode=23124")



