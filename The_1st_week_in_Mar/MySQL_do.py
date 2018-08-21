# 导入MySQL驱动
import mysql.connector

# password未root用户的密码
coon = mysql.connector.connect(user='root', password='password', database='test')
# cursor = coon.cursor()
# user表已创建，所以本程序仅做查询用
# cursor.execute('create a table (id varchar(20) primary key, name varchar(20))')
# cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'William'])
# print(cursor.rowcount)
# coon.commit()
# cursor.close()

cursor = coon.cursor()
# 运行查询
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
# 关闭cursor和connection
cursor.close()
coon.close()
