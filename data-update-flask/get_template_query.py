import queries as q
import database as db

CONN = r'./app-db/data-update.db'

def get_template_queries(user_id):
    query =(q.query_list['get_template_query'],(user_id,))
    result = db.get_data('sqlite',CONN,query)
    if result['status']:
        records = []
        for item in result['data']:
            records.append({"query_name": item[0],"query": item[1],"updated_columns": eval(item[2]),"where_columns": eval(item[3]),"application": item[4],"db": item[5]})
    return {"data":records,'status':result['status'], "message":result['message']}