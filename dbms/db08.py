import sqlite3

# 변수
con, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
sql = ""

con = sqlite3.connect("E:/Python/sqlite/soldesk")
cur = con.cursor()

ch = int(input("<입력>:1, <출력>:2 를 입력하세요 : "))

if ch == 1:
    while (True):
        data1 = input("사용자 ID ==> ")
        if data1 == "":
            break
        data2 = input("사용자 이름 ==> ")
        data3 = input("사용자 이메일 ==> ")
        data4 = input("사용자 출생연도 ==> ")
        sql = "insert into userTable values('" + data1 + "','" + data2 + "','" + data3 + "'," + data4 + ")"
        cur.execute(sql)
elif ch == 2:
    cur.execute("select * from userTable")
    print("사용자ID     사용자이름     이메일            출생연도")
    print("--------------------------------------------------------")
    while (True):
        row = cur.fetchone()
        if row == None:
            break
        data1 = row[0]
        data2 = row[1]
        data3 = row[2]
        data4 = row[3]
        print("%7s %15s  %15s  %5s" % (data1, data2, data3, data4))

con.commit()
con.close()
