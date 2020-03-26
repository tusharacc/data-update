import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.scss']
})
export class AdminComponent implements OnInit {

  load:string = ''
  flashMessage:boolean = false;
  erroredQuery:string = ''
  message:string = '';
  type:string = ''
  constructor() { }

  ngOnInit() {
  }

  loadComponent(value) {
    this.load = value;
  }

  displayMessage(message){
    this.flashMessage = true;
    this.type = message.split('-')[0].trim().toLowerCase();
    console.log('The type is', this.type)
    this.message = `${message}`;
  }

}
