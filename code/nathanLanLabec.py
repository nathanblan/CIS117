################################################################################
# SQL familiarization and extra credit
# nathanLanLabec.py
# 7.21.2020
################################################################################

import sqlite3

con = sqlite3.connect('lan.db')
cur = con.cursor()

def create_table():
    cur.execute("""CREATE TABLE IF NOT EXISTS
                PopByRegion(Region TEXT, Population INTEGER)""")

def data_entry(Region, Population):
    #Add single rows of entrys
    cur.execute("INSERT INTO PopByRegion (Region, Population) VALUES (?, ?)",
                (Region, Population))
    con.commit()
    
create_table()
data_entry('Central Africa', 330993)
data_entry('Southeastern Africa', 743112)
data_entry('Japan', 100562)

#run
'''
================ RESTART: D:\05CSM\CIS117\code\nathanLanLabec.py ===============
>>> cur.execute('SELECT Region, Population FROM PopByRegion')
<sqlite3.Cursor object at 0x0137BEE0>
>>> cur.fetchall()
[('Central Africa', 330993), ('Central Africa', 330993), ('Central Africa', 330993), ('Southeastern Africa', 743112), ('Japan', 100562), ('Central Africa', 330993), ('Southeastern Africa', 743112), ('Japan', 100562), ('Central Africa', 330993), ('Southeastern Africa', 743112), ('Japan', 100562)]
>>> cur.execute('SELECT Region, Population FROM PopByRegion ORDER by Region')
<sqlite3.Cursor object at 0x0137BEE0>
>>> cur.fetchall()
[('Central Africa', 330993), ('Central Africa', 330993), ('Central Africa', 330993), ('Central Africa', 330993), ('Central Africa', 330993), ('Japan', 100562), ('Japan', 100562), ('Japan', 100562), ('Southeastern Africa', 743112), ('Southeastern Africa', 743112), ('Southeastern Africa', 743112)]
>>> cur.execute('SELECT Region FROM PopByRegion')
<sqlite3.Cursor object at 0x0137BEE0>
>>> cur.fetchall()
[('Central Africa',), ('Central Africa',), ('Central Africa',), ('Southeastern Africa',), ('Japan',), ('Central Africa',), ('Southeastern Africa',), ('Japan',), ('Central Africa',), ('Southeastern Africa',), ('Japan',)]
>>> cur.execute ('SELECT Region FROM PopByRegion WHERE Population > 400000')
<sqlite3.Cursor object at 0x0137BEE0>
>>> cur.fetchall()
[('Southeastern Africa',), ('Southeastern Africa',), ('Southeastern Africa',)]
>>> cur.execute('SELECT * FROM PopByRegion WHERE Region = "Japan"')
<sqlite3.Cursor object at 0x0137BEE0>
>>> cur.fetchone()
('Japan', 100562)
>>> cur.execute('UPDATE PopByRegion SET Population = 100600 WHERE Region = "Japan"')
<sqlite3.Cursor object at 0x0137BEE0>
>>> cur.execute('SELECT * FROM PopByRegion WHERE Region = "Japan"')
<sqlite3.Cursor object at 0x0137BEE0>
>>> cur.fetchone()
('Japan', 100600)
>>> cur.execute('DELETE FROM PopByRegion WHERE Region < "S"')
<sqlite3.Cursor object at 0x0137BEE0>
>>> cur.execute('SELECT * FROM PopByRegion')
<sqlite3.Cursor object at 0x0137BEE0>
>>> cur.fetchall()
[('Southeastern Africa', 743112), ('Southeastern Africa', 743112), ('Southeastern Africa', 743112)]
>>> cur.close()
>>> con.close()
'''
