
import sqlite3
import pyodbc

def __connect_to_db(sql_type,cn):
    if sql_type == 'sqlite':
        return sqlite3.connect(cn)
    elif sql_type == 'sql-server':
        return pyodbc.connect(cn)
    

def __close_conn(conn):
    conn.close()

def get_data(type,cn,query):
    print ("The SQL Dest is", type)
    status = True
    data = None
    message = None
    conn = None
    try:
        conn = __connect_to_db(type,cn)
        if type == 'sqlite':
            conn.row_factory = sqlite3.Row

        cursor = conn.execute(*query)
        records = cursor.fetchall()
        print ("The records returned are",records)
        data = records
    except Exception as ex:
        status = False
        data = None
        message = ex
    finally:
        __close_conn(conn)
    
    return {'data':data,'status':status,'message':message}

def insert_data(type,cn, query):
    status = True
    data = None
    message = None
    conn = None
    try:
        conn = __connect_to_db(type,cn)
        print (query)
        conn.execute(*query)
        conn.commit()
    except Exception as ex:
        status = False
        data = None
        message = ex
    finally:
        __close_conn(conn)

    return {'data':data,'status':status,'message':message}

def update_data(type,cn,query,num_of_rows):
    status = True
    data = None
    message = None
    conn = None
    try:
        conn = __connect_to_db(type,cn)
        print ("database.py: Update Query is",query)
        cur = conn.cursor()
        cur.execute(*query)
        if num_of_rows == cur.rowcount:
            data = cur.rowcount
            print ("database.py: Row updated Expected")
            conn.commit()
        else:
            data = cur.rowcount
            conn.rollback()
            status = False
            message = f"database.py: The query is updating {cur.rowcount} records instead of {num_of_rows}"
    except Exception as ex:
        status = False
        data = None
        message = ex
    finally:
        __close_conn(conn)
    print (str(status), str(message))
    return {'data':data,'status':status,'message':message}