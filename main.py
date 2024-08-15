import sqlite3

con = sqlite3.connect("data.db")

cursor = con.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS name_table
                (id INTEGER PRIMARY KEY AUTOINCREMENT,  
                name TEXT, 
                age INTEGER DEFAULT 0)
            """)

cursor.execute("INSERT INTO name_table (name, age) VALUES ('Tom', 38), ('Bob', 41), ('Sam', 28)")
con.commit()

#cursor.execute('SELECT * FROM name_table')
#print(cursor.fetchall())
#cursor.execute('SELECT id FROM name_table')
#print(cursor.fetchall())
#cursor.execute('SELECT id, name FROM name_table')
#print(cursor.fetchall())
#

cursor.execute("SELECT AVG(age) FROM name_table")
print(cursor.fetchall())


