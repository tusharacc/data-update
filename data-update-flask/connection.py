import config

#Driver=SQLite3 ODBC Driver;Database=sqlite.db
#Driver=


def get_connection(application, database):
    sql_type = config.get_sql_type('database')
    if sql_type == 'sql-server':
        sql_server = config.get_value('server',application)
        user_id = config.get_value(application,'userid')
        password = config.get_value(application,'password')
        conn = f"Driver={{ODBC Driver 11 for SQL Server}};Server={sql_server};Database={database};UID={user_id};PWD={password};"
    elif sql_type == 'sqlite':
        database_addr = config.get_value('server',application)
        conn = f"Driver=SQLite3 ODBC Driver;Database={database_addr}"

    return conn