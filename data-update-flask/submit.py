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
def submit_query(query,num_of_rows,user_id,app):
    print ("Received the request",query)
    date_submitted = datetime.now().strftime('%Y-%m-%d')
    status = 'SUBMITTED'
    query = (q.query_list['insert_query'],(query,num_of_rows,user_id,app,date_submitted, status))
    result = db.insert_data(CONN,query)
    print ("The result is", result)
    return result
