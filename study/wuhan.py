# coding=utf-8

"""
使用Requests库完成Post表单操作
"""
import requests
import time

cookie = "sspm_proctorUrl=http://wljy.whut.edu.cn:80/; sspm_orgid=4406; sspm_appid=157438568781088; JSESSIONID=83B4062BFAC796348CD98283844F2BDF"
headers = {
    "Cookie": cookie,
    "Referer": "http://wljy.whut.edu.cn/web/kpointdetail.htm?kpointNo=150932&courlibNo=1774&courseNo=1663",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}

# 查询具体课程列表
def find_kpoint_data():
    url = "http://wljy.whut.edu.cn/edu/eduCourseKpoint/findKpointDataByNo.ajax"
    params = {"kpointNo": "150932"}
    session = requests.session()
    result = session.post(url, params, headers=headers)
    print(result.text.encode("utf-8"))

# 保存学习时间
def save_learn_time():
    url = "http://wljy.whut.edu.cn/edu/eduStuCourse/saveCourseLearnTime.ajax"
    params = {
        "userid": "203293412300022",
        "courlibNo": "2096",
        "learnTime": "290.99"
    }
    session = requests.session()
    result = session.post(url, params, headers=headers)
    print(result.text.encode("utf-8"))


# 保存视频播放记录
def save_play_data():
    url = "http://wljy.whut.edu.cn/edu/course/savePlayHistory.ajax"
    params = {
        "userId": "203293412300022",
        "courlibNo": "1774",
        "courseNo": "1663",
        "kPointNo": "150963",
        "process": "3000.151727",
        "type": "1"
    }
    session = requests.session()
    result = session.post(url, params, headers=headers)
    print(result.text.encode("utf-8"))

if __name__ == "__main__":
    find_kpoint_data()
    time.sleep(1)
    save_learn_time()
    time.sleep(1)
    save_play_data()
