import sqlite3

conn = sqlite3.connect('cmsuser.db')

#conn.execute('truncate table cmsuser')
#conn.commit()

cursor = conn.execute('select * from cmsuser')

#print(cursor)
for row in cursor:
    print('username: ',row[0]) 
    print('regno: ', row[1])
    print('gender: ', row[2])
    print('phone: ', row[3])
    print('email: ', row[4])
    print('password: ', row[5], '\n')

conn.close()