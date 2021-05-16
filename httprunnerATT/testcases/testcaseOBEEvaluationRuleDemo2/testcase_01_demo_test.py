import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from testcaseOBEEvaluationRuleDemo2.testcase_00_userlogin_test import TestCseUserLogin

class TestCseOBE(HttpRunner):
    config = (
        Config("OBE目标达成度分析")
        .base_url("https://courseapi.tongshike.cn")
        .verify(False)
    )
    teststeps = [
        Step(
            RunTestCase("用户登录成功")
            .call(TestCseUserLogin)
            .export(*["authorization","ocid"])
        ),
        Step(
            RunRequest("获取课件列表")
            .get("/obe/textbooks")
            .with_headers(**{"Content-Type": "application/json","Authorization":"$authorization"})
            .with_params(**{"ocId":"$ocid"})
            .validate()
            .assert_equal("status_code", 200)
        )
    ]


if __name__ == "__main__":
    TestCseOBE().test_start()