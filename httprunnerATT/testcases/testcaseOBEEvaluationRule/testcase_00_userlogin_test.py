import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

class TestCseUserLogin(HttpRunner):
    config = (
        Config("OBE目标达成度分析-新建OBE设置信息")
        .variables(loginName="${ENV(LoginNameCourseAdmin)}",password="${ENV(passwordCourseAdmin)}",HOST="${ENV(TestHOST)}")
        .base_url("https://${HOST}")
        .verify(False)
        .export(*["authorization","ocid"])
    )
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
        )
    ]


if __name__ == "__main__":
    TestCseUserLogin().test_start()