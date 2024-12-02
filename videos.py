from selenium import webdriver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# 初始化Selenium的Chrome驱动
service = Service(executable_path=r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe")
wd = webdriver.Chrome(service=service)

# 打开视频页面
wd.get("https://www.imooc.com/learn/1439")

wd.find_element("id","js-signin-btn").click()
time.sleep(3)
wd.find_element("xpath",'//*[@id="signup-form"]/div[1]/input').send_keys("18538716285")
wd.find_element("xpath",'//*[@id="signup-form"]/div[2]/input').send_keys("Qinhao.00")
wd.find_element("xpath",'//*[@id="signup-form"]/div[5]/input').click()
time.sleep(2)


# 获取视频总数
video_elements = wd.find_elements("class name","J-media-item")
video_elements[0].click()
time.sleep(5)
js = "return document.getElementById('video-box-mocoplayer-hls-video_html5_api').duration"
wait_time = wd.execute_script(js)
print("视频总时长：", wait_time)
time.sleep(wait_time+5)
wd.find_element("xpath",'/html/body/div[8]/a').click()
time.sleep(2)

video_elements2 = wd.find_elements("class name","sec-li")
print("python视频个数：", len(video_elements2))
for i in range(len(video_elements2)):
    video_elements3 = wd.find_elements("class name", "sec-li")
    time.sleep(2)
    wd.find_element("xpath",'//*[@id="courseSidebar"]/dl/dd[1]/i').click()
    time.sleep(3)
    s = i+1
    print("第", s, "个视频")
    video_elements3[i].click()
    time.sleep(5)
    js = "return document.getElementById('video-box-mocoplayer-hls-video_html5_api').duration"
    wait_time = wd.execute_script(js)
    time.sleep(wait_time)


# for i in range(len(video_elements)):
#     print("第", i, "个视频")
#     video_elements[i].click()
#     js = "return document.getElementById('video-box-mocoplayer-hls-video_html5_api').duration"
#     wait_time = wd.execute_script(js)
#     print("视频总时长：", wait_time)
#     time.sleep(wait_time)
#     wd.back()








