import sqlite3 as sq

conn = sq.connect('cmsfeed.db') #creates file
conn.execute('''Create table if not exists cmsfeed
        (email char(25) not null,
        feedback char(500) not null);''')

print('Table Created Successfully')
conn.close()