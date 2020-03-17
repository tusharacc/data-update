import { Component, OnInit } from '@angular/core';
import {CookieService} from 'ngx-cookie-service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'data-update';

  cookieValue = 'UNKNOWN';

  constructor (private cookieService:CookieService){}

  ngOnInit(): void{
    this.cookieValue = this.cookieService.get('username')
    console.log("The username is", this.cookieValue)
  }

}
