import sqlite3

conn = sqlite3.connect('cmsfeed.db')
cursor = conn.execute('select * from cmsfeed')

#print(cursor)
for row in cursor:
    print('Email: ',row[0], end = '\n') 
    print('Feedback: ', row[1])

conn.close()