import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import ddddocr
from selenium.common.exceptions import NoSuchElementException, WebDriverException

service = Service(executable_path=r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe")
wd = webdriver.Chrome(service=service)

def click_element(xpath):
    """尝试点击指定的元素并捕获异常"""
    try:
        wd.find_element("xpath", xpath).click()
    except NoSuchElementException as e:
        print("找不到元素:", e)

def send_keys_to_element(element_id, keys):
    """尝试向指定的元素发送输入，并捕获异常"""
    try:
        wd.find_element("id", element_id).send_keys(keys)
    except NoSuchElementException as e:
        print("找不到元素:", e)

try:
    wd.get("https://hnjswlxy.cn/")

    # 点击登录按钮
    click_element("//*[@id='root']/header/div[3]/div[2]/button")
    time.sleep(1)

    # 输入用户名和密码
    send_keys_to_element("loginForm_username", "410325199111103063")
    send_keys_to_element("loginForm_password", "Lipeifei.123")
    time.sleep(3)

    # 点击验证码按钮
    click_element('//*[@id="loginForm"]/div[3]/div/div/div/span/span/span/button')
    time.sleep(10)

    # 获取验证码
    captcha_img_element = wd.find_element("xpath", '//*[@id="loginForm"]/div[3]/div/div/div/span/span/span/div/img')
    captcha_img_data = captcha_img_element.screenshot_as_png


    # 识别验证码
    ocr = ddddocr.DdddOcr()
    captcha_text = ocr.classification(captcha_img_data)
    # 输入验证码
    send_keys_to_element("loginForm_code", captcha_text)
    time.sleep(1)


    # 点击登录按钮
    click_element('//*[@id="loginForm"]/div[5]/div/div/div/button')

    # 等待页面加载完成
    time.sleep(10)

    #等待手机验证码
    input("等待手机验证码")

    #点击个人中心
    click_element('//*[@id="root"]/header/div/div[2]/div/ul/li[7]/a')
    time.sleep(2)

    #点击学历提升
    click_element('//*[@id="root"]/div[3]/div[3]/div/div[2]/div[1]/div[3]/a')
    time.sleep(2)

    #点击学习
    studys = wd.find_elements('class name','ant-btn ant-btn-link')
    studys[1].click()
    time.sleep(2)

    #弹窗知道了
    click_element('/html/body/div[3]/div/div[2]/div/div[2]/div/div/div[2]/button')
    time.sleep(2)

    #获取所有视频
    videos = wd.find_elements("class name","fa z-m-right fa-check-circle z-icon-red")
    for i in range(len(videos)):
        videos[i].click()
        time.sleep(2)
        # 点击播放按钮
        wd.find_element("id", "videoPlayer_component_B8EDA07F-C0DE-4CC7-A06E-1CA1FC196BA3").click()
        # 获取视频长度
        js = "return document.querySelector('video').duration"
        wait_time = wd.execute_script(js)
        # 时间少50秒需要加上
        time.sleep(wait_time+50)


except WebDriverException as e:
    print("WebDriver出现错误:", e)
finally:
    wd.quit()  # 确保在结束时关闭webdriver
