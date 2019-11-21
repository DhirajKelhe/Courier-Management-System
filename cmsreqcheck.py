import sqlite3

conn = sqlite3.connect('cmsreq.db')

#conn.execute('truncate table cmsuser')
#conn.commit()

cursor = conn.execute('select * from cmsreq')

#print(cursor)
for row in cursor:
    print('username: ',row[0]) 
    print('regno: ', row[1])
    print('mobile: ', row[2])
    print('to: ', row[3])
    print('weight: ', row[4])
    print('distance: ', row[5])
    print('deltype: ', row[6])
    print('Consignment number: ', row[7], '\n')

conn.close()