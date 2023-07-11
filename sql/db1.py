import sqlite3
conn=sqlite3.connect('my_friends.db')

c=conn.cursor()
c.execute("select * from friends where first_name='Steve';")
r=c.fetchall()
print(r)

conn.commit()
conn.close()