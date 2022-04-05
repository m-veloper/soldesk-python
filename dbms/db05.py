import sqlite3

con = sqlite3.connect("E:/Python/sqlite/soldesk")
cur = con.cursor()
# 테이블 생성
cur.execute("drop table userTable")
cur.execute("create table userTable(id char(4), userName char(20), email char(20), birthYear int(15))")

# 입력
cur.execute("insert into userTable(id , userName , email , birthYear) values('sul', 'Back Sul', 'sul@naver.com', 2018)")
cur.execute("insert into userTable(id , userName , email , birthYear) values('desk', 'Sol Desk', 'desk@sol.com', 2000)")
cur.execute(
    "insert into userTable(id , userName , email , birthYear) values('smile', 'Smile516', 'smile@smile.com', 2012)")
# 삭제
cur.execute("delete from userTable where id='desk'")
# 검색
cur.execute("select * from userTable")
rows = cur.fetchall()
for r in rows:
    print('{0},{1},{2},{3}'.format(r[0], r[1], r[2], r[3]))
cur.close()
con.close()
