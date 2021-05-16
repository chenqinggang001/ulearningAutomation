import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcaseOBEEvaluationRule.testcase_00_userlogin_test import TestCseUserLogin
from testcaseOBEEvaluationRule.testcase_0_relationId_test import TestCseRelationId

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
            .export(*["authorization","ocid","authorizationtea","ocidtea",\
            "linkList1","linkList2","linkList3","linkList4","linkList5","linkList6","linkList7","linkList8","linkList9","linkList10",\
            "outcomeList1","outcomeList2","outcomeList3","outcomeList4","outcomeList5","outcomeList6","outcomeList7","outcomeList8","outcomeList9","outcomeList10",\
            "userId1","userId2","userId3","userId4","classId1","classId2"])
        ),
        Step(
            RunTestCase("获取课件ID")
            .call(TestCseRelationId)
            .export(*["textbookId2"])
        ),
        Step(
            RunRequest("修改活动的关联课程目标")
            .put("/obe/activityOutcome")
            .with_headers(**{"Content-Type": "application/json","Authorization":"$authorization"})
            .with_params(**{"relationId":"${textbookId2}","type":"1","outcomeId":"${outcomeList1}"})
            .validate()
            .assert_equal("body.message", "成功")
        )
    ]


if __name__ == "__main__":
    TestCseOBE().test_start()