import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', password='12345', db='stuser', charset='utf8')
cursor = conn.cursor()

cursor.execute(
    "insert into T_STU_INFO(ST_name, ST_code, ST_MAJ, ST_GRA, ST_PHO) values('smile','160320','Secure','4','010-111-1111')")
cursor.execute(
    "insert into T_STU_INFO(ST_name, ST_code, ST_MAJ, ST_GRA, ST_PHO) values('parksu','151120','SW','2','010-222-1111')")
cursor.execute(
    "insert into T_STU_INFO(ST_name, ST_code, ST_MAJ, ST_GRA, ST_PHO) values('kimchi','180310','SW','3','010-333-1111')")

conn.commit()
cursor.close()
conn.close()
