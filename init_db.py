import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO users (name, hash, larder) VALUES (?, ?, ?)",
            ('First User ', 'xxx', 'tobasco')
            )

connection.commit()
connection.close()
