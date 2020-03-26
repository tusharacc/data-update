import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';
import { Router } from '@angular/router';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-template',
  templateUrl: './template.component.html',
  styleUrls: ['./template.component.scss']
})
export class TemplateComponent implements OnInit {

  templateResponse:[{}];
  queryname:string = 'SELECT QUERY'
  queries: Array<string>;
  showAdditionalInfo:boolean = false;
  appName:string;
  database:string;
  query: string;
  columns:Array<string>;
  queriesToBeSubmitted:Array<string> = [];
  submitted:boolean = false;
  processing: boolean = false;


  constructor(private service:DataService, private router: Router) { }

  ngOnInit() {
    if (this.service.user_id){
      this.service.getTemplateQueries()
    .subscribe(data =>{
      console.log(data)
      this.queries = []
      this.templateResponse = data['data']
      data['data'].forEach(item =>{
        this.queries.push(item['query_name']);
        console.log(this.queries);
      })
    })
    } else {
      this.router.navigateByUrl('/')
    }
    
  }

  querySelected(){
    if (this.queryname != 'SELECT QUERY'){
      for (let item in this.templateResponse){
        console.log('The item processes id', this.templateResponse[item],this.queryname)
        if (this.templateResponse[item]['query_name'] == this.queryname){
          this.appName = this.templateResponse[item]['application']
          this.database = this.templateResponse[item]['db']
          this.query = this.templateResponse[item]['query']
          this.showAdditionalInfo = true;
          this.columns = []
          for (let col of this.templateResponse[item]['updated_columns']){
            console.log("The column Update clause", col)
            this.columns.push(col)
          }
          for (let col of this.templateResponse[item]['where_columns']){
            console.log("The column where clause", col)
            this.columns.push(col)
          }
        }
      }
    }
  }

  onSubmit(f:NgForm){
    console.log("The form value",f)
    let query = this.query;
    for (let col of this.columns){
      console.log("The value being processed,",col,f['value'][col],query);
      query = query.replace('?',`'${f['value'][col]}'`);
      console.log("The Updated Vlaue is",query);
    }

    this.queriesToBeSubmitted.push(query)
    f.resetForm();
    
  }

  resetForm(){
    this.queryname = 'SELECT QUERY';
    this.appName = null;
    this.database = null;
    this.query = null
    this.showAdditionalInfo = false
    this.queriesToBeSubmitted = [];
  }

  initiateProcessing(el){
    for (let i=0; i< 1; i++){
      this.processing = true
      console.log(el, typeof el)
      let processingQuery = el.getElementsByClassName("query")[0].innerText
      this.bubbleProgress(el)
      this.service.executeTemplateQueries(processingQuery,this.queryname, this.database, this.appName)
      .subscribe((data)=>{
        this.processing = false
        console.log("Completed", data)
        if (data['status']){
          el.getElementsByClassName('status')[0].insertAdjacentHTML('afterbegin',`<kbd>Completed<\kbd>`)
          el.className = "success"
          this.submitQueries()
        } else {
          el.className = "error"
          el.getElementsByClassName('status')[0].insertAdjacentHTML('afterbegin',`<kbd>Failed<span> ${data['message']}</span></kbd>`)
        }
      })
    }
  }

  submitQueries(){
    console.log("Gettnig Submitted")
    let elems = document.getElementsByClassName('submitted-query-row')
    if (elems.length >= 1){
      this.initiateProcessing(elems[0])
    }
    

  }

  bubbleProgress(el){
    console.log(el, typeof el)
    let elem = el.getElementsByClassName("progress")[0];
    let childElems = elem.getElementsByTagName("div");
    let index = 0;
    function showElement(childElems) {
      for (let i = 0; i < childElems.length; i++) {
        if (i == index) {
          childElems[i].style.backgroundColor = "white";
        } else {
          childElems[i].style.backgroundColor = "#D2C68D";
        }
      }
      index++;
      if (index > 2) {
        index = 0;
      }
      console.log("The class name is",el.className, el, el.classList)
      if (el.className != 'error' && el.className != 'success'){
        setTimeout(showElement, 500, childElems);
      } else {
        for (let i = 0; i < childElems.length; i++){
          childElems[i].style.backgroundColor = "#D2C68D";
        }
      }
      
    }
    //console.log(childElems[1].style.display)
    setTimeout(showElement, 500, childElems);

  }

}
