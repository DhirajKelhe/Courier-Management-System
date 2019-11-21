import sqlite3 as sq

conn = sq.connect('cmsuser.db') #creates file
conn.execute('''Create table if not exists cmsuser
        (username char(20) not null,
        regno number(8) not null,
        gender char(6) not null,
        mobile number(10) not null,
        email char(25) not null,
        password varchar(25) not null);''')

print('Table Created Successfully')
conn.close()