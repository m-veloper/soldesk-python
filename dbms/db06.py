import sqlite3

# 변수
con, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
sql = ""

con = sqlite3.connect("E:/Python/sqlite/soldesk")
cur = con.cursor()

while (True):
    data1 = input("사용자 ID ==> ")
    if data1 == "":
        break
    data2 = input("사용자 이름 ==>")
    data3 = input("사용자 이메일 ==>")
    data4 = input("사용자 출생연도 ==>")
    sql = "insert into userTable values('" + data1 + "','" + data2 + "','" + data3 + "'," + data4 + ")"
    cur.execute(sql)

con.commit()
con.close()
