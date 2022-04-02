# coding=utf-8

"""
使用Requests库完成Post表单操作
"""
import requests
import time
import json

cookie = "JSESSIONID=1127B6422F17E92CF01A4B4787103B03; sspm_proctorUrl=http://wljy.whut.edu.cn:80/; sspm_orgid=4406; sspm_appid=157438568781088"
headers = {
    "Cookie": cookie,
    "Referer": "Referer: http://wljy.whut.edu.cn/web/admissionprocess.htm",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}

# 查询我的课程
def find_edu_stu_course():
    print("查询我的课程开始...")
    url = "http://wljy.whut.edu.cn/edu/eduStuCourse/findEduStuCourse.ajax"
    params = {"userid": "203293412300022"}
    session = requests.session()
    result = session.post(url, params, headers=headers)
    data = result.text.encode("utf-8")
    print(data)
    data2 = json.loads(data)
    data3 = data2['mycourse']
    json_txt = []
    for courseData in data3:
        print(courseData['courNo'] + ' ' + courseData['courName'] + ' ' + courseData['state'])
        json_data = {}
        json_data["courNo"] = courseData['courNo']
        json_data["state"] = courseData['state']
        json_txt.append(json_data)
    return json_txt

# 检查和刷新我的课程
def check_refresh_course(json_data):
    print("检查和刷新我的课程开始...")
    for data2 in json_data:
        courNo = data2['courNo']
        state = float(data2['state'])
        if(state <= 340):
            num = 10
            while(num >=0):
                num = num -1
                refresh_course(courNo)
        else:
            print("课程结束: %s"%data2)

# 刷新我的课程
def refresh_course(courNo):
    print("刷新我的课程开始...")
    print(courNo)
    time.sleep(1)
    url = "http://wljy.whut.edu.cn/edu/eduStuCourse/saveCourseLearnTime.ajax"
    params = {
        "userid": "203293412300022",
        "courlibNo": courNo,
        "learnTime": "290.99"
    }
    session = requests.session()
    result = session.post(url, params, headers=headers)
    print(result.text.encode("utf-8"))

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
def save_play_history_data():
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
    json_data = find_edu_stu_course()
    print("我的课程结果: %s"%json_data)
    check_refresh_course(json_data)
    # find_kpoint_data()
    # time.sleep(1)
    # save_learn_time()
    # time.sleep(1)
    # save_play_history_data
