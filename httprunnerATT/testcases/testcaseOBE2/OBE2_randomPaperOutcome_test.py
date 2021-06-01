import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.testcaseOBE2.OBE2_login_test import TestCaseUserLogin

class TestCseUserLogin(HttpRunner):
    config = (
        Config("OBE目标达成度分析-新建OBE设置信息")
        .variables(loginNameadmin="${ENV(LoginNameCourseAdmin)}",loginNametea="${ENV(LoginNametea)}",password="${ENV(Password)}",HOST="${ENV(TestHOST)}")
        .base_url("https://${HOST}")
        .verify(False)
        .export(*[])
    )
    teststeps = [
        Step(
            RunTestCase("获取用户信息")
            .call(TestCaseUserLogin)
            .export(*["authorization","ocid","authorizationtea","ocidtea",\
            "linkList1","linkList2","linkList3","linkList4","linkList5","linkList6","linkList7","linkList8","linkList9","linkList10",\
            "outcomeList1","outcomeList2","outcomeList3","outcomeList4","outcomeList5","outcomeList6","outcomeList7","outcomeList8","outcomeList9","outcomeList10",\
            "userId1","userId2","userId3","userId4","classId1","classId2","classId3"])
        ),
        Step(
            RunRequest("保存随机抽题考试的关联课程目标")
            .post("/obe/randomPaperOutcome")
            .with_headers(**{"Content-Type": "application/json","Authorization":"authorization"})
            .with_params(**{"examId":"authorization"})
            .with_json({"loginName": "${loginNameadmin}","password": "wenhua123"})
            .extract()
            .with_jmespath("body.authorization", "authorization")
            .validate()
            .assert_equal("status_code", 200)
        )
    ]


if __name__ == "__main__":
    TestCseUserLogin().test_start()