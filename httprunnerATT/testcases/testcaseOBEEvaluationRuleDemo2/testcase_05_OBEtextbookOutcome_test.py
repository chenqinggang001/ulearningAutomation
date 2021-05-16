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
            RunRequest("获取课件的关联课程目标")
            .get("/obe/textbookOutcome")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"ocId":"${ocid}","textbookId":"${textbookId2}"})
            .extract()
            .with_jmespath("body.result.chapterOutcomeDTOList[0].itemOutcomeDTOList[0].itemId", "itemId1_1")        # 获取课件节的ID   格式:1_1   第几章_第几节
            .with_jmespath("body.result.chapterOutcomeDTOList[0].itemOutcomeDTOList[1].itemId", "itemId1_2")
            .with_jmespath("body.result.chapterOutcomeDTOList[0].itemOutcomeDTOList[2].itemId", "itemId1_3")
            .with_jmespath("body.result.chapterOutcomeDTOList[1].itemOutcomeDTOList[0].itemId", "itemId2_1")
            .with_jmespath("body.result.chapterOutcomeDTOList[2].itemOutcomeDTOList[0].itemId", "itemId3_1")
            .with_jmespath("body.result.chapterOutcomeDTOList[2].itemOutcomeDTOList[1].itemId", "itemId3_2")
            .with_jmespath("body.result.chapterOutcomeDTOList[2].itemOutcomeDTOList[2].itemId", "itemId3_3")
            .validate()
            .assert_equal("body.message", "成功")
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("获取课件的关联课程目标")
            .post("/obe/textbookOutcome")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"textbookId":"${textbookId2}","ocId":"${ocid}"})
            # .with_json([{"itemId":"${itemId1_1}","outcomeId":"${outcomeList1}"},{"itemId":"${itemId1_2}","outcomeId":"${outcomeList1}"},\
            #              {"itemId":"${itemId1_3}","outcomeId":"${outcomeList3}"},{"itemId":"${itemId2_1}","outcomeId":"${outcomeList1}"},\
            #              {"itemId":"${itemId3_1}","outcomeId":"${outcomeList1}"},{"itemId":"${itemId3_2}","outcomeId":"${outcomeList1}"},\
            #              {"itemId":"${itemId3_3}","outcomeId":"${outcomeList1}"}])
            .with_json(
                [
                    {"itemId": "${itemId1_1}", "outcomeId": "${outcomeList1}"},
                    {"itemId": "${itemId1_2}", "outcomeId": "${outcomeList2}"},
                    {"itemId": "${itemId1_3}", "outcomeId": "${outcomeList2}"},
                    {"itemId": "${itemId2_1}", "outcomeId": "${outcomeList3}"},
                    {"itemId": "${itemId3_1}", "outcomeId": "${outcomeList4}"},
                ]
            )
            .extract()
            .validate()
            .assert_equal("body.message", "成功")
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("获取课件的关联课程目标")
            .get("/obe/textbookOutcome")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"ocId":"${ocid}","textbookId":"${textbookId2}"})
            .validate()
            .assert_equal("status_code", 200)
        )
    ]


if __name__ == "__main__":
    TestCseOBE().test_start()