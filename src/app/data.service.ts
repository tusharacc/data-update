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
  constructor(private http:HttpClient) { }

  verify(query){
    let endpoint = this.url + 'verify'
    return this.http.post<[]>(endpoint,JSON.stringify({query: query}),this.httpOptions);
  }

  submit(query,numOfRows,app){
    let endpoint = this.url + 'submit'
    return this.http.post<{}>(endpoint,JSON.stringify({query: query,user_id: this.user_id,num_of_rows: numOfRows, app: app}),this.httpOptions);
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
