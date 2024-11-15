import sqlite3

# Establish a connection and cursor
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# Query all data based ona condition
cursor.execute("SELECT * FROM events WHERE date='2088.10.15'")
rows = cursor.fetchall()
print(rows)

# Query certain columns based on a condition
cursor.execute("SELECT band, date FROM events WHERE date='2088.10.15'")
rows = cursor.fetchall()
print(rows)

# Insert new rows
new_rows = [('Cats', 'Cats city', '2088.10.17'),
            ('Hens', 'Hens city', '2088.10.17'),
            ('Lions', 'Lions city', '2088.10.16')]

cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
connection.commit()

# Query all data.
cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)