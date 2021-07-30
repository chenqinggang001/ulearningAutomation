import pymysql

# 数据连接信息:数据库对应的接口地址

DBCONFIG = {
    "host": "119.3.253.124",
    "port": 3306,
    "user": "ulearningdb",
    "password": "ulearning_2015",
    "db": "ulearningdb"
}


def query(sql):
    """
        方法：连接并且操作mysql数据库
        参数：sql: "select * from t_user where id=123"
        返回值： 
            ((id, username, password...), (id2, username2, passwor2,...))
    """
    # 步骤1：连接并且打开对应的数据库
    db = pymysql.connect(host=DBCONFIG["host"], 
                         port=DBCONFIG["port"],
                         user=DBCONFIG["user"], 
                         password=DBCONFIG["password"], 
                         db=DBCONFIG["db"]
                        )
    # 步骤2：获取查询的窗口：游标
    cur = db.cursor()
    # 步骤3：执行sql语句
    cur.execute(sql)
    # 步骤4：获取对应的结果
    res = cur.fetchall()
    # 步骤5：关闭数据库连接
    db.close()

    return res


# 测试方法是否通过，注释代码
sql = "select userid,loginname,password,name from u_user_tab where loginName='chenqinggangtea'"
a = query(sql)
print(a)
# print(len(a))
