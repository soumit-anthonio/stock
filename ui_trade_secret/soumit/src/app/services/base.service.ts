import { Inject, Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Headers, RequestOptions } from '@angular/http';
import { HttpClient, HttpHeaders, HttpErrorResponse, HttpParams, HttpBackend } from '@angular/common/http';
import { LOCAL_STORAGE, WebStorageService } from 'angular-webstorage-service';
import 'rxjs/add/operator/catch';
import 'rxjs/add/observable/throw';
import { map } from 'rxjs/operators/map';
import { environment } from '../../environments/environment';
import { catchError } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class BaseService {
  private queryParam = {};
  public AccessToken: string;
  private rootURL = environment.apiUrl;
  private httpClient: HttpClient;
  constructor(@Inject(LOCAL_STORAGE) private storage: WebStorageService, private http: HttpClient, private handler: HttpBackend) {
    this.AccessToken = '';
  }

  get(url: string, urlParamObject: any, queryparam: any): Observable<any> {
    const headers = new HttpHeaders();

    if (queryparam.updates != null) {
      this.queryParam = { params: queryparam };
    } else {
      this.queryParam = {};
    }


    this.httpClient = new HttpClient(this.handler);
    return this.httpClient.get(url, this.queryParam)
      .catch(this.errorHandler);



  }
  private errorHandler(error: HttpErrorResponse) {
    return Observable.throw(error.message || 'Server Error....');

  }




}
