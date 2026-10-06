'''import sqlite3
conn=sqlite3.connect('sqldatabase.db')
cur=conn.cursor()
cur.execute('create table if not exists sqldatabase(sid number,sname varchar(20),sphno number)')#1 step
cur.execute(" insert into sqldatabase values(123,'nandhu',72982788728)")#2 step
cur.execute("insert into sqldatabase values(456,'nathiya',89384388378)")#2 step
print('table inserted ')
#res=cur.execute("select * from sqldatabase where sname='nandhu'")#3 step
cur.execute("update sqldatabase set sid=567 where sname='nandhu'")# 4 step
res=cur.execute("select * from sqldatabase where sname='nandhu'")# 5 step
print(res.fetchall()) # after inserted
conn.commit()
conn.close()
'''


#emp table
import sqlite3
conn=sqlite3.connect('sql1.db')
cur=conn.cursor()
cur.execute('create table  if not exists emp(eid number,ename varchar(20),esal number,edepartment varchar(20))')
cur.execute("insert into emp values (325,'arun',6000,'IT')")
cur.execute("insert into emp values(526,'surya',8000,'sales') ")
cur.execute("insert into emp values(728,'chettan',2000,'IT')")
cur.execute("insert into emp values(935,'hemanth',23000,'IT')")
res=cur.execute("select esal from emp where edepartment ='IT'" )
cur.execute(" update emp set esal=10000 where esal=8000")
#print('table created')
#print('table inserted')
conn.commit()
res=cur.execute("select * from emp")
print(res.fetchall())
conn.close()



import mysql.connector
conn=mysql.connector.connect(
    host
