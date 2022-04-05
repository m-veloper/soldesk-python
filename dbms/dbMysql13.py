import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', password='12345', db='stuser', charset='utf8')
cursor = conn.cursor()

cursor.execute("delete from T_STU_INFO where ST_name='smile'")

conn.commit()
cursor.close()
conn.close()
