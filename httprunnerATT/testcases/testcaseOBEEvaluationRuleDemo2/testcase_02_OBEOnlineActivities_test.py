import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcaseOBEEvaluationRuleDemo2.testcase_00_userlogin_test import TestCseUserLogin

class TestCseOBE(HttpRunner):
    config = (
        Config("OBE目标达成度分析-获取在线活动列表")
        .base_url("https://courseapi.tongshike.cn")
        .verify(False)
    )
    teststeps = [
        Step(
            RunTestCase("用户登录成功")
            .call(TestCseUserLogin)
            .export(*["authorization","ocid","authorizationtea","ocidtea","linkList1","linkList2","linkList3","linkList4","linkList5","linkList6","linkList7","linkList8","linkList9","linkList10",\
            "outcomeList1","outcomeList2","outcomeList3","outcomeList4","outcomeList5","outcomeList6","outcomeList7","outcomeList8","outcomeList9","outcomeList10",\
            "userId1","userId2","userId3","userId4","classId1","classId2"])
        ),
        Step(
            RunRequest("获取在线活动列表")                                            # 考试
            .get("/obe/onlineActivities")
            .with_headers(**{"Content-Type": "application/json","Authorization":"$authorization"})
            .with_params(**{"ocId":"$ocid","teacherId":"${userId1}","type":"2","classId":"${classId1}","keyword":"","pn":"1","ps":"10"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.result.list[0].type", 2)
        ),
        Step(
            RunRequest("获取课件")                                                    # 个人作业
            .get("/obe/onlineActivities")
            .with_headers(**{"Content-Type": "application/json","Authorization":"$authorization"})
            .with_params(**{"ocId":"$ocid","teacherId":"${userId1}","type":"3","classId":"${classId2}","keyword":"","pn":"1","ps":"10"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.result.list[0].type", 3)
        ),
        Step(
            RunRequest("获取课件")                                                    # 小组作业
            .get("/obe/onlineActivities")
            .with_headers(**{"Content-Type": "application/json","Authorization":"$authorization"})
            .with_params(**{"ocId":"$ocid","teacherId":"${userId1}","type":"4","classId":"${classId2}","keyword":"","pn":"1","ps":"10"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.result.list[0].type", 4)
        ),
        Step(
            RunRequest("获取课件")                                                    # 测验
            .get("/obe/onlineActivities")
            .with_headers(**{"Content-Type": "application/json","Authorization":"$authorization"})
            .with_params(**{"ocId":"$ocid","teacherId":"${userId1}","type":"5","classId":"${classId2}","keyword":"","pn":"1","ps":"10"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.result.list[0].type", 5)
        ),
        Step(
            RunRequest("获取课件")                                                    # 关键字查询
            .get("/obe/onlineActivities")
            .with_headers(**{"Content-Type": "application/json","Authorization":"$authorization"})
            .with_params(**{"ocId":"$ocid","teacherId":"${userId1}","type":"","classId":"${classId2}","keyword":"作业","pn":"1","ps":"10"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_contains("body.result.list[0].activityName", "作业")
            .assert_contains("body.result.list[1].activityName", "作业")
        ),
        Step(
            RunRequest("获取课件")                                                    # 教师账号查看自己班级测验
            .get("/obe/onlineActivities")
            .with_headers(**{"Content-Type": "application/json","Authorization":"$authorizationtea"})
            .with_params(**{"ocId":"$ocid","teacherId":"","type":"5","classId":"","keyword":"","pn":"1","ps":"10"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_length_equal("body.result.list", 0)
        )
        # Step   #讨论
    ]


if __name__ == "__main__":
    TestCseOBE().test_start()