import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import {HttpClientModule} from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DishesApi } from './dishes/dishes-api.service';
import { DessertsComponent } from './desserts/desserts.component';
import { RouterModule } from '@angular/router';
import { DessertApi } from './desserts/desserts-api.service';
import { DishesComponent } from './dishes/dishes.component';
import { LoginFormComponent } from './login-form/login-form.component';


@NgModule({
  declarations: [
    AppComponent,
    DessertsComponent,
    DishesComponent,
    LoginFormComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    RouterModule.forRoot([
      {path: 'dishes', component: DishesComponent},
      {path: 'desserts', component: DessertsComponent}
    ])
  ],
  providers: [DishesApi, DessertApi],
  bootstrap: [AppComponent]
})

export class AppModule { }
