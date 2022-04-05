import sqlite3

con = sqlite3.connect("E:/Python/sqlite/soldesk")
cur = con.cursor()

cur.execute(
    "insert into T_STU_INFO(ST_name, ST_code, ST_MAJ, ST_GRA, ST_PHO) values('smile','160321','SW','4','010-111-1111')")
id = cur.lastrowid  # 튜플의 수 반환
print(id)

cur.execute(
    "insert into T_STU_INFO(ST_name, ST_code, ST_MAJ, ST_GRA, ST_PHO) values('parksu','150820','SW','2','010-333-1111')")
id = cur.lastrowid  # 튜플의 수 반환
print(id)

cur.execute(
    "insert into T_STU_INFO(ST_name, ST_code, ST_MAJ, ST_GRA, ST_PHO) values('kimchi','180320','Secure','3','010-222-1111')")
id = cur.lastrowid  # 튜플의 수 반환
print(id)

con.commit()
cur.close()
con.close()
