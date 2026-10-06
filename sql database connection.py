import sqlite3
conn=sqlite3.connect('lambda.db')
cur=conn.cursor()
cur.execute('create table  lambda(sid number,sname varchar(20),sphno  number)')
print('table created ')
conn.commit()
conn.close()
