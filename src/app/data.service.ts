import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders,  } from '@angular/common/http'
import { Observable } from 'rxjs';

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


}
