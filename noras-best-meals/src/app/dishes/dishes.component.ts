import { Component, OnInit } from '@angular/core';
import { Subscription } from 'rxjs';
import { Dish } from './dishes.model';
import { DishesApi } from './dishes-api.service';

@Component({
  selector: 'app-dishes',
  templateUrl: './dishes.component.html',
})

export class DishesComponent implements OnInit {

  dishesSub: Subscription = new Subscription();
  dishesList: Dish[] = []

  constructor(private dishesApi: DishesApi) { }

  ngOnInit(): void {
    this.dishesSub = this.dishesApi
      .getDishes()
      .subscribe(res => {
        for (let key in res) {
          this.dishesList.push(new Dish(key, res[key]['name'], res[key]['description']))
        }
      },
      console.error
    );
  }
}
