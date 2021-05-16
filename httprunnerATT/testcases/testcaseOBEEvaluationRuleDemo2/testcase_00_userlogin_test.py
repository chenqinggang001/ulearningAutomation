import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

class TestCseUserLogin(HttpRunner):
    config = (
        Config("OBE目标达成度分析-新建OBE设置信息")
        .variables(loginNameadmin="${ENV(LoginNameCourseAdmin)}",loginNametea="${ENV(LoginNametea)}",password="${ENV(Password)}",HOST="${ENV(TestHOST)}")
        .base_url("https://${HOST}")
        .verify(False)
        .export(*["authorization","ocid","authorizationtea","ocidtea",\
            "linkList1","linkList2","linkList3","linkList4","linkList5","linkList6","linkList7","linkList8","linkList9","linkList10",\
            "outcomeList1","outcomeList2","outcomeList3","outcomeList4","outcomeList5","outcomeList6","outcomeList7","outcomeList8","outcomeList9","outcomeList10",\
            "userId1","userId2","userId3","userId4","classId1","classId2","classId3"])
    )
    teststeps = [
        Step(
            RunRequest("用户登录成功！")
            .post("/users/login")
            .with_headers(**{"Content-Type": "application/json"})
            .with_json({"loginName": "${loginNameadmin}","password": "wenhua123"})
            .extract()
            .with_jmespath("body.authorization", "authorization")
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("用户登录成功！")
            .post("/users/login")
            .with_headers(**{"Content-Type": "application/json"})
            .with_json({"loginName": "${loginNameadmin}","password": "wenhua123"})
            .extract()
            .with_jmespath("body.authorization", "authorizationtea")
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("获取课程列表")
            .get("/courses")
            .with_headers(**{"Content-Type": "application/json","Authorization":"$authorization"})
            .with_params(**{"keyword":"","publishStatus":"1","type":"1","pn":"1","ps":"15","octypeId":"","lang":"zh"})
            .extract()
            .with_jmespath("body.courseList[0].id", "ocid")
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("获取课程列表")
            .get("/courses")
            .with_headers(**{"Content-Type": "application/json","Authorization":"$authorizationtea"})
            .with_params(**{"keyword":"","publishStatus":"1","type":"1","pn":"1","ps":"15","octypeId":"","lang":"zh"})
            .extract()
            .with_jmespath("body.courseList[0].id", "ocidtea")
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("新建OBE设置信息")
            .post("/obe")
            .with_headers(**{"Content-Type": "application/json","Authorization":"$authorization"})
            .with_json(
                {
                    "id": 7,
                    "ocId": "$ocid",
                    "passScore": 0.7,
                    "linkList": [
                        {
                            "name": "考核环节1"
                        },
                        {
                            "name": "考核环节2"
                        },
                        {
                            "name": "考核环节3"
                        }
                    ],
                    "outcomeList": [
                        {
                            "description": "这是一个目标描述1",
                            "outcomeLinkDTOList": [
                                {
                                    "factor": 5,
                                    "code": "A"
                                },
                                {
                                    "factor": 10,
                                    "code": "B"
                                }
                            ]
                        },
                        {
                            "description": "这是一个目标描述2",
                            "outcomeLinkDTOList": [
                                {
                                    "factor": 10,
                                    "code": "A"
                                },
                                {
                                    "factor": 30,
                                    "code": "C"
                                }
                            ]
                        },
                        {
                            "description": "这是一个目标描述3",
                            "outcomeLinkDTOList": [
                                {
                                    "factor": 5,
                                    "code": "A"
                                },
                                {
                                    "factor": 20,
                                    "code": "B"
                                },
                                {
                                    "factor": 20,
                                    "code": "C"
                                }
                            ]
                        }
                    ]
                }
            )
            .extract()
            .with_jmespath("body.result.linkList[0].id","linkList1")
            .with_jmespath("body.result.linkList[1].id","linkList2")
            .with_jmespath("body.result.linkList[2].id","linkList3")
            .with_jmespath("body.result.linkList[3].id","linkList4")
            .with_jmespath("body.result.linkList[4].id","linkList5")
            .with_jmespath("body.result.linkList[5].id","linkList6")
            .with_jmespath("body.result.linkList[6].id","linkList7")
            .with_jmespath("body.result.linkList[7].id","linkList8")
            .with_jmespath("body.result.linkList[8].id","linkList9")
            .with_jmespath("body.result.linkList[9].id","linkList10")
            .with_jmespath("body.result.outcomeList[0].id","outcomeList1")
            .with_jmespath("body.result.outcomeList[1].id","outcomeList2")
            .with_jmespath("body.result.outcomeList[2].id","outcomeList3")
            .with_jmespath("body.result.outcomeList[3].id","outcomeList4")
            .with_jmespath("body.result.outcomeList[4].id","outcomeList5")
            .with_jmespath("body.result.outcomeList[5].id","outcomeList6")
            .with_jmespath("body.result.outcomeList[6].id","outcomeList7")
            .with_jmespath("body.result.outcomeList[7].id","outcomeList8")
            .with_jmespath("body.result.outcomeList[8].id","outcomeList9")
            .with_jmespath("body.result.outcomeList[9].id","outcomeList10")
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("获取课程内的教师信息")
            .get("/teachingteam/${ocid}")
            .with_headers(**{"Content-Type": "application/json","Authorization":"$authorization"})
            .with_params(**{"pn":"1","ps":"9999","lang":"zh"})
            .extract()
            .with_jmespath("body.list[0].userId", "userId1")
            .with_jmespath("body.list[1].userId", "userId2")
            .with_jmespath("body.list[2].userId", "userId3")
            .with_jmespath("body.list[3].userId", "userId4")
            .with_jmespath("body.list[0].classes[0].classId", "classId1")
            .with_jmespath("body.list[0].classes[1].classId", "classId2")
            .with_jmespath("body.list[0].classes[2].classId", "classId3")
        )
    ]


if __name__ == "__main__":
    TestCseUserLogin().test_start()