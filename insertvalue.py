import mysql.connector
conn = mysql.connector.connect(host = 'localhost',user='root',password='2005',database='pythondb')
mycursor = conn.cursor()

sql = 'insert into student (name,branch,id) values(%s,%s,%s)'
#val = ('john','cse',56)
 # if user want to create multiple value then you can create list

val = [('anil','cse','56'),('banu','IT','78'),('chandu','me','80')]

#mycursor.executemany(sql,val)
mycursor.executemany(sql,val)
conn.commit()
print(mycursor.rowcount,'record inserted')