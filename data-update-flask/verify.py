#!usr/bin/python3
import re
import database as db

query_pattern = re.compile(r'^\s*update\s+(?P<table_name>.*)\s+set\s+(?P<columns>.*)\s+where\s+(?P<condition>.*)\s*$',flags=re.IGNORECASE)
column_value_pattern = re.compile(r'^\s*(?P<column>.*)\s*=\s*(?P<value>.*)\s*$')
CONN = r'./sample-db/sample.db'

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
def verify_query(query):
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
        
        result = db.get_data(CONN,select_query)
        print ("The select Query is",select_query)
        if result['status']:
            number_of_records = len (result['data'])
            rows = []
            #print (result['data'].keys())
            for data in result['data']:
                d = {}
                for col in columns:
                    d[col] = data[col.strip()]
                rows.append(d)
            output.append({'update_query':item,'select_query':select_query[0],'number_of_rows':number_of_records,'rows':rows,'status':'Ok'})
        else:
            output.append({'update_query':item,'select_query':select_query[0],'number_of_rows':'Error','rows':'Error','status':str(result['message'])})
    print (output)
    return (output)

if __name__ == '__main__':
    verify_query("Update UserCartTable set user_name='user3', item = 'keyboard' where user_name='user1' and shipping_status='Not Shipped';Update UserCartTable1 set user_name='user3', item = 'keyboard' where user_name='user5' and shipping_status='Not Shipped';Update UserCartTable set user_name='user3', item = 'keyboard' where user_name='user5' and shipping_status='Not Shipped';")
