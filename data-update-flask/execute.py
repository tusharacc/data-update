import database as db
import queries as q
from datetime import datetime 

CONN = r'./app-db/data-update.db'

APP_CONN = {
    'app':r'./sample-db/sample.db'
}

def execute_query(id):
    query = (q.query_list['get_query'],(id,))
    result = db.get_data(CONN,query)
    if result['status']:
        #query,num_of_rows,date_submitted,status,date_executed,application
        query = (result['data'][0][0],)
        num_of_rows = result['data'][0][1]
        status = result['data'][0][3]
        application = result['data'][0][5]

        if status == 'SUBMITTED':
            conn_str = APP_CONN[application]
            update_result = db.update_data(conn_str,query,num_of_rows)
            if update_result['status']:
                query = (q.query_list['update_query'],(datetime.now().strftime('%Y-%m-%d'),1,id),)
                querytable_update = db.update_data(CONN,query,1)
            return update_result
        else:
            {'data':None,'status':False,'message':"Query is not in SUBMITTED "}