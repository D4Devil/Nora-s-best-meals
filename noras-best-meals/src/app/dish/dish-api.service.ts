import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Observable} from 'rxjs';
import {API_URL} from '../env';

@Injectable()

export class DishApi {

    constructor(private http: HttpClient) {
    }
  
    private static _handleError(err: HttpErrorResponse | any) {
      return Observable.throw(err.message || 'Error: Unable to complete request.');
    }
  
    // GET list of public, future events
    getDishes(): Observable<any> {
      return this.http
        .get(`${API_URL}/dishes/`)
    }
  }