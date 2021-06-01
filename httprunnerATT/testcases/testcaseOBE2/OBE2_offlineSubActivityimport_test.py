import os, sys

sys.path.append(os.getcwd())

from pathlib import Path

# sys.path.insert(0, str(Path(__file__).parent.parent))

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.testcaseOBE2.OBE2_login_test import TestCaseUserLogin

class TestCseofflineSubActivityimport(HttpRunner):
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
            RunTestCase("获取用户信息")
            .call(TestCaseUserLogin)
            .export(*["authorization","ocid","authorizationtea","ocidtea",\
            "linkList1","linkList2","linkList3","linkList4","linkList5","linkList6","linkList7","linkList8","linkList9","linkList10",\
            "outcomeList1","outcomeList2","outcomeList3","outcomeList4","outcomeList5","outcomeList6","outcomeList7","outcomeList8","outcomeList9","outcomeList10",\
            "userId1","userId2","userId3","userId4","classId1","classId2","classId3"])
        ),
        Step(
            RunRequest("新建线下活动")
            .post("/obe/offlineActivity")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_json({"id":"","ocId":"${ocid}","name":"这是一个活动名称"})
            .extract()
            .with_jmespath("body.result.id", "offlineActivityId")
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("导入线下教学活动的成绩")
            .post("/obe/offlineSubActivity/scores/import?offlineActivityId=${offlineActivityId}")
            .with_headers(**{"Authorization":"${authorization}"})
            .upload(
                file="files\\OBE线下活动成绩导入模板.xlsx"
            )
            .validate()
            .assert_equal("status_code", 200)
        )
    ]


if __name__ == "__main__":
    TestCseofflineSubActivityimport().test_start()