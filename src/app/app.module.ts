import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';

import { CookieService} from 'ngx-cookie-service';
import { HeaderComponent } from './header/header.component';
import { HomeComponent } from './home/home.component';

import { HttpClientModule } from '@angular/common/http';
import { ExecuteComponent } from './execute/execute.component';
import { AdminComponent } from './admin/admin.component';
import { TemplateQueriesComponent } from './admin/template-queries/template-queries.component';
import { TemplateComponent } from './template/template.component';


@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    HeaderComponent,
    HomeComponent,
    ExecuteComponent,
    AdminComponent,
    TemplateQueriesComponent,
    TemplateComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    AppRoutingModule
    
  ],
  providers: [CookieService],
  bootstrap: [AppComponent]
})
export class AppModule { }
