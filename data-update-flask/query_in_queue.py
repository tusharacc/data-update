#!usr/bin/python3
import database as db
import queries as q
import verify as ver

CONN = r'./app-db/data-update.db'

def get_query_in_queue(executor_user):
    query = (q.query_list['query_queue'],(executor_user,))
    result = db.get_data(CONN,query)
    print (result)
    records = []
    if result['status']:
        #a.id, a.query, a.num_of_row,a.application,a.user_id
        for item in result['data']:
            print ("Processing Record", item)
            query_verified = ver.verify_query(item[1]+";")
            print (query_verified)
            current_rows =  query_verified[0]['number_of_rows']
            #current_rows =  0
            records.append({"id":item[0],"update_query":item[1],"num_of_rows": item[2],"current_rows":current_rows,"application": item[3], "user": item[4]})
        
    return {"data":records,"status":result['status'],"message":result['message']}

if __name__ == '__main__':
    print (get_query_in_queue('user_3'))