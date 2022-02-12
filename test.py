
import sqlite3
con = sqlite3.connect('student.db', check_same_thread=False)
c = con.cursor()
for row in c.execute('SELECT * FROM prefrence'):
        print(row)

# username = 'vedp'
# c.execute("DELETE FROM studentd")
# c.execute("DELETE FROM prefrence")
# con.commit()
for row in c.execute('SELECT * FROM studentd'):
        print(row)
# con.close()
# # password= '7898'
# print(c.execute("SELECT * FROM studentd"))
# print(c.fetchall())