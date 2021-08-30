import { keyframes } from '@angular/animations';
import { Component, OnDestroy, OnInit } from '@angular/core';
import {Subscription} from 'rxjs';
import {DishApi} from './dish-api.service';
import {Dish} from './dish.model';

@Component({
  selector: 'dish',
  templateUrl: './dish.component.html',
})

export class DishComponent implements OnInit, OnDestroy{
  title = 'Dishes';
  dishesListSubs: Subscription = new Subscription();
  dishesList: Dish[] = [];

  constructor(private dishesApi: DishApi) {
  }

  ngOnInit() {
    this.dishesListSubs = this.dishesApi
      .getDishes()
      .subscribe(res => {
          for (let key in res) {
            this.dishesList.push(new Dish(key, res[key]['name'], res[key]['description']))
          }
        },
        console.error
      );
  }

  ngOnDestroy() {
    this.dishesListSubs.unsubscribe();
  }
}