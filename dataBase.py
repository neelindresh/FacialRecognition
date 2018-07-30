import pymysql
conn=pymysql.connect(host='localhost', user='root', password='', db='face')

cur=conn.cursor()
sql='select * from userinfo;'
cur.execute(sql)
data=cur.fetchall()
for val in data:
    print (val[0])


id=input()

name=input()

gender=input()

assoc=input()
#cur = conn.cursor()
sql = 'insert into userinfo values(%s,%s,%s,%s);'
cur.execute(sql,(id,name,gender,assoc))
conn.commit()