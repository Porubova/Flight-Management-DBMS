import sqlite3
from utils.colours import *

def create_db():

    print (f"{COLOR_YELLOW}Creating Flight_Management Database...{COLOR_END}")
    print()

    # Open the connection
    conn = sqlite3.connect('Flight_Management')
    sql = open("queries/create_table.sql", "r").read()

    for query in sql.split(";"):
        conn.execute(query)
    conn.commit()

    print (f"{COLOR_YELLOW}Flight_Management Database created successfully!{COLOR_END}")
    print()
    print("************************************************")
    print()

    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' and name !='sqlite_sequence';")
    tables = [table[0] for table in cursor.fetchall()]

    for table in tables:
        rows = str(cursor.execute(f"SELECT COUNT(*) FROM {table}").fetchall()[0][0])
        columns = [i[1] for i in cursor.execute(f"PRAGMA table_info({table})").fetchall()]
        print(f"The table {COLOR_CYAN}{table}{COLOR_END} "
              f"has been created with {COLOR_CYAN}{rows}{COLOR_END} rows and following columns:")
        for column in columns:
           print(column)
        print()

    # Close the connection
    conn.close()

