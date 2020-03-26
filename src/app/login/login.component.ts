import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import {CookieService} from 'ngx-cookie-service';
import {Router} from '@angular/router';
import { DataService } from '../data.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  constructor(private cookieService:CookieService, private router:Router,private service: DataService) { }

  ngOnInit() {
  }

  validate(userid,password){
    console.log('The user name is',userid);
    console.log('The password is',password);
    this.service.login(userid,password)
    .subscribe(data => {
      console.log(data)
      if (data['login']){
        this.service.user_id = userid
        if (data['access'] === 'submitor'){
          this.service.application = data['applications']
          this.service.databases = data['databases']
          this.service.role = data['access']

          this.router.navigateByUrl('/home')
        } else if (data['access'] === 'executor'){
          this.service.application = data['applications']
          this.service.role = data['access']

          this.router.navigateByUrl('/execute')
        }
        
      }
    })
    //this.cookieService.set('username',userid);
    //this.router.navigateByUrl('/home')

  }
}
