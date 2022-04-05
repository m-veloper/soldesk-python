import sqlite3

con = sqlite3.connect("E:/Python/sqlite/soldesk")
cur = con.cursor()

cur.execute("drop table T_STU_INFO")
cur.execute(
    "create table T_STU_INFO(ST_name char(32), ST_code char(32), ST_MAJ char(32), ST_GRA char(32), ST_PHO char(32))")

cur.close()
con.close()
