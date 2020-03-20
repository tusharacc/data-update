import database as db
import queries as q

CONN = r'./app-db/data-update.db'

def get_queries(userid):
    query = (q.query_list['get_queries'],(userid,))
    result = db.get_data('sqlite',CONN,query)
    records = []
    for item in result['data']:
        #query,num_of_rows,date_submitted,status,date_executed,application
        records.append({"query": item[0], "num_of_rows": item[1], "date_submitted": item[2],"status": item[3], "date_executed": item[4],"application": item[5]})
    return {'data': records, 'status': result['status'], 'message': result['message']}

if __name__ == '__main__':
    print (get_queries('user_1'))