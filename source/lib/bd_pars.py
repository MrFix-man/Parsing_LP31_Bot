import sqlite3

con = sqlite3.connect('mydata.db')

sql = 'CREATE TABLE ads (id INT, rooms INT, area FLOAT, price INT, address TEXT, district TEXT, floor INT, url TEXT, type TEXT)'

cursor = con.cursor()

cursor.execute(sql)

con.close()
