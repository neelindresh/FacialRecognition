def getDetails(id):
    conn = pymysql.connect(host='localhost', user='root', password='', db='face')

    cur = conn.cursor()
    sql = 'select * from userinfo where id=%s;'
    cur.execute(sql,id)
    data = cur.fetchall()
    list=[]
    for val in data:
        print(type(val))
return data
