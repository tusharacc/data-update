#!usr/bin/python3
import re
import database as db
import connection as cn
import config

query_pattern = re.compile(r'^\s*update\s+(?P<table_name>.*)\s+set\s+(?P<columns>.*)\s+where\s+(?P<condition>.*)\s*$',flags=re.IGNORECASE)
column_value_pattern = re.compile(r'^\s*(?P<column>.*)\s*=\s*(?P<value>.*)\s*$',flags=re.IGNORECASE)
#CONN = r'./sample-db/sample.db'

'''
Input;
    query: string

Output:
    Array: Dictionary of individual query
        update query,
        corresponding select query,
        # of records impacted,
        records impacted,
        status
        
'''
def verify_query(query,application,database=None):
    list_of_queries = query.split(';')
    output = []
    for item in list_of_queries[:-1]:
        print (f"Processing the query {repr(item)}")
        query_match_group = query_pattern.match(item)
        print ("The match group",query_match_group)
        column_group = query_match_group.group('columns')
        columns = []
        values = []
        for column_value in column_group.split(','):
            column_match_group = column_value_pattern.match(column_value)
            columns.append(column_match_group.group('column').strip())
            values.append(column_match_group.group('value').strip())
        
        print ("Columns",columns)

        select_query = (f"select {','.join(columns)} from {query_match_group.group('table_name')} where {query_match_group.group('condition')}",)
        print ("The select Query is",select_query)

        CONN = cn.get_connection(application,database)

        print ("The connection string is",CONN)
        result = db.get_data(config.get_sql_type('database'),CONN,select_query)
        
        if result['status']:
            number_of_records = len (result['data'])
            rows = []
            #print (result['data'].keys())
            for data in result['data']:
                print ("The data processes is", data)
                d = {}
                row = 0
                for col in columns:
                    d[col] = data[row]
                    row += 1
                rows.append(d)
            output.append({'update_query':item,'select_query':select_query[0],'number_of_rows':number_of_records,'rows':rows,'status':'Ok'})
        else:
            output.append({'update_query':item,'select_query':select_query[0],'number_of_rows':'Error','rows':'Error','status':str(result['message'])})
    print (output)
    return (output)

def get_number_of_rows(query,application,db_name):
    print ("Verify",application, db_name)
    CONN = cn.get_connection(application,db_name)
    result = db.get_data(config.get_sql_type('database'),CONN,query)
    status = True
    message=  None
    number_of_records = 0
    if result['status']:
        number_of_records = len (result['data'])

    return {"data":number_of_records,"status": status,"message":message}

if __name__ == '__main__':
    pass
    #verify_query("Update UserCartTable set user_name='user3', item = 'keyboard' where user_name='user1' and shipping_status='Not Shipped';Update UserCartTable1 set user_name='user3', item = 'keyboard' where user_name='user5' and shipping_status='Not Shipped';Update UserCartTable set user_name='user3', item = 'keyboard' where user_name='user5' and shipping_status='Not Shipped';")
