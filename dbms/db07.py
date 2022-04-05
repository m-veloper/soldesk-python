import sqlite3

# 변수
con, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
sql = ""

con = sqlite3.connect("E:/Python/sqlite/soldesk")
cur = con.cursor()

cur.execute("select * from userTable")

print("사용자ID     사용자이름     이메일               출생연도")
print("--------------------------------------------------------")
while (True):
    row = cur.fetchone()  # 한줄
    if row == None:
        break
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    print("%7s %12s  %15s %5s" % (data1, data2, data3, data4))

con.commit()
con.close()
