#!usr/bin/python3
from flask import Flask,request, make_response,jsonify
import queries as q
import database as db
from datetime import datetime
import verify as ver
import submit as sub
from flask_cors  import CORS
import check_user as chk
import fetch
import query_in_queue as qq
import execute as ex
import config

app = Flask(__name__)
CORS(app)
CONN = r'./app-db/data-update.db'


@app.route('/verify',methods=['POST'])
def analyze():
    req = request.get_json()
    print (req)
    print ("The cookie is",request.cookies)
    query = req['query']
    application = req['application'].strip()
    db_name = req['database'].strip()
    response = ver.verify_query(query,application,db_name)
    print (response)
    return make_response(jsonify(response),200)

@app.route('/submit',methods=['POST'])
def submit():
    req = request.get_json()
    print ("submit received",req)
    user_id = req['user_id']
    update_query = req['update_query']
    select_query = req['select_query']
    num_of_rows = req['num_of_rows']
    app = req['app']
    db_name = req['db_name']
    result = sub.submit_query(update_query,select_query,num_of_rows,user_id,app,db_name)
    return make_response(jsonify(result),200)

@app.route('/login',methods=['POST'])
def login():
    req = request.get_json()
    user_id = req['user_id']
    password = req['password']
    result = chk.verify_login(user_id,password)
    print (result)
    login_status = False
    applications = []
    databases = []
    access = ''
    user = ''
    message = ''
    if result['status']:
        if len(result['data'])>0:
            print ('more than 1 record')
            login_status = True
            for item in result['data']:
                print ("Prinitng item",item)
                user = item[0]
                applications.append(item[2])
                for app in applications:
                    print ("The app is", app)
                    d = {}
                    temp = config.get_database_value(app). split(',')
                    d[app] = temp
                    databases.append(d)
                access = item[1]
        else:
            message = "User Id or Password Not set up"
            
    else:
        message = f"Application Issue - {result['message']}"
    res = make_response(jsonify({"login":login_status,"applications":applications,"access":access,"message": message,'databases': databases}),200)
    res.headers["Access-Control-Allow-Origin"] = 'http://localhost:4200'
    res.headers["Access-Control-Allow-Credentials"] = True

    res.set_cookie('username',user,max_age=60*60,samesite='LAX')
    return res

@app.route('/queue',methods=['POST'])
def query_in_queue():
    if request.method == 'POST':
        req = request.get_json()
        print ("received",req)
        user_id = req['user_id']
        result = qq.get_query_in_queue(user_id)
        return  make_response(jsonify(result), 200)

@app.route('/execute',methods=['POST'])
def execute_query():
    if request.method == 'POST':
        req = request.get_json()
        print ("Execute Query received",req)
        query_id = req['id']
        result = ex.execute_query(query_id)
        return  make_response(jsonify(result), 200)

@app.route('/query',methods=['GET','POST'])
def query():
    if request.method == 'POST':
        req = request.get_json()
        print ("received",req)
        user_id = req['user_id']
        result = fetch.get_queries(user_id)
        print (result)
        return make_response(result,200)

    elif request.method == 'GET':
        #req = request.get_json()
        print (request.cookies)
        for key in request.cookies:
            print (key, request.cookies[key])
        #print ("received",req)
        '''user_id = req['user_id']
        query = q.query_list['get_queries'],(user_id,)
        result = db.get_data(CONN,query)
        print (result)
        status = True
        message = None
        records = []
        if result['status']:
            for item in (result['data'][0]):
                print ("The item being processed is",item)
                row = []    
                for i,v in enumerate(item):
                    print (f"the index is {i}", v)
                    d = {}
                    d[result['data'][1][i][0]] = v
                    row.append(d)
                records.append(row)
        else:
            status = False
            message = result['message']
        
        return {'data':records,'status':status,'message':message}'''
        return make_response('Ok',200)

