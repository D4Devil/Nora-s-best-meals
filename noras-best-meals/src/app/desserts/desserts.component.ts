import { Component, OnInit } from '@angular/core';
import { Subscription } from 'rxjs';
import { Dessert } from './desserts.model';
import { DessertApi } from './desserts-api.service';

@Component({
  selector: 'desserts',
  templateUrl: './desserts.component.html',
})
export class DessertsComponent implements OnInit {
  title = 'Desserts'
  dessertsSub: Subscription = new Subscription();
  dessertsList: Dessert[] = [];

  constructor(private DessertApi: DessertApi) { }

  ngOnInit(): void {
    this.dessertsSub = this.DessertApi
    .getDishes()
    .subscribe(res => {
        for (let key in res) {
          this.dessertsList.push(new Dessert(key, res[key]['name'], res[key]['description']))
        }
      },
      console.error
    );
  }
}
