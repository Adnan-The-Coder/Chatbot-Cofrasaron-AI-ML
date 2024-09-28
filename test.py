import mysql.connector as mys

con = mys.connect(host='localhost',user='root',passwd='9801!adnan',database='testing')
if con.is_connected():
    print('Data connected...')
    print()

mycur = con.cursor()

# data = mycur.execute("show databases")
# data = mycur.execute("create table stu(name varchar(20),rno INT)")
cmd = mycur.execute("desc stu")

data = cmd.fetchall()

for i in data:
    print(i)