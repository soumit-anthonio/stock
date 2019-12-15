import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpParams } from '@angular/common/http';
import { ApiUrlService } from 'src/app/services/api.url.service';
import { BaseService } from './services/base.service';

@Injectable({
  providedIn: 'root'
})
export class AppService {

  constructor(private baseService: BaseService, private apiUrlService: ApiUrlService) { }

  public GetStock(symbol_name: string): Observable<any> {
    const params = new HttpParams();

    const urlStringObject = {
      symbol_name: symbol_name
    };
    const mainURL = this.apiUrlService.getFullURL('GET_STOCK_INFORMATION', urlStringObject);
    return this.baseService.get(mainURL, {}, params);
  }
}
