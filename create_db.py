import sqlite3


def create_db():
    con = sqlite3.connect("LMS Project.db")
    cur = con.cursor()
    # Create table if it doesn't exist, all TEXT fields
    cur.execute("""
        CREATE TABLE IF NOT EXISTS course (
            course_name TEXT,
            teacher_name TEXT,
            course_code TEXT,
            shift TEXT
        )
    """)
    con.commit()
    con.close()


create_db()