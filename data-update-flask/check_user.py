import database as db
import queries as q

CONN = r'./app-db/data-update.db'

def verify_login(user_id, password):
    query = q.query_list['login'],(user_id,password)
    result = db.get_data(CONN,query)
    return result