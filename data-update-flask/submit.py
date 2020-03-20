import database as db
import queries as q
from datetime import datetime

CONN = r'./app-db/data-update.db'

'''
Input;
    query: Query to be submitted for execution
    num_of_rows: Number of rows impacted
    user_id: User who submitted the query
    app: Application for which query is intended

Output:
    Dictionary with keys => data (none), Status Ok or Failure, message = 
        
'''
#update_query,select_query,num_of_rows,user_id,app,db_name
def submit_query(update_query,select_query,num_of_rows,user_id,app,db_name):
    print ("Received the request",update_query)
    date_submitted = datetime.now().strftime('%Y-%m-%d')
    status = 'SUBMITTED'
    query = (q.query_list['insert_query'],(update_query,select_query,num_of_rows,user_id,app, db_name ,date_submitted, status))
    result = db.insert_data('sqlite',CONN,query)
    print ("The result is", result)
    return result
