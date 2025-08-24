import sqlite3
def create_db():
    con = sqlite3.connect("LMS Project.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT, name text , duration text,charges text,description text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS student(roll INTEGER PRIMARY KEY AUTOINCREMENT, name text , email text , gender text,dob text , contact text, admission text , course text , state text , city text , pin text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY AUTOINCREMENT, roll text , name text , course text , marks_ob text , full_mark text ,per text)")
    con.commit()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users(
            Cid INTEGER PRIMARY KEY AUTOINCREMENT,
            f_name TEXT NOT NULL,
            l_name TEXT NOT NULL,
            contact TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)

    con.commit()
    con.close()
    print("✅ Database and 'users' table created successfully!")


create_db()