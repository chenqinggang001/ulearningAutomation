        Step(
            RunRequest("新建OBE设置信息")
            .post("/obe")
            .with_headers(**{"Content-Type": "application/json","Authorization":"$authorization"})
            .with_json(
                {
                    "id": 7,
                    "ocId": "$ocid",
                    "passScore": 0.7,
                    "linkList": [
                        {
                            "name": "考核环节1"
                        },
                        {
                            "name": "考核环节2"
                        },
                        {
                            "name": "考核环节3"
                        }
                    ],
                    "outcomeList": [
                        {
                            "description": "这是一个目标描述1",
                            "outcomeLinkDTOList": [
                                {
                                    "factor": 5,
                                    "code": "A"
                                },
                                {
                                    "factor": 10,
                                    "code": "B"
                                }
                            ]
                        },
                        {
                            "description": "这是一个目标描述2",
                            "outcomeLinkDTOList": [
                                {
                                    "factor": 10,
                                    "code": "A"
                                },
                                {
                                    "factor": 30,
                                    "code": "C"
                                }
                            ]
                        },
                        {
                            "description": "这是一个目标描述3",
                            "outcomeLinkDTOList": [
                                {
                                    "factor": 5,
                                    "code": "A"
                                },
                                {
                                    "factor": 20,
                                    "code": "B"
                                },
                                {
                                    "factor": 20,
                                    "code": "C"
                                }
                            ]
                        }
                    ]
                }
            )