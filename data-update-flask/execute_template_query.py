import database as db
import queries as  q
import config
import connection as cn

CONN = r'./app-db/data-update.db'

def execute_query(incoming_query, query_name, app, db_name):
    query = (q.query_list['get_updated_row'],(query_name,))
    result = db.get_data('sqlite',CONN,query)
    if result['status']:
        conn_str = cn.get_connection(app,db_name)
        update_result = db.update_data(config.get_sql_type('database'),conn_str,(incoming_query,),result['data'][0]['expected_rows'])
        return update_result
    else:
        return {'data':None,'status':False,'message':'Invalid Query Name'}