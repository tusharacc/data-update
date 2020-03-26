query_list = {
    "insert_query": "INSERT INTO QueryTable (query,select_query,num_of_rows,user_id,application,database,date_submitted, status) VALUES (?,?,?,?,?,?,?,?) ",
    "get_queries":"SELECT query,num_of_rows,date_submitted,status,date_executed,application FROM QueryTable where user_id = ?",
    "login":"SELECT user_id,access, application FROM UserTable where user_id = ? and password = ?",
    "query_queue": "Select a.id, a.query, a.select_query,a.num_of_rows,a.application,a.database,a.user_id from QueryTable a, UserTable b where b.user_id = ? and b.access = 'executor' and a.status = 'SUBMITTED' and b.application = a.application",
    "get_query":"SELECT query,num_of_rows,date_submitted,status,date_executed,application,database FROM QueryTable where id = ?",
    "update_query":"UPDATE  QueryTable Set status = 'EXECUTED', date_executed = ?, updated_rows = ? where id = ?",
    "insert_query_template":"INSERT INTO QueryTemplate (query,updated_columns, where_columns,query_name,db,application,expected_rows) VALUES (?,?,?,?,?,?,?)",
    "get_template_query": "Select a.query_name,a.query, a.updated_columns, a.where_columns, a.application, a.db From QueryTemplate a, UserTable b where b.user_id = ? and a.application = b.application",
    "get_updated_row": "Select expected_rows From QueryTemplate where query_name = ?",
}