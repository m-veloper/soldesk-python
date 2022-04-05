import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', password='12345', db='stuser', charset='utf8')
cursor = conn.cursor()

cursor.execute(
    "create table T_STU_INFO(ST_name char(32), ST_code char(32), ST_MAJ char(32), ST_GRA char(32), ST_PHO char(32))")

cursor.close()
conn.close()
