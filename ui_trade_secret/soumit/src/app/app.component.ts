import { Component, OnInit } from '@angular/core';
import { AppService } from './app.service';
import { StockModel } from './models/stock.model';
import { AlertService } from './services/alert.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'Stock !!!!';
  public stockFound: boolean;
  public company_name: string;
  public open_price: number;
  public high_price: number;
  public low_price: number;
  public close_price: number;
  public range: number;
  public pvt: number;
  public th: number;
  public ph: number;
  public bh: number;
  public tl: number;
  public pl: number;
  public bl: number;
  public th_tl: number;

  public circuit_high: number;
  public moderate_stoploss: number;
  public risky_stoploss: number;
  public first_low: number;
  public total_circuit_low: number;
  public total_circuit_high: number;
  public show_main: boolean;
  public avg_high_price: number;
  public avg_low_price: number;
  constructor(private alertService: AlertService, private appService: AppService) {
  }

  ngOnInit() {
    this.stockFound = false;
    this.company_name = '';
    this.open_price = 0.0;
    this.high_price = 0.0;
    this.low_price = 0.0;
    this.close_price = 0.0;
    this.range = 0.0;
    this.pvt = 0.0;
    this.th = 0.0;
    this.ph = 0.0;
    this.bh = 0.0;
    this.tl = 0.0;
    this.pl = 0.0;
    this.bl = 0.0;
    this.th_tl = 0.0;
    this.circuit_high = 0.0;
    this.moderate_stoploss = 0.0;
    this.risky_stoploss = 0.0;
    this.first_low = 0.0;
    this.total_circuit_low = 0.0;
    this.total_circuit_high = 0.0;
    this.avg_high_price = 0.0;
    this.avg_low_price = 0.0;

    this.show_main = false;
  }
  public showMain(): boolean {
    return this.show_main;
  }
  public submit(password: any) {
    if (password.value === 'rony9903481771') {
      this.show_main = true;
    } else {
      this.show_main = false;
      password.value = '';
    }
  }


  public predictStock($event): void {
    const openPrice = document.getElementById('openPrice');
    const highPrice = document.getElementById('highPrice');
    const lowPrice = document.getElementById('lowPrice');
    const closePrice = document.getElementById('closePrice');
    this.ruleEngine(+openPrice['value'], +highPrice['value'], +lowPrice['value'], +closePrice['value']);
  }

  public callAPI($event): void {
    const stock_signature = document.getElementById('stock_signature');
    if (stock_signature['value'].toString() !== '') {
      this.appService.GetStock(stock_signature['value'].toString())
        .subscribe((response: StockModel) => {
          this.alertService.confirmationMessage('Success', `Your stock name is ${response.companyName}`,
            'success', true, false, 'Ok', '', '');
          this.company_name = response.companyName;
          document.getElementById('openPrice')['value'] = +response.open;
          document.getElementById('highPrice')['value'] = +response.dayHigh;
          document.getElementById('lowPrice')['value'] = +response.dayLow;
          document.getElementById('closePrice')['value'] = +response.closePrice;
          this.predictStock($event);
        }, _ => {
          this.alertService.confirmationMessage('Error', `Something went wrong.`,
            'error', true, false, 'Ok', '', '');
        });
    }
  }



  private ruleEngine(openPrice: number, highPrice: number, lowPrice: number, closePrice: number): void {
    this.open_price = openPrice;
    this.high_price = highPrice;
    this.low_price = lowPrice;
    this.close_price = closePrice;
    this.range = this.high_price - this.low_price;
    this.th = (this.high_price + this.close_price) / 2;
    this.tl = (this.low_price + this.close_price) / 2;
    this.pl = (this.th - this.range);
    this.bl = (this.pl - this.range);
    this.ph = (this.tl + this.range);
    this.bh = (this.ph + this.range);
    this.pvt = (this.th + this.tl) / 2;
    this.circuit_high = (this.close_price * 20) / 100;
    this.moderate_stoploss = ((this.tl + this.pl) / 2) + this.range;
    this.risky_stoploss = ((this.bl + this.pl) / 2) + this.range;
    this.first_low = (this.th + this.tl) / 2;
    this.avg_high_price = (this.ph + this.th) / 2;
    this.avg_low_price = (this.first_low + this.pl) / 2;
    this.total_circuit_low = (this.close_price - this.circuit_high);
    this.total_circuit_high = (this.close_price + this.circuit_high);
    this.th_tl = this.th - this.tl;
    this.moderate_stoploss = this.moderate_stoploss - this.th_tl;
    this.stockFound = true;
  }
  public clear(openPrice: any, highPrice: any, lowPrice: any, closePrice: any): void {
    this.stockFound = false;
    this.open_price = 0.0;
    this.high_price = 0.0;
    this.low_price = 0.0;
    this.close_price = 0.0;
    this.range = 0.0;
    this.pvt = 0.0;
    this.th = 0.0;
    this.ph = 0.0;
    this.bh = 0.0;
    this.tl = 0.0;
    this.pl = 0.0;
    this.bl = 0.0;
    this.circuit_high = 0.0;
    this.moderate_stoploss = 0.0;
    this.risky_stoploss = 0.0;
    this.first_low = 0.0;
    this.total_circuit_low = 0.0;
    this.total_circuit_high = 0.0;
    openPrice.value = '';
    highPrice.value = '';
    lowPrice.value = '';
    closePrice.value = '';
  }
  public back(): void {
    this.stockFound = false;
    this.show_main = false;
  }
}
