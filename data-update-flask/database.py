import sqlite3

def __connect_to_db(cn):
    return sqlite3.connect(cn)

def __close_conn(conn):
    conn.close()

def get_data(cn,query):
    status = True
    data = None
    message = None
    conn = None
    try:
        conn = __connect_to_db(cn)
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

def insert_data(cn, query):
    status = True
    data = None
    message = None
    conn = None
    try:
        conn = __connect_to_db(cn)
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

def update_data(cn,query,num_of_rows):
    status = True
    data = None
    message = None
    conn = None
    try:
        conn = __connect_to_db(cn)
        print ("Update Query is",query)
        cur = conn.cursor()
        cur.execute(*query)
        if num_of_rows == cur.rowcount:
            print ("Row updated Expected")
            conn.commit()
        else:
            conn.rollback()
            status = False
            message = f"The query is updating {cur.rowcount} records instead of {num_of_rows}"
    except Exception as ex:
        status = False
        data = None
        message = ex
    finally:
        __close_conn(conn)
    print (str(status), str(message))
    return {'data':data,'status':status,'message':message}