
from os import supports_bytes_environ
import sqlite3

#data base connection
conn = sqlite3.connect(":memory:")

#cursor
cursor = conn.cursor()

#create table
cursor.execute("CREATE TABLE currency (ID integer primary key, name text, symbol text)")

#insert data currency
cursor.execute("INSERT INTO currency VALUES (1, 'Peso (ARG)', '$' ")
cursor.execute("INSERT INTO currency VALUES (2, 'Dollar (US)', 'US$' ")

#save data
conn.commit()

#query
query = 'SELECT * FROM currency'

#search
currencies = cursor.execute(query).fetchall()

print(currencies)

#close session
conn.close