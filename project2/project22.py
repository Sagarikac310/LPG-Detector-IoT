import sqlite3
import time
import datetime
import random
import csv

conn = sqlite3.connect('pro2.db')
c = conn.cursor()
print ("Done")

c.execute("CREATE TABLE IF NOT EXISTS project('value' REAL,'situation' REAL, 'datestamp' REAL)")

count = 0
    #cursor.execute('INSERT INTO \'daily_new\' (date, cust_bal, cust_credit, fund_stock, fund_hyb, fund_bond ) VALUES({}, {}, {}, {}, {}, {})'.format(row[0], row[1], row[2], row[3], row[4], row[5]))
with open('project2.csv','r') as infile:
    dr = csv.reader(infile,delimiter=',')
    for x in dr:
        value = x[0]
        situation = x[1]
        time = count
        print ("Done")
        c.execute("INSERT INTO project(value,situation,datestamp) VALUES(?,?,?)",(value,situation,time))
        count = count + 0.5
        conn.commit()

c.close()
conn.close()
