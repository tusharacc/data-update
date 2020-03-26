import { Component, OnInit, EventEmitter, Input, Output } from '@angular/core';
import { DataService } from 'src/app/data.service';

@Component({
  selector: 'app-template-queries',
  templateUrl: './template-queries.component.html',
  styleUrls: ['./template-queries.component.scss']
})
export class TemplateQueriesComponent implements OnInit {
  databases:Array<{}>;
  applicableDatabases:[];
  applications:Array<string>;
  name:string ;
  rows:number ;
  app:string;
  query:string;
  database:string;
  disableDbSelect: boolean = true;

  @Output() flashMessage = new EventEmitter<string>();

  constructor(private service: DataService) { }

  ngOnInit() {

    this.service.getApplicationConfigurations()
    .subscribe(data =>{
      //let data = incoming['data']
      console.log("Template Component",data)
      let arrData = data['data']
      this.applications = [];
      this.databases = []
      for (let item of arrData){
        let application = item['name'];
        console.log(item)
        this.applications.push(application);
        this.databases.push({ [application] : item['databases']})
      }
    })
  }

  applicationSelected(){
    console.log("Template, application selected", this.app);
    this.applicableDatabases = []
    for (let item of this.databases){
      console.log("The item is", item)
      for (let key in item){
        console.log("The key is",key)
        if (key == this.app){
          this.applicableDatabases = item[key];
          console.log(this.applicableDatabases);
          this.disableDbSelect = false;
        }
      }
      
    }
  }

  submitTemplateQuery(){
    console.log(this.query, this.name, this.app, this.database, this.rows)
    this.service.submitTemplateQuery(this.query, this.name, this.app, this.database, this.rows)
    .subscribe(data =>{
      console.log("Template Submit Query", data)
      if (data['status']){
        this.flashMessage.emit(`Success - ${this.query} Updated`)
      } else {
        this.flashMessage.emit(`Error - ${this.query} Updated`)
      }
    })
    
  }

}
