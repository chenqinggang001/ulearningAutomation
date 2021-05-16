import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcaseOBEEvaluationRuleDemo2.testcase_0_relationId_test import TestCseRelationId

class TestCseOBE(HttpRunner):
    config = (
        Config("OBE目标达成度分析-获取在线活动列表")
        .variables(loginNameadmin="${ENV(LoginNameCourseAdmin)}",loginNametea="${ENV(LoginNametea)}",password="${ENV(Password)}",HOST="${ENV(TestHOST)}")
        .base_url("https://${HOST}")
        .verify(False)
    )
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
            "userId1","userId2","userId3","userId4","classId1","classId2",\
            "examId1","examId2","examId3","examId4","examId5","examId6","examId7","examId8","examId9","examId10",\
            "paperId1","paperId2","paperId3_1","paperId3_2","paperId3_3","paperId6",\
            ])
        ),
        Step(
            RunRequest("获取试卷的关联课程目标")                                        # 试卷
            .get("/obe/paperOutcome")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"paperId":"${paperId6}","examId":"${examId6}"})
            .extract()
            .with_jmespath("body.result[0].questionId", "questionId1")
            .with_jmespath("body.result[1].questionId", "questionId2")
            .with_jmespath("body.result[2].questionId", "questionId3")
            .with_jmespath("body.result[3].questionId", "questionId4")
            .with_jmespath("body.result[4].questionId", "questionId5")
            .with_jmespath("body.result[5].questionId", "questionId6")
            .with_jmespath("body.result[6].questionId", "questionId7")
            .with_jmespath("body.result[7].questionId", "questionId8")
            .with_jmespath("body.result[8].questionId", "questionId9")
            .with_jmespath("body.result[9].questionId", "questionId10")
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("获取试卷的关联课程目标")                                        # 试卷
            .post("/obe/paperOutcome")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"paperId":"${paperId1}","examId":"${examId1}"})
            .with_json([
                {"questionId":"${questionId1}","outcomeId":"${outcomeList1}"},
                {"questionId":"${questionId2}","outcomeId":"${outcomeList2}"},
                {"questionId":"${questionId3}","outcomeId":"${outcomeList2}"},
                {"questionId":"${questionId4}","outcomeId":"${outcomeList2}"},
                {"questionId":"${questionId5}","outcomeId":"${outcomeList1}"},
                {"questionId":"${questionId6}","outcomeId":"${outcomeList1}"},
                {"questionId":"${questionId7}","outcomeId":"${outcomeList1}"},
                {"questionId":"${questionId8}","outcomeId":"${outcomeList1}"},
                {"questionId":"${questionId9}","outcomeId":"${outcomeList1}"},
                {"questionId":"${questionId10}","outcomeId":"${outcomeList1}"},
            ])
            .extract()
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("获取达成度统计列表")
            .get("/obe/completionDegreeList")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"ocId":"${ocid}","pn":"1","ps":"999","teacherId":""})
            .extract()

        )
    ]


if __name__ == "__main__":
    TestCseOBE().test_start()