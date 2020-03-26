import { Injectable, Query } from '@angular/core';
import { HttpClient, HttpHeaders,  } from '@angular/common/http'
import { Observable , of} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DataService   {

  httpOptions = {headers: new HttpHeaders({
    'Content-Type': 'application/json'
  })};

  url:string = 'http://127.0.0.1:5000/';
  user_id: string;
  application:[];
  role:string;
  databases:Array<{}>;

  constructor(private http:HttpClient) { }

  verify(query, app, database){
    let endpoint = this.url + 'verify'
    return this.http.post<[]>(endpoint,JSON.stringify({query: query, application: app, database: database}),this.httpOptions);
  }

  submit(updateQuery,selectQuery,numOfRows,appName,databaseName){
    console.log("The data received are",updateQuery, selectQuery, numOfRows, appName,databaseName)
    let endpoint = this.url + 'submit'
    return this.http.post<{}>(endpoint,JSON.stringify({update_query: updateQuery,select_query: selectQuery,user_id: this.user_id,num_of_rows: numOfRows, app: appName, db_name: databaseName}),this.httpOptions);
  }

  getQueries(){
    let endpoint = this.url + 'query'
    if (this.user_id){
      return this.http.post<[]>(endpoint,JSON.stringify({user_id: this.user_id}),this.httpOptions);
    }
    

  }

  login(userId,password){
    let endpoint = this.url + 'login'
    return this.http.post<{}>(endpoint,JSON.stringify({user_id: userId,password: password}),this.httpOptions);
    
  }

  getQueryInQueue(){
    let endpoint = this.url + 'queue'
    if (this.user_id){
      return this.http.post<[]>(endpoint,JSON.stringify({user_id: this.user_id}),this.httpOptions);
    }
  }

  executeQuery(id){
    let endpoint = this.url + 'execute'
    if (this.user_id){
      return this.http.post<[]>(endpoint,JSON.stringify({id: id}),this.httpOptions);
    }
  }

  getApplicationConfigurations(){
    let endpoint = this.url + 'appconfig'
    return this.http.get<[{}]>(endpoint,this.httpOptions);

  }

  submitTemplateQuery(query,name, app, db_name,rows){
    let endpoint = this.url + 'submittemplatequery'
    //this.query, this.name, this.app, this.database, this.rows
    return this.http.post<[]>(endpoint,JSON.stringify({query: query,name: name, app: app, db_name: db_name, rows: rows}),this.httpOptions);
  }

  getTemplateQueries(){
    let endpoint = this.url + 'gettemplatequery';
    if (this.user_id){
      return this.http.post<[]>(endpoint,JSON.stringify({user_id: this.user_id}),this.httpOptions);
    }
  }

  executeTemplateQueries(incomingQuery,name,db_name,app){
    let endpoint = this.url + 'executeTemplateQuery';
    if (this.user_id){
      return this.http.post<[]>(endpoint,JSON.stringify({query: incomingQuery, name: name, db: db_name, application: app }),this.httpOptions);
    }
  }

}
