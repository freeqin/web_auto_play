import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import ddddocr
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException
from selenium.webdriver.common.by import By

service = Service(executable_path=r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe")
wd = webdriver.Chrome(service=service)

def click_element(xpath):
    """尝试点击指定的元素并捕获异常"""
    try:
        wd.find_element(By.XPATH, xpath).click()
    except NoSuchElementException as e:
        print("找不到元素:", e)
    except Exception as e:
        print("点击元素时出现错误:", e)

def send_keys_to_element(element_id, keys):
    """尝试向指定的元素发送输入，并捕获异常"""
    try:
        wd.find_element(By.ID, element_id).send_keys(keys)
    except NoSuchElementException as e:
        print("找不到元素:", e)
    except Exception as e:
        print("发送输入时出现错误:", e)

def wait_for_element(xpath, timeout=10):
    """等待元素加载"""
    for _ in range(timeout):
        try:
            element = wd.find_element(By.XPATH, xpath)
            return element
        except NoSuchElementException:
            time.sleep(1)
    print("元素未找到，超出时间限制:", xpath)
    return None

try:
    wd.get("https://hnjswlxy.cn/")

    # 点击登录按钮
    click_element("//*[@id='root']/header/div[3]/div[2]/button")
    time.sleep(1)

    # 输入用户名和密码
    send_keys_to_element("loginForm_username", "")
    send_keys_to_element("loginForm_password", "")
    time.sleep(3)

    # 点击验证码按钮
    click_element('//*[@id="loginForm"]/div[3]/div/div/div/span/span/span/button')
    time.sleep(10)

    # 获取验证码
    captcha_img_element = wait_for_element('//*[@id="loginForm"]/div[3]/div/div/div/span/span/span/div/img')
    if captcha_img_element:
        captcha_img_data = captcha_img_element.screenshot_as_png

        # 识别验证码
        ocr = ddddocr.DdddOcr()
        captcha_text = ocr.classification(captcha_img_data)
        send_keys_to_element("loginForm_code", captcha_text)
        time.sleep(1)

        # 点击登录按钮
        click_element('//*[@id="loginForm"]/div[5]/div/div/div/button')

        # 等待页面加载完成
        time.sleep(10)

        # 等待手机验证码
        input("等待手机验证码")

        # 点击个人中心
        click_element('//*[@id="root"]/header/div/div[2]/div/ul/li[7]/a')
        time.sleep(2)

        # 点击学历提升
        click_element('//*[@id="root"]/div[3]/div[3]/div/div[2]/div[1]/div[3]/a')
        time.sleep(2)

        # 点击学习
        studys = wd.find_elements(By.CLASS_NAME, 'ant-btn ant-btn-link')
        if len(studys) > 1:
            studys[1].click()
            time.sleep(2)

            # 弹窗知道了
            click_element('/html/body/div[3]/div/div[2]/div/div[2]/div/div/div[2]/button')
            time.sleep(2)

            # 获取所有视频
            videos = wd.find_elements(By.CLASS_NAME, "fa z-m-right fa-check-circle z-icon-red")
            for video in videos:
                video.click()
                time.sleep(2)
                # 点击播放按钮并获取视频长度
                try:
                    wd.find_element(By.ID, "videoPlayer_component_B8EDA07F-C0DE-4CC7-A06E-1CA1FC196BA3").click()
                    js = "return document.querySelector('video').duration"
                    wait_time = wd.execute_script(js)
                    time.sleep(wait_time + 50)
                except Exception as e:
                    print("处理视频播放时出现错误:", e)

except WebDriverException as e:
    print("WebDriver出现错误:", e)

except Exception as e:
    print("发生了一个意外错误:", e)

finally:
    wd.quit()  # 确保在结束时关闭webdriver

