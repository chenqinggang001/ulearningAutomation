from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from platform import python_version_tuple
import sys
from pathlib import Path

from json import JSONDecoder, JSONEncoder, JSONDecodeError
import pytest
from httprunner import Parameters

sys.path.insert(0, str(Path(__file__).parent.parent))


class TestCaseUserLogin(HttpRunner):
    @pytest.mark.parametrize(
        "param", Parameters(
            {
                "loginname": ["chenqinggangtea", "teststu001"],
                "passwrod": ["wenhua123", "wenhua123"]
            }
        )
    )
    def test_start(self, param):
        super().test_start(param)

    config = (
        Config("OBE目标达成度分析-新建OBE设置信息")
        .variables(loginNameadmin="${ENV(LoginNameCourseAdmin)}", loginNametea="${ENV(LoginNametea)}", password="${ENV(Password)}", HOST="${ENV(TestHOST)}")
        .base_url("https://${HOST}")
        .verify(False)
        .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("用户登录成功！")
            .post("/users/login")
            .with_headers(**{"Content-Type": "application/json"})
            .with_json({"loginName": "${pram.loginname}", "password": "${pram.password}"})
            .extract()
            .with_jmespath("body.authorization", "authorization")
            .validate()
            .assert_equal("status_code", 200)
        )
    ]


if __name__ == "__main__":
    TestCaseUserLogin().test_start()
