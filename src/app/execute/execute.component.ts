import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-execute',
  templateUrl: './execute.component.html',
  styleUrls: ['./execute.component.scss']
})
export class ExecuteComponent implements OnInit {

  queries: any;
  flashMessage:boolean = false;
  message:string = '';
  type:string = ''
  constructor( private service: DataService, private router:Router ) { }

  ngOnInit( ) {
    this.fetchQueries()
  }

  fetchQueries(){
    this.queries = []
    if (this.service.user_id){
      this.service.getQueryInQueue()
      .subscribe(data => {
        console.log(data['data'])
        this.queries = data['data'];
      })
    } else {
      this.router.navigateByUrl('/')
    }
  }

  executeQuery(id){
    this.service.executeQuery(id)
    .subscribe(data => {
      console.log(data)
      if (data['status']){
        this.flashMessage = true;
        this.type = 'success';
        this.message = `UPDATE SUCCESS.`;
        setTimeout(()=>{
          
          this.flashMessage = false;
        }, 5000)
        this.fetchQueries();
      } else {
        this.flashMessage = true;
        this.type = 'error';
        this.message = `UPDATE FAILED: ${data['message']}.`;
        setTimeout(()=>{
          this.flashMessage = false;
        }, 5000)
      }
    })
  }

  
}
