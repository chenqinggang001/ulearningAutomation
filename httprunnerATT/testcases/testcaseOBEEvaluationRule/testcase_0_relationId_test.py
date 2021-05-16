import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcaseOBEEvaluationRule.testcase_00_userlogin_test import TestCseUserLogin

class TestCseRelationId(HttpRunner):
    config = (
        Config("OBE目标达成度分析-获取在线活动列表")
        .base_url("https://courseapi.tongshike.cn")
        .verify(False)
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
    )
    # 测试输入10个正确的环节和目标时，请求成功
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
            RunRequest("获取在线活动列表")                                            # 考试
            .get("/obe/onlineActivities")
            .with_headers(**{"Content-Type": "application/json","Authorization":"$authorizationtea"})
            .with_params(**{"ocId":"$ocid","teacherId":"","type":"2","classId":"","keyword":"","pn":"1","ps":"10"})
            .extract()
            .with_jmespath("body.result.list[0].relationId", "relationIdexam1")
            .with_jmespath("body.result.list[1].relationId", "relationIdexam2")
            .with_jmespath("body.result.list[2].relationId", "relationIdexam3")
            .with_jmespath("body.result.list[3].relationId", "relationIdexam4")
            .with_jmespath("body.result.list[4].relationId", "relationIdexam5")
            .with_jmespath("body.result.list[5].relationId", "relationIdexam6")
            .with_jmespath("body.result.list[6].relationId", "relationIdexam7")
            .with_jmespath("body.result.list[7].relationId", "relationIdexam8")
            .with_jmespath("body.result.list[8].relationId", "relationIdexam9")
            .with_jmespath("body.result.list[9].relationId", "relationIdexam10")
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("获取课件")                                                    # 个人作业
            .get("/obe/onlineActivities")
            .with_headers(**{"Content-Type": "application/json","Authorization":"$authorization"})
            .with_params(**{"ocId":"$ocid","teacherId":"","type":"3","classId":"","keyword":"","pn":"1","ps":"10"})
            .extract()
            .with_jmespath("body.result.list[0].relationId", "relationIdstudent1")
            .with_jmespath("body.result.list[1].relationId", "relationIdstudent2")
            .with_jmespath("body.result.list[2].relationId", "relationIdstudent3")
            .with_jmespath("body.result.list[3].relationId", "relationIdstudent4")
            .with_jmespath("body.result.list[4].relationId", "relationIdstudent5")
            .with_jmespath("body.result.list[5].relationId", "relationIdstudent6")
            .with_jmespath("body.result.list[6].relationId", "relationIdstudent7")
            .with_jmespath("body.result.list[7].relationId", "relationIdstudent8")
            .with_jmespath("body.result.list[8].relationId", "relationIdstudent9")
            .with_jmespath("body.result.list[9].relationId", "relationIdstudent10")
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("获取课件")                                                    # 小组作业
            .get("/obe/onlineActivities")
            .with_headers(**{"Content-Type": "application/json","Authorization":"$authorization"})
            .with_params(**{"ocId":"$ocid","teacherId":"","type":"4","classId":"","keyword":"","pn":"1","ps":"10"})
            .extract()
            .with_jmespath("body.result.list[0].relationId", "relationIdgroup1")
            .with_jmespath("body.result.list[1].relationId", "relationIdgroup2")
            .with_jmespath("body.result.list[2].relationId", "relationIdgroup3")
            .with_jmespath("body.result.list[3].relationId", "relationIdgroup4")
            .with_jmespath("body.result.list[4].relationId", "relationIdgroup5")
            .with_jmespath("body.result.list[5].relationId", "relationIdgroup6")
            .with_jmespath("body.result.list[6].relationId", "relationIdgroup7")
            .with_jmespath("body.result.list[7].relationId", "relationIdgroup8")
            .with_jmespath("body.result.list[8].relationId", "relationIdgroup9")
            .with_jmespath("body.result.list[9].relationId", "relationIdgroup10")
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("获取课件")                                                    # 测验
            .get("/obe/onlineActivities")
            .with_headers(**{"Content-Type": "application/json","Authorization":"$authorization"})
            .with_params(**{"ocId":"$ocid","teacherId":"","type":"5","classId":"","keyword":"","pn":"1","ps":"10"})
            .extract()
            .with_jmespath("body.result.list[0].relationId", "relationIdactivity1")
            .with_jmespath("body.result.list[1].relationId", "relationIdactivity2")
            .with_jmespath("body.result.list[2].relationId", "relationIdactivity3")
            .with_jmespath("body.result.list[3].relationId", "relationIdactivity4")
            .with_jmespath("body.result.list[4].relationId", "relationIdactivity5")
            .with_jmespath("body.result.list[5].relationId", "relationIdactivity6")
            .with_jmespath("body.result.list[6].relationId", "relationIdactivity7")
            .with_jmespath("body.result.list[7].relationId", "relationIdactivity8")
            .with_jmespath("body.result.list[8].relationId", "relationIdactivity9")
            .with_jmespath("body.result.list[9].relationId", "relationIdactivity10")
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(                                                                       # 课件
            RunRequest("获取课件列表")
            .get("/obe/textbooks")
            .with_headers(**{"Content-Type": "application/json","Authorization":"$authorization"})
            .with_params(**{"ocId":"$ocid"})
            .extract()
            .with_jmespath("body.result[0].textbookId", "textbookId1")      # 口语评测
            .with_jmespath("body.result[1].textbookId", "textbookId2")      # tuxi_测试课程
            .with_jmespath("body.result[2].textbookId", "textbookId3")      # 新交互大学英语2
            .with_jmespath("body.result[3].textbookId", "textbookId4")      # 商务洽谈（中级）
            .with_jmespath("body.result[4].textbookId", "textbookId5")      # 朗文交互英语第一级
            .validate()
        ),
        Step(                                                                       # 考试
            RunRequest("获取考试列表")
            .get("/obe/onlineActivities")
            .with_headers(**{"Content-Type": "application/json","Authorization":"$authorization"})
            .with_params(**{"ocId":"$ocid","teacherId":"","type":"2","classId":"","keyword":"","pn":"1","ps":"999"})
            .extract()
            .with_jmespath("body.result.list[0].relationId", "examId1")
            .with_jmespath("body.result.list[1].relationId", "examId2")
            .with_jmespath("body.result.list[2].relationId", "examId3")
            .with_jmespath("body.result.list[3].relationId", "examId4")
            .with_jmespath("body.result.list[4].relationId", "examId5")
            .with_jmespath("body.result.list[5].relationId", "examId6")
            .with_jmespath("body.result.list[6].relationId", "examId7")
            .with_jmespath("body.result.list[7].relationId", "examId8")
            .with_jmespath("body.result.list[8].relationId", "examId9")
            .with_jmespath("body.result.list[9].relationId", "examId10")
        ),
        Step(                                                                       # 试卷
            RunRequest("获取试卷列表")
            .get("/exams/${examId1}")
            .with_headers(**{"Content-Type": "application/json","Authorization":"$authorization"})
            .extract()
            .with_jmespath("body.examPaperList[0].paperId", "paperId1")
        ),
        Step(                                                                       # 试卷
            RunRequest("获取试卷列表")
            .get("/exams/${examId2}")
            .with_headers(**{"Content-Type": "application/json","Authorization":"$authorization"})
            .extract()
            .with_jmespath("body.examPaperList[0].paperId", "paperId2")
        ),
        Step(                                                                       # 试卷
            RunRequest("获取试卷列表")
            .get("/exams/${examId3}")
            .with_headers(**{"Content-Type": "application/json","Authorization":"$authorization"})
            .extract()
            .with_jmespath("body.examPaperList[0].paperId", "paperId3_1")
            .with_jmespath("body.examPaperList[1].paperId", "paperId3_2")
            .with_jmespath("body.examPaperList[2].paperId", "paperId3_3")
        ),
        Step(                                                                       # 试卷
            RunRequest("获取试卷列表")
            .get("/exams/${examId6}")
            .with_headers(**{"Content-Type": "application/json","Authorization":"$authorization"})
            .extract()
            .with_jmespath("body.examPaperList[0].paperId", "paperId6")
        ),
        # Step(                                                                       # 试卷
        #     RunRequest("获取试卷列表")
        #     .get("/exams/${examId5}")
        #     .with_headers(**{"Content-Type": "application/json","Authorization":"$authorization"})
        #     .extract()
        #     .with_jmespath("body.examPaperList[0].paperId", "paperId5")
        # )
    ]


if __name__ == "__main__":
    TestCseRelationId().test_start()