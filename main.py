
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import os

class AutoPlayer():
    def __init__(self) -> None:
        self.desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        # 使用 Service 来指定驱动程序路径
        service = Service(executable_path=r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe")

        self.driver = webdriver.Chrome(service=service)
        self.id = ""
        self.pwd = ""
        self.url = "https://baidu.com"
    def get_user_info(self):
        with open(self.desktop + "\\uid.txt") as f:
             self.id = f.read()

        with open(self.desktop + "\\pwd.txt") as f:
             self.pwd = f.read()

    def work(self):
        self.driver.get(self.url)


if __name__ == "__main__":
    auto_play = AutoPlayer()
    auto_play.work()


