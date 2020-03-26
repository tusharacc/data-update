import database as db
import queries as q
import re

CONN = r'./app-db/data-update.db'
pattern_template = re.compile('^\s?Update\s(?P<tablename>.*)\sset\s(?P<columnnames>.*)\swhere\s(?P<conditions>.*)$',flags=re.IGNORECASE)
column_value_pattern = re.compile(r'^\s*(?P<column>.*)\s*=\s*[?]\s*$',flags=re.IGNORECASE)
where_pattern = re.compile(r'(\w*)\s*=\s*[?]',flags=re.IGNORECASE)

##query: query,name: name, app: app, db_name: db_name, rows: rows
def submit_query(template_query,name,app,db_name,rows):
    query_match_group = pattern_template.match(template_query)
    print ("The match group",query_match_group)
    table_group = query_match_group.group('tablename')
    column_group = query_match_group.group('columnnames')
    where_group = query_match_group.group('conditions')

    #Get Columns
    columns = []
    for column_value in column_group.split(','):
        column_match_group = column_value_pattern.match(column_value)
        columns.append(column_match_group.group('column').strip())

    where = []
    #for conditions in where_group:
    print (repr(where_group))
    all_columns = where_pattern.findall(where_group)
    where = all_columns

    query = (q.query_list['insert_query_template'],(template_query,str(columns),str(where),name,db_name,app,rows,))
    result = db.insert_data('sqlite',CONN,query)
    print (result)
    return result




