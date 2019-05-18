import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table_users = "create table if not exists users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table_users)

create_table_items = "create table if not exists items (id INTEGER PRIMARY KEY, name text, price real)"
cursor.execute(create_table_items)

connection.commit()
connection.close()
