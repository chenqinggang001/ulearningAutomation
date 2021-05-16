# NOTE: Generated By HttpRunner v3.1.4
# FROM: har\test.har


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseTest(HttpRunner):

    config = Config("testcase description").verify(False)

    teststeps = [
        Step(
            RunRequest("/obe/textbookOutcome")
            .post("http://courseapi.tongshike.cn/obe/textbookOutcome")
            .with_params(**{"textbookId": "9674", "ocId": "33834"})
            .with_headers(
                **{
                    "Content-Type": "application/json",
                    "Authorization": "DA97110685B1E8FEDED6E2954C08A15F",
                    "User-Agent": "PostmanRuntime/7.26.8",
                    "Accept": "*/*",
                    "Cache-Control": "no-cache",
                    "Postman-Token": "d0dc6211-e83e-4693-9a8f-ac737a19939b",
                    "Host": "courseapi.tongshike.cn",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Connection": "keep-alive",
                    "Content-Length": "94",
                }
            )
            .with_json(
                [
                    {"itemId": "374725", "outcomeId": "1390"},
                    {"itemId": "1235673", "outcomeId": "1391"},
                ]
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.code", 1)
            .assert_equal("body.message", "成功")
        ),
    ]


if __name__ == "__main__":
    TestCaseTest().test_start()