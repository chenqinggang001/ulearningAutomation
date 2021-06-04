import os, sys

sys.path.append(os.getcwd())

from pathlib import Path

# sys.path.insert(0, str(Path(__file__).parent.parent))

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from testcases.testcaseOBE2.OBE2_login_test import TestCaseUserLogin

class TestCaselike(HttpRunner):
    config = (
        Config("OBE目标达成度分析-新建OBE设置信息")
        .variables(loginNameadmin="${ENV(LoginNameCourseAdmin)}",loginNametea="${ENV(LoginNametea)}",password="${ENV(Password)}",HOST="${ENV(TestHOST)}")
        .base_url("https://${HOST}")
        .verify(False)
        .export(*["authorization","ocid","authorizationtea","ocidtea",\
        "linkList1","linkList2","linkList3",\
        "outcomeList1","outcomeList2","outcomeList3"])
    )
    teststeps = [
        Step(
            RunTestCase("获取用户信息")
            .call(TestCaseUserLogin)
            .export(*["authorization","ocid","authorizationtea","ocidtea",\
            "linkList1","linkList2","linkList3",\
            "outcomeList1","outcomeList2","outcomeList3"])
        ),
        Step(
            RunRequest("修改活动所属考核环节")  #考试
            .put("/obe/activityLink")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"ocId":"${ocid}","relationId":"11365","type":"2","linkId":"${linkList1}"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("修改活动所属考核环节")
            .put("/obe/activityLink")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"ocId":"${ocid}","relationId":"11364","type":"2","linkId":"${linkList1}"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("修改活动所属考核环节")
            .put("/obe/activityLink")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"ocId":"${ocid}","relationId":"11363","type":"2","linkId":"${linkList1}"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("修改活动所属考核环节")
            .put("/obe/activityLink")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"ocId":"${ocid}","relationId":"11362","type":"2","linkId":"${linkList1}"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("修改活动所属考核环节")
            .put("/obe/activityLink")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"ocId":"${ocid}","relationId":"11360","type":"2","linkId":"${linkList1}"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("修改活动所属考核环节")  # 作业
            .put("/obe/activityLink")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"ocId":"${ocid}","relationId":"169957","type":"3","linkId":"${linkList2}"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("修改活动所属考核环节")
            .put("/obe/activityLink")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"ocId":"${ocid}","relationId":"169955","type":"3","linkId":"${linkList2}"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("修改活动所属考核环节")
            .put("/obe/activityLink")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"ocId":"${ocid}","relationId":"169954","type":"3","linkId":"${linkList2}"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("修改活动所属考核环节")
            .put("/obe/activityLink")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"ocId":"${ocid}","relationId":"169953","type":"3","linkId":"${linkList2}"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("修改活动所属考核环节")
            .put("/obe/activityLink")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"ocId":"${ocid}","relationId":"169959","type":"3","linkId":"${linkList2}"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("修改活动所属考核环节")  # 讨论
            .put("/obe/activityLink")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"ocId":"${ocid}","relationId":"22959","type":"6","linkId":"${linkList3}"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("修改活动所属考核环节")
            .put("/obe/activityLink")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"ocId":"${ocid}","relationId":"22957","type":"6","linkId":"${linkList3}"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("修改活动所属考核环节")
            .put("/obe/activityLink")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"ocId":"${ocid}","relationId":"22953","type":"6","linkId":"${linkList3}"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("修改活动所属考核环节")
            .put("/obe/activityLink")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"ocId":"${ocid}","relationId":"22946","type":"6","linkId":"${linkList3}"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("修改活动所属考核环节")
            .put("/obe/activityLink")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"ocId":"${ocid}","relationId":"22869","type":"6","linkId":"${linkList3}"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("修改活动所属考核环节")
            .put("/obe/activityLink")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"ocId":"${ocid}","relationId":"22951","type":"6","linkId":"${linkList1}"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("修改活动关联的课程目标")    # 课程目标  作业
            .put("/obe/activityOutcome")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"ocId":"${ocid}","relationId":"169957","type":"3","outcomeId":"${outcomeList1}"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("修改活动关联的课程目标")    # 课程目标  作业
            .put("/obe/activityOutcome")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"ocId":"${ocid}","relationId":"169955","type":"3","outcomeId":"${outcomeList1}"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("修改活动关联的课程目标")    # 课程目标  作业
            .put("/obe/activityOutcome")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"ocId":"${ocid}","relationId":"169954","type":"3","outcomeId":"${outcomeList3}"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("修改活动关联的课程目标")    # 课程目标  作业
            .put("/obe/activityOutcome")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"ocId":"${ocid}","relationId":"169953","type":"3","outcomeId":"${outcomeList3}"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("修改活动关联的课程目标")    # 课程目标  作业
            .put("/obe/activityOutcome")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"ocId":"${ocid}","relationId":"169959","type":"3","outcomeId":"${outcomeList3}"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("修改活动关联的课程目标")    # 课程目标  讨论
            .put("/obe/activityOutcome")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"ocId":"${ocid}","relationId":"22959","type":"6","outcomeId":"${outcomeList2}"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("修改活动关联的课程目标")    # 课程目标  讨论
            .put("/obe/activityOutcome")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"ocId":"${ocid}","relationId":"22957","type":"6","outcomeId":"${outcomeList2}"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("修改活动关联的课程目标")    # 课程目标  讨论
            .put("/obe/activityOutcome")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"ocId":"${ocid}","relationId":"22953","type":"6","outcomeId":"${outcomeList2}"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("修改活动关联的课程目标")    # 课程目标  讨论
            .put("/obe/activityOutcome")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"ocId":"${ocid}","relationId":"22946","type":"6","outcomeId":"${outcomeList3}"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("修改活动关联的课程目标")    # 课程目标  讨论
            .put("/obe/activityOutcome")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"ocId":"${ocid}","relationId":"22869","type":"6","outcomeId":"${outcomeList3}"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("修改活动关联的课程目标")    # 课程目标  讨论
            .put("/obe/activityOutcome")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"ocId":"${ocid}","relationId":"22951","type":"6","outcomeId":"${outcomeList1}"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("修改活动关联的课程目标")    # 课程目标  作业
            .put("/obe/activityOutcome")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"ocId":"${ocid}","relationId":"169957","type":"3","outcomeId":"${outcomeList1}"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("修改考试关联的课程目标")    # 课程目标  考试
            .post("/obe/paperOutcomes")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"examId":"11365"})
            .with_json(
                [
                    {
                        "paperId": 109181,
                        "obeQuestionOutcomeDTOList":[
                        {"questionId":12247848,"outcomeId":"${outcomeList1}"},
                        {"questionId":12247847,"outcomeId":"${outcomeList1}"},
                        {"questionId":12247707,"outcomeId":"${outcomeList1}"},
                        {"questionId":12250433,"outcomeId":"${outcomeList1}"},
                        {"questionId":12250432,"outcomeId":"${outcomeList1}"},
                        {"questionId":12250431,"outcomeId":"${outcomeList1}"},
                        {"questionId":12250430,"outcomeId":"${outcomeList1}"},
                        {"questionId":12250429,"outcomeId":"${outcomeList1}"},
                        {"questionId":12250428,"outcomeId":"${outcomeList1}"},
                        {"questionId":12247849,"outcomeId":"${outcomeList1}"}
                        ]
                    }
                ]
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("修改考试关联的课程目标")    # 课程目标  考试
            .post("/obe/paperOutcomes")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"examId":"11364"})
            .with_json(
                [
                    {
                        "paperId":"109181",
                        "obeQuestionOutcomeDTOList":[
                        {"questionId":12247848,"outcomeId":"${outcomeList1}"},
                        {"questionId":12247847,"outcomeId":"${outcomeList1}"},
                        {"questionId":12247707,"outcomeId":"${outcomeList1}"},
                        {"questionId":12250433,"outcomeId":"${outcomeList1}"},
                        {"questionId":12250432,"outcomeId":"${outcomeList1}"},
                        {"questionId":12250431,"outcomeId":"${outcomeList1}"},
                        {"questionId":12250430,"outcomeId":"${outcomeList1}"},
                        {"questionId":12250429,"outcomeId":"${outcomeList1}"},
                        {"questionId":12250428,"outcomeId":"${outcomeList1}"},
                        {"questionId":12247849,"outcomeId":"${outcomeList1}"}
                        ]
                    }
                ]
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("修改考试关联的课程目标")    # 课程目标  考试
            .post("/obe/paperOutcomes")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"examId":"11363"})
            .with_json(
                [
                    {
                        "paperId":"109181",
                        "obeQuestionOutcomeDTOList":[
                        {"questionId":12247848,"outcomeId":"${outcomeList2}"},
                        {"questionId":12247847,"outcomeId":"${outcomeList2}"},
                        {"questionId":12247707,"outcomeId":"${outcomeList2}"},
                        {"questionId":12250433,"outcomeId":"${outcomeList2}"},
                        {"questionId":12250432,"outcomeId":"${outcomeList2}"},
                        {"questionId":12250431,"outcomeId":"${outcomeList2}"},
                        {"questionId":12250430,"outcomeId":"${outcomeList2}"},
                        {"questionId":12250429,"outcomeId":"${outcomeList2}"},
                        {"questionId":12250428,"outcomeId":"${outcomeList2}"},
                        {"questionId":12247849,"outcomeId":"${outcomeList2}"}
                        ]
                    }
                ]
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("修改考试关联的课程目标")    # 课程目标  考试
            .post("/obe/paperOutcomes")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"examId":"11362"})
            .with_json(
                [
                    {
                        "paperId":"109181",
                        "obeQuestionOutcomeDTOList":[
                        {"questionId":12247848,"outcomeId":"${outcomeList3}"},
                        {"questionId":12247847,"outcomeId":"${outcomeList3}"},
                        {"questionId":12247707,"outcomeId":"${outcomeList3}"},
                        {"questionId":12250433,"outcomeId":"${outcomeList3}"},
                        {"questionId":12250432,"outcomeId":"${outcomeList3}"},
                        {"questionId":12250431,"outcomeId":"${outcomeList3}"},
                        {"questionId":12250430,"outcomeId":"${outcomeList3}"},
                        {"questionId":12250429,"outcomeId":"${outcomeList3}"},
                        {"questionId":12250428,"outcomeId":"${outcomeList3}"},
                        {"questionId":12247849,"outcomeId":"${outcomeList3}"}
                        ]
                    }
                ]
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("修改考试关联的课程目标")    # 课程目标  考试
            .post("/obe/paperOutcomes")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"examId":"11360"})
            .with_json(
                [
                    {
                        "paperId":"109181",
                        "obeQuestionOutcomeDTOList":[
                        {"questionId":12247848,"outcomeId":"${outcomeList3}"},
                        {"questionId":12247847,"outcomeId":"${outcomeList3}"},
                        {"questionId":12247707,"outcomeId":"${outcomeList3}"},
                        {"questionId":12250433,"outcomeId":"${outcomeList3}"},
                        {"questionId":12250432,"outcomeId":"${outcomeList3}"},
                        {"questionId":12250431,"outcomeId":"${outcomeList1}"},
                        {"questionId":12250430,"outcomeId":"${outcomeList1}"},
                        {"questionId":12250429,"outcomeId":"${outcomeList1}"},
                        {"questionId":12250428,"outcomeId":"${outcomeList1}"},
                        {"questionId":12247849,"outcomeId":"${outcomeList1}"}
                        ]
                    }
                ]
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("新建线下活动")
            .post("/obe/offlineActivity")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_json(
                {
                    "id":"",
                    "ocId":"${ocid}",
                    "name":"线下活动1"
                }
            )
            .extract()
            .with_jmespath("body.result.id","offlineActivityId1")
        ),
        Step(
            RunRequest("修改活动所属考核环节")
            .put("/obe/activityLink")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"ocId":"${ocid}","relationId":"${offlineActivityId1}","type":"7","linkId":"${linkList1}"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("新建线下活动")
            .post("/obe/offlineActivity")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_json(
                {
                    "id":"",
                    "ocId":"${ocid}",
                    "name":"线下活动2"
                }
            )
            .extract()
            .with_jmespath("body.result.id","offlineActivityId2")
        ),
        Step(
            RunRequest("修改活动所属考核环节")
            .put("/obe/activityLink")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"ocId":"${ocid}","relationId":"${offlineActivityId2}","type":"7","linkId":"${linkList2}"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("新建线下活动")
            .post("/obe/offlineActivity")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_json(
                {
                    "id":"",
                    "ocId":"${ocid}",
                    "name":"线下活动3"
                }
            )
            .extract()
            .with_jmespath("body.result.id","offlineActivityId3")
        ),
        Step(
            RunRequest("修改活动所属考核环节")
            .put("/obe/activityLink")
            .with_headers(**{"Content-Type": "application/json","Authorization":"${authorization}"})
            .with_params(**{"ocId":"${ocid}","relationId":"${offlineActivityId3}","type":"7","linkId":"${linkList3}"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("导入线下教学活动的成绩")
            .post("/obe/offlineSubActivity/scores/import?offlineActivityId=${offlineActivityId1}")
            .with_headers(**{"Authorization":"${authorization}"})
            .upload(
                file="files\\OBE线下活动成绩导入模板1.xlsx"
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("导入线下教学活动的成绩")
            .post("/obe/offlineSubActivity/scores/import?offlineActivityId=${offlineActivityId2}")
            .with_headers(**{"Authorization":"${authorization}"})
            .upload(
                file="files\\OBE线下活动成绩导入模板2.xlsx"
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("导入线下教学活动的成绩")
            .post("/obe/offlineSubActivity/scores/import?offlineActivityId=${offlineActivityId3}")
            .with_headers(**{"Authorization":"${authorization}"})
            .upload(
                file="files\\OBE线下活动成绩导入模板3.xlsx"
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("发起达成度统计计算")
            .get("/obe/completionDegree/calculate")
            .with_headers(**{"Content-Type": "application/json","Authorization":"$authorizationtea"})
            .with_params(**{"ocId":"${ocid}"})
            .validate()
            .assert_equal("status_code", 200)
        )
    ]


if __name__ == "__main__":
    TestCaselike().test_start()