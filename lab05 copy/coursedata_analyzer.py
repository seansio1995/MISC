__author__ = 'Vivain Liu'

import sqlite3

def instructor_numbers(dept_id):
    dict = {}
    conn = sqlite3.connect("course1.db")
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT seatsTaken, instructor FROM coursedata WHERE deptID =\"dept_id\"")
        rows = cur.fetchall()
        students = rows[0]
        instructors = rows[1]
        for line in rows:
            if instructors in dict:
                dict[instructors] += students
            else:
                dict[instructors] = students

