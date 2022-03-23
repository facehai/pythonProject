# coding=utf-8

from selenium import webdriver

import time
import threading

browser = webdriver.Chrome()
# 请求登陆页面
browser.get('https://passport.zhihuishu.com/login?service=http://online.zhihuishu.com/onlineSchool/')


# 登陆
def login(number, password):
    phone_number = browser.find_element_by_id('lUsername')  # 通过id定位，手机号码
    pwd = browser.find_element_by_id('lPassword')  # 密码
    login_btn = browser.find_element_by_class_name('wall-sub-btn')  # 登陆按钮

    phone_number.send_keys(number)  # 输入手机号码
    pwd.send_keys(password)  # 输入密码
    login_btn.click()  # 点击登陆按钮


# 转到播放视频页面
def to_course(key):
    time.sleep(5)
    current = browser.current_window_handle  # 当前页面的句柄
    key = browser.find_element_by_partial_link_text(key)  # 找到课程
    key.click()  # 跳转到播放视频页面
    time.sleep(1)  # 等待页面加载
    # 因为跳转到新的页面，所以browser要切换到新的页面操作
    handles = browser.window_handles
    for handle in handles:
        if handle != current:
            browser.switch_to.window(handle)

    time.sleep(10)
    try:
        video = browser.find_element_by_id('mediaplayer')  # 定位视频窗口
        video.click()  # 点击播放
    except:
        pass


# 判断是否有答题窗口弹出
def is_exist():
    while True:
        try:
            browser.switch_to.default_content()
            browser.switch_to.frame('tmDialog_iframe')  # 答题窗口在另一个frame里面，要切换
            box = browser.find_elements_by_class_name('answerOption')  # 答题列表
            radio = box[0].find_element_by_tag_name('input')  # 找到第一个选项
            radio.click()  # 选择
            browser.switch_to.default_content()
            browser.find_element_by_link_text('关闭').click()  # 关闭答题窗口
        except:
            browser.switch_to.parent_frame()  # 没有弹出，切换回本来的frame
        time.sleep(5)


# 判断当前视频是否结束
def is_end():
    while True:
        try:
            video = browser.find_element_by_id('mediaplayer')  # 定位视频窗口
            # 获取当前播放的进度
            current_time = video.find_element_by_class_name('currentTime').get_attribute('textContent')
            # 该视频的总时间
            total_time = video.find_element_by_class_name('duration').get_attribute('textContent')
            print(current_time, total_time)
            if current_time == total_time:
                # 当前视频播放结束，点击下一节
                js = "document.ElementById('nextBtn').click()"  # js脚本
                browser.execute_script(js)

            time.sleep(10)  # 10秒检测一次
        except:
            current_time = '00:00'
            total_time = '00:01'


if __name__ == '__main__':
    '''
    number=''#手机号码
    password=''#密码
    key=''#课程名称，可以部分名字

    '''
    login(number, password)
    to_course(key)
    # 开两个线程
    t1 = threading.Thread(target=is_exist)
    t2 = threading.Thread(target=is_end)
    t2.start()
    time.sleep(3)
    t1.start()
    t2.join()
    t1.join()