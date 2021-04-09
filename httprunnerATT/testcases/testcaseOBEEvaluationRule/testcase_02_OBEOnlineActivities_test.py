from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
import xlrd

class TestCseOBE(HttpRunner):
    config = (
        Config("OBE目标达成度分析-获取在线活动列表")
        .base_url("https://courseapi.tongshike.cn")
        .verify(False)
    )
    # 测试输入10个正确的环节和目标时，请求成功
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
            RunRequest("获取课件列表")
            .get("/obe/onlineActivities")
            .with_headers(**{"Content-Type": "application/json","Authorization":"$authorization"})
            .with_params(**{"ocId":"$ocid","teacherId":"","type":"2","classId":"","keyword":"","pn":"1","ps":"10"})
            .validate()
            .assert_equal("status_code", 200)
        )
    ]


if __name__ == "__main__":
    TestCseOBE().test_start()