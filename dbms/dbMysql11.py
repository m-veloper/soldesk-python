import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', password='12345', db='stuser', charset='utf8')
cursor = conn.cursor()

cursor.execute("select * from T_STU_INFO")

rows = cursor.fetchall()
for r in rows:
    print('ST_name:{0}, ST_code:{1}, ST_MAJ:{2}, ST_GRA:{3}, ST_PHO:{4}'.format(r[0], r[1], r[2], r[3], r[4]))

cursor.close()
conn.close()
