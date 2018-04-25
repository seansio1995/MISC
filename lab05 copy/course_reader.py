__author__ = 'Vivian Liu'

import csv
import sqlite3


def load_course_database(db_name, csv_filename):
    conn = sqlite3.connect(db_name)
    with conn:
        cur = conn.cursor()
        with open(csv_filename, 'rU') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                aTuple = tuple(row)
                sql_cmd = "insert into coursedata values(?, ?, ?, ?, ?, ?, ?)"
                cur.execute(sql_cmd, aTuple)

load_course_database("course1.db", "seas-courses-5years.csv")