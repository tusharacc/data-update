import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { HomeComponent } from './home/home.component';
import { ExecuteComponent } from './execute/execute.component';
import { AdminComponent } from './admin/admin.component';
import { TemplateComponent } from './template/template.component';


const routes: Routes = [
  {path: '', component:LoginComponent, },
  {path: 'home', component:HomeComponent, },
  {path: 'execute', component:ExecuteComponent, },
  {path: 'admin', component:AdminComponent, },
  {path: 'template', component:TemplateComponent, },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
