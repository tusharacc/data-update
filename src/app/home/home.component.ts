import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';
import {CookieService} from 'ngx-cookie-service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  
  flashMessage:boolean = false;
  erroredQuery:string = ''
  message:string = '';
  type:string = ''
  queries: any;
  headers: any;
  data: any;
  selectQuery: string;
  showTable: boolean = false;
  errorFound: boolean = false;
  showData: boolean = false;
  submittedQueries: []

  constructor(private service: DataService,private cookieService:CookieService,private router:Router) { }

  ngOnInit() {
    this.submittedQueries = [];
    if (this.service.user_id){
      this.service.getQueries()
      .subscribe(data => {
      console.log(data['data'])
      this.submittedQueries = data['data']
      })
    } else {
      this.router.navigateByUrl('/')
    }
  }

  basicVerification(query){
    let splitQuery = query.split(';')
  
    let re = /^\s?update\s+(.*)\s+set\s+(.*)\s+where\s+(.*)\s*$/i
  
    for (let i = 0; i < splitQuery.length - 1; i++){
      let match:boolean = re.test(splitQuery[i]);
      console.log("Processing", JSON.stringify(splitQuery[i]),match );
      if (match){
        console.log("Element Processed")
      } else {
        this.erroredQuery = splitQuery[i];
        console.log("Validation Failed")
        return false
      }
    }
    return true 
  }

  submitQuery(updateQuery,numOfRows){
    console.log("The update Query is ,", updateQuery);
    let userid:string = this.cookieService.get('username');
    this.service.submit(updateQuery,userid,numOfRows,'app')
    .subscribe(data =>{
      console.log('Data from Post', data)
      this.flashMessage = true;
      if (data['status']){
        this.type = 'success';
        this.message = `${updateQuery} submitted succesfully`;
      } else {
        this.type = 'error';
        this.message = `${updateQuery} submission failed. Reason ${data['message']}`;
      }
      
      setTimeout(()=>{
        this.flashMessage = false;
      }, 5000)
    })
  }

  verifyQuery(query){
    console.log(query);
    let verified:boolean = this.basicVerification(query);
    console.log("The verification status", verified)
    if (verified){
      let number_of_records;
      this.queries = [];
      let queryMessage: string;
      this.service.verify(query)
      .subscribe(data => {
        console.log(data)
        data.forEach(element => {
          let error = false;
          if (element['number_of_rows'] === 'Error'){
            number_of_records = 0
            this.errorFound = true;
            queryMessage = element['status']
            error = true
          } else {
            number_of_records = element['number_of_rows']
            queryMessage = 'No Error Found'
          }
          this.queries.push({update_query: element['update_query']
                            ,number_of_rows: number_of_records
                            ,message: queryMessage
                            ,select_query: element['select_query']
                            ,rows: element['rows']
                            ,error: error})
        });
        this.showTable = true;
      })
    } else {
      console.log("Errored")
      this.flashMessage = true;
      this.type = 'error';
      this.message = `${this.erroredQuery} is incorrect.`;
      setTimeout(()=>{
        this.flashMessage = false;
      }, 5000)
    }
    
  }

  displayData(records,query){
    this.headers = [];
    this.data = [];
    this.selectQuery = query;
    let firstPass: boolean = true
    console.log(records)
    records.forEach(element =>{
      if (firstPass){
        for (const key in element){
          this.headers.push(key)
        }
        firstPass = false
      }

      this.data.push(Object.values(element))
    })
    this.showData = true
  }

  closeDiv(){
    this.showData = false;
    this.headers = [];
    this.data = [];
    this.selectQuery = '';
  }
}
