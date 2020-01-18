import sqlite3

# conn = sqlite3.connect('users.db')
conn = sqlite3.connect('payments.db')

c = conn.cursor()
# c.execute("CREATE TABLE bookings_for_national( fname text not null, lname text not null, email text not null, phnumber text not null,source text not null,destination text not null,modeoftransport text not null, tickets_required text not null)")
# c.execute(""" CREATE TABLE users1(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# pickup TEXT NOT NULL,
# dropp TEXT NOT NULL,
# modeoftransport TEXT NOT NULL,
# price REAL NOT NULL
# ) """)
# c.execute(""" CREATE TABLE login(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# username TEXT NOT NULL,
# password TEXT NOT NULL
# ) """)
# c.execute("INSERT INTO users VALUES(5,'Hyderabad','Chennai','Bus',7.99,8)")
# c.execute("INSERT INTO users1 VALUES(16,'Banjara Hills','Secunderabad','Cab',130)")

# c.execute("INSERT INTO login VALUES(1,'easyTravel','PYFIVE5')")

# c.execute("SELECT * FROM users")
# c.execute("SELECT * FROM users1")
c.execute("INSERT INTO bookings_for_national VALUES('Snikitha', 'Siddavatam', 'snikithasiddavatam@gmail.com', '9666697782', 'Hyderabad', 'Delhi', 'Flight', '2')")

c.execute("SELECT * FROM bookings_for_national")

print(c.fetchall())

conn.commit()

conn.close()