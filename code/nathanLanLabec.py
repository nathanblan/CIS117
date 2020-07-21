import sqlite3

con = sqlite3.connect('yourlastname.db')

cur = con.cursor()

cur.execute('SELECT Region, Population FROM PopByRegion')

cur.fetchall()

cur.execute('SELECT Region, Population FROM PopByRegion ORDER by Region')
cur.fetchall()

cur.execute('SELECT Region FROM PopByRegion')

cur.fetchall()

cur.execute ('SELECT Region FROM PopByRegion WHERE Population > 400000')

cur.fetchall()

cur.execute('SELECT * FROM PopByRegion WHERE Region = "Japan"')

cur.fetchone()

cur.execute('''UPDATE PopByRegion SET Population = 100600 WHERE Region = "Japan"''')

cur.execute('SELECT * FROM PopByRegion WHERE Region = "Japan"')

cur.fetchone()

cur.execute('DELETE FROM PopByRegion WHERE Region < "S"')

cur.execute('SELECT * FROM PopByRegion')

cur.fetchall()

cur.close()

con.close()
