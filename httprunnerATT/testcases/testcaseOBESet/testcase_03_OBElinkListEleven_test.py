from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCseOBE(HttpRunner):
    config = (
        Config("OBE目标达成度分析-修改OBE设置信息-目标环节大于10个")
        .base_url("https://courseapi.tongshike.cn")
        .verify(False)
    )
    # 测试设置的环节和目标超过10个时，请求失败
    teststeps = [
        Step(
            RunRequest("用户登录成功！")
            .post("/users/login")
            .with_headers(**{"Content-Type": "application/json"})
            .with_json({"loginName": "chenqinggangtea","password": "wenhua123"})
            .extract()
            .with_jmespath("body.authorization", "authorization")
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("获取课程列表")
            .get("/courses")
            .with_headers(**{"Content-Type": "application/json","Authorization":"$authorization"})
            .with_params(**{"keyword":"","publishStatus":"1","type":"1","pn":"1","ps":"15","octypeId":"","lang":"zh"})
            .extract()
            .with_jmespath("body.courseList[0].id", "ocid")
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("修改OBE设置信息-目标环节大于10个")
            .post("/obe")
            .with_headers(**{"Content-Type": "application/json","Authorization":"$authorization"})
            .with_json(
                {
                    "id": 7,
                    "ocId": "$ocid",
                    "passScore": 0.6,
                    "linkList": [
                        {
                            "name": "作业1"
                        },
                        {
                            "name": "作业2"
                        },
                        {
                            "name": "作业3"
                        },
                        {
                            "name": "作业4"
                        },
                        {
                            "name": "作业5"
                        },
                        {
                            "name": "作业6"
                        },
                        {
                            "name": "作业7"
                        },
                        {
                            "name": "作业8"
                        },
                        {
                            "name": "作业9"
                        },
                        {
                            "name": "作业10"
                        },
                        {
                            "name": "作业11"
                        }
                    ],
                    "outcomeList": [
                        {
                            "description": "这是一个目标描述1",
                            "outcomeLinkDTOList": [
                                {
                                    "factor": 1,
                                    "code": "A"
                                },
                                {
                                    "factor": 1,
                                    "code": "B"
                                },
                                {
                                    "factor": 1,
                                    "code": "C"
                                },
                                {
                                    "factor": 1,
                                    "code": "D"
                                },
                                {
                                    "factor": 1,
                                    "code": "E"
                                },
                                {
                                    "factor": 1,
                                    "code": "F"
                                },
                                {
                                    "factor": 1,
                                    "code": "G"
                                },
                                {
                                    "factor": 1,
                                    "code": "H"
                                },
                                {
                                    "factor": 1,
                                    "code": "I"
                                },
                                {
                                    "factor": 1,
                                    "code": "J"
                                },
                                {
                                    "factor": 1,
                                    "code": "K"
                                }
                            ]
                        },
                        {
                            "description": "这是一个目标描述2",
                            "outcomeLinkDTOList": [
                                {
                                    "factor": 1,
                                    "code": "A"
                                },
                                {
                                    "factor": 1,
                                    "code": "B"
                                },
                                {
                                    "factor": 1,
                                    "code": "C"
                                },
                                {
                                    "factor": 1,
                                    "code": "D"
                                },
                                {
                                    "factor": 1,
                                    "code": "E"
                                },
                                {
                                    "factor": 1,
                                    "code": "F"
                                },
                                {
                                    "factor": 1,
                                    "code": "G"
                                },
                                {
                                    "factor": 1,
                                    "code": "H"
                                },
                                {
                                    "factor": 1,
                                    "code": "I"
                                },
                                {
                                    "factor": 1,
                                    "code": "J"
                                },
                                {
                                    "factor": 1,
                                    "code": "K"
                                }
                            ]
                        },
                        {
                            "description": "这是一个目标描述3",
                            "outcomeLinkDTOList": [
                                {
                                    "factor": 1,
                                    "code": "A"
                                },
                                {
                                    "factor": 1,
                                    "code": "B"
                                },
                                {
                                    "factor": 1,
                                    "code": "C"
                                },
                                {
                                    "factor": 1,
                                    "code": "D"
                                },
                                {
                                    "factor": 1,
                                    "code": "E"
                                },
                                {
                                    "factor": 1,
                                    "code": "F"
                                },
                                {
                                    "factor": 1,
                                    "code": "G"
                                },
                                {
                                    "factor": 1,
                                    "code": "H"
                                },
                                {
                                    "factor": 1,
                                    "code": "I"
                                },
                                {
                                    "factor": 1,
                                    "code": "J"
                                },
                                {
                                    "factor": 1,
                                    "code": "K"
                                }
                            ]
                        },
                        {
                            "description": "这是一个目标描述4",
                            "outcomeLinkDTOList": [
                                {
                                    "factor": 1,
                                    "code": "A"
                                },
                                {
                                    "factor": 1,
                                    "code": "B"
                                },
                                {
                                    "factor": 1,
                                    "code": "C"
                                },
                                {
                                    "factor": 1,
                                    "code": "D"
                                },
                                {
                                    "factor": 1,
                                    "code": "E"
                                },
                                {
                                    "factor": 1,
                                    "code": "F"
                                },
                                {
                                    "factor": 1,
                                    "code": "G"
                                },
                                {
                                    "factor": 1,
                                    "code": "H"
                                },
                                {
                                    "factor": 1,
                                    "code": "I"
                                },
                                {
                                    "factor": 1,
                                    "code": "J"
                                },
                                {
                                    "factor": 1,
                                    "code": "K"
                                }
                            ]
                        },
                        {
                            "description": "这是一个目标描述5",
                            "outcomeLinkDTOList": [
                                {
                                    "factor": 1,
                                    "code": "A"
                                },
                                {
                                    "factor": 1,
                                    "code": "B"
                                },
                                {
                                    "factor": 1,
                                    "code": "C"
                                },
                                {
                                    "factor": 1,
                                    "code": "D"
                                },
                                {
                                    "factor": 1,
                                    "code": "E"
                                },
                                {
                                    "factor": 1,
                                    "code": "F"
                                },
                                {
                                    "factor": 1,
                                    "code": "G"
                                },
                                {
                                    "factor": 1,
                                    "code": "H"
                                },
                                {
                                    "factor": 1,
                                    "code": "I"
                                },
                                {
                                    "factor": 1,
                                    "code": "J"
                                },
                                {
                                    "factor": 1,
                                    "code": "K"
                                }
                            ]
                        },
                        {
                            "description": "这是一个目标描述6",
                            "outcomeLinkDTOList": [
                                {
                                    "factor": 1,
                                    "code": "A"
                                },
                                {
                                    "factor": 1,
                                    "code": "B"
                                },
                                {
                                    "factor": 1,
                                    "code": "C"
                                },
                                {
                                    "factor": 1,
                                    "code": "D"
                                },
                                {
                                    "factor": 1,
                                    "code": "E"
                                },
                                {
                                    "factor": 1,
                                    "code": "F"
                                },
                                {
                                    "factor": 1,
                                    "code": "G"
                                },
                                {
                                    "factor": 1,
                                    "code": "H"
                                },
                                {
                                    "factor": 1,
                                    "code": "I"
                                },
                                {
                                    "factor": 1,
                                    "code": "J"
                                },
                                {
                                    "factor": 1,
                                    "code": "K"
                                }
                            ]
                        },
                        {
                            "description": "这是一个目标描述7",
                            "outcomeLinkDTOList": [
                                {
                                    "factor": 1,
                                    "code": "A"
                                },
                                {
                                    "factor": 1,
                                    "code": "B"
                                },
                                {
                                    "factor": 1,
                                    "code": "C"
                                },
                                {
                                    "factor": 1,
                                    "code": "D"
                                },
                                {
                                    "factor": 1,
                                    "code": "E"
                                },
                                {
                                    "factor": 1,
                                    "code": "F"
                                },
                                {
                                    "factor": 1,
                                    "code": "G"
                                },
                                {
                                    "factor": 1,
                                    "code": "H"
                                },
                                {
                                    "factor": 1,
                                    "code": "I"
                                },
                                {
                                    "factor": 1,
                                    "code": "J"
                                },
                                {
                                    "factor": 1,
                                    "code": "K"
                                }
                            ]
                        },
                        {
                            "description": "这是一个目标描述8",
                            "outcomeLinkDTOList": [
                                {
                                    "factor": 1,
                                    "code": "A"
                                },
                                {
                                    "factor": 1,
                                    "code": "B"
                                },
                                {
                                    "factor": 1,
                                    "code": "C"
                                },
                                {
                                    "factor": 1,
                                    "code": "D"
                                },
                                {
                                    "factor": 1,
                                    "code": "E"
                                },
                                {
                                    "factor": 1,
                                    "code": "F"
                                },
                                {
                                    "factor": 1,
                                    "code": "G"
                                },
                                {
                                    "factor": 1,
                                    "code": "H"
                                },
                                {
                                    "factor": 1,
                                    "code": "I"
                                },
                                {
                                    "factor": 1,
                                    "code": "J"
                                },
                                {
                                    "factor": 1,
                                    "code": "K"
                                }
                            ]
                        },
                        {
                            "description": "这是一个目标描述9",
                            "outcomeLinkDTOList": [
                                {
                                    "factor": 1,
                                    "code": "A"
                                },
                                {
                                    "factor": 1,
                                    "code": "B"
                                },
                                {
                                    "factor": 1,
                                    "code": "C"
                                },
                                {
                                    "factor": 1,
                                    "code": "D"
                                },
                                {
                                    "factor": 1,
                                    "code": "E"
                                },
                                {
                                    "factor": 1,
                                    "code": "F"
                                },
                                {
                                    "factor": 1,
                                    "code": "G"
                                },
                                {
                                    "factor": 1,
                                    "code": "H"
                                },
                                {
                                    "factor": 1,
                                    "code": "I"
                                },
                                {
                                    "factor": 1,
                                    "code": "J"
                                },
                                {
                                    "factor": 1,
                                    "code": "K"
                                }
                            ]
                        },
                        {
                            "description": "这是一个目标描述10",
                            "outcomeLinkDTOList": [
                                {
                                    "factor": 1,
                                    "code": "A"
                                },
                                {
                                    "factor": 1,
                                    "code": "B"
                                },
                                {
                                    "factor": 1,
                                    "code": "C"
                                },
                                {
                                    "factor": 1,
                                    "code": "D"
                                },
                                {
                                    "factor": 1,
                                    "code": "E"
                                },
                                {
                                    "factor": 1,
                                    "code": "F"
                                },
                                {
                                    "factor": 1,
                                    "code": "G"
                                },
                                {
                                    "factor": 1,
                                    "code": "H"
                                },
                                {
                                    "factor": 1,
                                    "code": "I"
                                },
                                {
                                    "factor": 1,
                                    "code": "J"
                                },
                                {
                                    "factor": 1,
                                    "code": "K"
                                }
                            ]
                        },
                        {
                            "description": "这是一个目标描述11",
                            "outcomeLinkDTOList": [
                                {
                                    "factor": 1,
                                    "code": "A"
                                },
                                {
                                    "factor": 1,
                                    "code": "B"
                                },
                                {
                                    "factor": 1,
                                    "code": "C"
                                },
                                {
                                    "factor": 1,
                                    "code": "D"
                                },
                                {
                                    "factor": 1,
                                    "code": "E"
                                },
                                {
                                    "factor": 1,
                                    "code": "F"
                                },
                                {
                                    "factor": 1,
                                    "code": "G"
                                },
                                {
                                    "factor": 1,
                                    "code": "H"
                                },
                                {
                                    "factor": 1,
                                    "code": "I"
                                },
                                {
                                    "factor": 1,
                                    "code": "J"
                                },
                                {
                                    "factor": 1,
                                    "code": "K"
                                }
                            ]
                        }
                    ]
                }
            )
            # .extract()
            # .with_jmespath("body.result.linkList[0].id","linkList1")
            # .with_jmespath("body.result.linkList[1].id","linkList2")
            # .with_jmespath("body.result.linkList[2].id","linkList3")
            # .with_jmespath("body.result.linkList[3].id","linkList4")
            # .with_jmespath("body.result.linkList[4].id","linkList5")
            # .with_jmespath("body.result.linkList[5].id","linkList6")
            # .with_jmespath("body.result.linkList[6].id","linkList7")
            # .with_jmespath("body.result.linkList[7].id","linkList8")
            # .with_jmespath("body.result.linkList[8].id","linkList9")
            # .with_jmespath("body.result.linkList[9].id","linkList10")
            # .with_jmespath("body.result.outcomeList[0].id","outcomeList1")
            # .with_jmespath("body.result.outcomeList[1].id","outcomeList2")
            # .with_jmespath("body.result.outcomeList[2].id","outcomeList3")
            # .with_jmespath("body.result.outcomeList[3].id","outcomeList4")
            # .with_jmespath("body.result.outcomeList[4].id","outcomeList5")
            # .with_jmespath("body.result.outcomeList[5].id","outcomeList6")
            # .with_jmespath("body.result.outcomeList[6].id","outcomeList7")
            # .with_jmespath("body.result.outcomeList[7].id","outcomeList8")
            # .with_jmespath("body.result.outcomeList[8].id","outcomeList9")
            # .with_jmespath("body.result.outcomeList[9].id","outcomeList10")
            .validate()
            .assert_equal("status_code", 200)
        )
    ]


if __name__ == "__main__":
    TestCseOBE().test_start()