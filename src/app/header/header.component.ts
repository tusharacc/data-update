import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {

  role:string = ''
  constructor(private service: DataService, private router: Router) { }

  ngOnInit() {
  }

  ngDoCheck() {
    if (this.service.role != ''){
      this.role = this.service.role
    }
  }

  navigateTo(url,event){
    console.log("Event is", event)
    this.router.navigateByUrl(url)
  }
  

}
