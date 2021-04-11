# 返回状态==200
.assert_equal("status_code", 200)
# 返回的code值==0
.assert_not_equal("body.code", 0)

# 返回的header的content-type值是application/json;charset=UTF-8
.assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")

# body中folderid的值==0
.assert_equal("body.data.folderid", 0)

# folders的数量大于等于5
.assert_length_equal("body.data.folders", 5)
.assert_greater_than("body.data.folders", 5)
.assert_length_greater_or_equals("body.data.folders", 5)

# jmespath中的值包含abc
.assert_contained_by("body.data.map", "adc")
# jmespath中的值长度==5
.assert_length_equal("body.data.m", 5)

# jmespath中的值以message字符串结尾、开始
.assert_endswith("body.data.m", "message")
.assert_startswith("body.data.m", "message")


mailcli -u "1304085583@qq.com" -p "gxxacyfysvgtfgge" --mail-sender "smtp.exmail.qq.com" --mail-recepients chenqinggang@ulearning.cn --mail-subject subject-test --mail-content helloworld


mailcli -u "1304085583@qq.com" -p "gxxacyfysvgtfgge" --mail-sender "smtp.exmail.qq.com" --mail-recepients chenqinggang@ulearning.cn --mail-subject subject-test --mail-content helloworld