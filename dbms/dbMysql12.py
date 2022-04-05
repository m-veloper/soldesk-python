import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', password='12345', db='stuser', charset='utf8')
cursor = conn.cursor()

cursor.execute("update T_STU_INFO set ST_PHO='010-555-5555' where ST_NAME='smile'")

conn.commit()
cursor.close()
conn.close()
