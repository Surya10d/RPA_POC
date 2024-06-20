import sqlite3
from datetime import datetime
import os

# Define database name
if os.name == 'nt':
    DB_NAME = os.path.dirname(__file__)+'\\children_agency.db'
else:
    DB_NAME = os.path.dirname(__file__) + '/children_agency.db'


def create_connection(db_name):
    """ Create a database connection to the SQLite database """
    conn = sqlite3.connect(db_name)
    return conn


def create_table(conn):
    """ Create the children table if it doesn't exist """
    create_table_sql = '''
    CREATE TABLE IF NOT EXISTS children (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        agency_name TEXT NOT NULL,
        state_name TEXT NOT NULL,
        child_detail TEXT NOT NULL,
        posted_on TEXT NOT NULL
    );
    '''
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def check_table_exists(conn, table_name):
    """ Check if a table exists in the database """
    check_table_sql = '''
    SELECT name FROM sqlite_master WHERE type='table' AND name=?;
    '''
    c = conn.cursor()
    c.execute(check_table_sql, (table_name,))
    return c.fetchone() is not None


def insert_data(conn, data):
    """ Insert a new row into the children table """
    insert_sql = '''
    INSERT INTO children (agency_name, state_name, child_detail, posted_on)
    VALUES (?, ?, ?, ?);
    '''
    try:
        c = conn.cursor()
        c.execute(insert_sql, data)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def read_data(conn):
    """ Query all rows in the children table """
    read_sql = '''
    SELECT * FROM children;
    '''
    c = conn.cursor()
    c.execute(read_sql)
    rows = c.fetchall()
    return rows


def check_and_get_details(data):
    # Create a database connection
    conn = create_connection(DB_NAME)

    # Check if the table exists, if not, create it
    if not check_table_exists(conn, 'children'):
        create_table(conn)

    data = data.replace("'", "").split("Reserve Child")[1:]

    child_data = []
    for i in data:
        if i == '':
            continue
        agency_name = i.split("\n")[1]
        state_name = i.split("\n")[2]
        child_detail = i.split("\n")[4].replace(" View", "")
        child_data.append([agency_name, state_name, child_detail, datetime.now().strftime('%Y-%m-%d %H:%M:%S')])

    # Read all data from the table
    all_rows = read_data(conn)
    all_child_data = []
    if all_rows:
        for row in all_rows:
            all_child_data.append(list(row[1:4]))

    flag = 0

    for j in child_data:
        if str(j[:3]) not in str(all_child_data):
            flag = 1
            # Insert new data
            insert_data(conn, j)
    # Close the connection
    conn.close()

    if flag == 1:
        return True
    else:
        return False


if __name__ == '__main__':
    pass
