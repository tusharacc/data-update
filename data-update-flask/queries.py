query_list = {
    "insert_query": "INSERT INTO QueryTable (query,num_of_rows,user_id,application,date_submitted, status) VALUES (?,?,?,?,?,?) ",
    "get_queries":"SELECT query,num_of_rows,date_submitted,status,date_executed,application FROM QueryTable where user_id = ?",
    "login":"SELECT user_id,access, application FROM UserTable where user_id = ? and password = ?",
    "query_queue": "Select a.id, a.query, a.num_of_rows,a.application,a.user_id from QueryTable a, UserTable b where b.user_id = ? and b.access = 'executor' and a.status = 'SUBMITTED' and b.application = a.application",
    "get_query":"SELECT query,num_of_rows,date_submitted,status,date_executed,application FROM QueryTable where id = ?",
    "update_query":"UPDATE  QueryTable Set status = 'EXECUTED', date_executed = ?, updated_rows = ? where id = ?",
}