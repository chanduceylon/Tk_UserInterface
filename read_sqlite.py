import sqlite3
import numpy as np

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

conn = sqlite3.connect('mux.db')
conn.row_factory = dict_factory
    #sqlite3.Row

cur = conn.cursor()
cur.execute('select out from mux WHERE out=40')
pinout=cur.fetchone()

cur.execute('select A0, A1, A2, A3, A4, CS1, CS2, CS3 from mux ')
row = cur.fetchone()


print(pinout)
print(row)
print


# cur.execute("select 1 as A")
# print(cur.fetchone()['A'])

