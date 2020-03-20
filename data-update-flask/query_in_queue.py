#!usr/bin/python3
import database as db
import queries as q
import verify as ver

CONN = r'./app-db/data-update.db'

def get_query_in_queue(executor_user):
    query = (q.query_list['query_queue'],(executor_user,))
    result = db.get_data('sqlite',CONN,query)
    print (result)
    records = []
    if result['status']:
        #a.id, a.query, a.num_of_row,a.application,a.user_id
        for item in result['data']:
            print ("Processing Record", item)
            select_query = item[2]
            db_name = item[5]
            app_name = item[4]
            result = ver.get_number_of_rows(select_query,app_name,db_name)
            if result['status']:
                current_rows =  result['data']
            #current_rows =  0

            #a.id, a.query, a.select_query,a.num_of_rows,a.application,a.database,a.user_id
            records.append({"id":item[0],"update_query":item[1],"num_of_rows": item[3],"current_rows":current_rows,"application": item[4], "user": item[6]})
        
    return {"data":records,"status":result['status'],"message":result['message']}

if __name__ == '__main__':
    print (get_query_in_queue('user_3'))