from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCseOBE(HttpRunner):
    config = (
        Config("OBE目标达成度分析-测试权重为1.01时，请求失败")
        .base_url("https://courseapi.tongshike.cn")
        .verify(False)
    )
    # 测试权重为1.01时，请求失败
    teststeps = [
        Step(
            RunRequest("用户登录成功！")
            .post("/users/login")
            .with_headers(**{"Content-Type": "application/json"})
            .with_json({"loginName": "chenqinggangtea","password": "wenhua123"})
            .extract()
            .with_jmespath("body.authorization", "authorization")
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
            RunRequest("测试权重为1.01时，请求失败")
            .post("/obe")
            .with_headers(**{"Content-Type": "application/json","Authorization":"$authorization"})
            .with_json(
                {
                    "id": 7,
                    "ocId": "$ocid",
                    "passScore": 1.01,
                    "linkList": [
                        {
                            "name": "作业1"
                        }
                    ],
                    "outcomeList": [
                        {
                            "description": "这是一个目标描述1",
                            "outcomeLinkDTOList": [
                                {
                                    "factor": 1,
                                    "code": "A"
                                }
                            ]
                        }
                    ]
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        )
    ]

if __name__ == "__main__":
    TestCseOBE().test_start()