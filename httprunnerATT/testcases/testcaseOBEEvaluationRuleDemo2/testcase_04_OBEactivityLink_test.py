import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcaseOBEEvaluationRuleDemo2.testcase_0_relationId_test import TestCseRelationId

class TestCseOBE(HttpRunner):
    config = (
        Config("OBE目标达成度分析-获取在线活动列表")
        .base_url("https://courseapi.tongshike.cn")
        .verify(False)
    )
    # 测试输入10个正确的环节和目标时，请求成功
    teststeps = [
        Step(
            RunTestCase("获取活动ID")
            .call(TestCseRelationId)
            .export(*["textbookId1","textbookId2","textbookId3","textbookId4","textbookId5",\
            "relationIdexam1","relationIdexam2","relationIdexam3","relationIdexam4","relationIdexam5","relationIdexam6","relationIdexam7","relationIdexam8","relationIdexam9","relationIdexam10",\
            "relationIdstudent1","relationIdstudent2","relationIdstudent3","relationIdstudent4","relationIdstudent5","relationIdstudent6","relationIdstudent7","relationIdstudent8","relationIdstudent9","relationIdstudent10",\
            "relationIdgroup1","relationIdgroup2","relationIdgroup3","relationIdgroup4","relationIdgroup5","relationIdgroup6","relationIdgroup7","relationIdgroup8","relationIdgroup9","relationIdgroup10",\
            "relationIdactivity1","relationIdactivity2","relationIdactivity3","relationIdactivity4","relationIdactivity5","relationIdactivity6","relationIdactivity7","relationIdactivity8","relationIdactivity9","relationIdactivity10",\
            "authorization","ocid","authorizationtea","ocidtea",\
            "linkList1","linkList2","linkList3","linkList4","linkList5","linkList6","linkList7","linkList8","linkList9","linkList10",\
            "outcomeList1","outcomeList2","outcomeList3","outcomeList4","outcomeList5","outcomeList6","outcomeList7","outcomeList8","outcomeList9","outcomeList10",\
            "userId1","userId2","userId3","userId4","classId1","classId2"
            ])
        ),
        Step(
            RunRequest("修改活动的所属考核环节")                # 个人作业
            .put("/obe/activityLink")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"relationId":"${relationIdstudent1}","type":"3","linkId":"${linkList1}"})
            .validate()
            .assert_equal("body.message", "成功")
        ),
        Step(
            RunRequest("修改活动的所属考核环节")                # 小组作业
            .put("/obe/activityLink")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"relationId":"${relationIdgroup1}","type":"4","linkId":"${linkList1}"})
            .validate()
            .assert_equal("body.message", "成功")
        ),
        Step(
            RunRequest("修改活动的所属考核环节")                # 测验
            .put("/obe/activityLink")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"relationId":"${relationIdactivity1}","type":"5","linkId":"${linkList1}"})
            .validate()
            .assert_equal("body.message", "成功")
        ),
        Step(
            RunRequest("修改活动的所属考核环节")                # 考试
            .put("/obe/activityLink")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"relationId":"${relationIdexam1}","type":"2","linkId":"${linkList1}"})
            .validate()
            .assert_equal("body.message", "成功")
        )
    ]


if __name__ == "__main__":
    TestCseOBE().test_start()