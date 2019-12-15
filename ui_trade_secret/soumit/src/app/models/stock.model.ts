
export interface StockModel {
    symbol: string;
    companyName: string;
    date: Date;
    previousClose: number;
    open: number;
    dayHigh: number;
    dayLow: number;
    closePrice: number;
    basePrice: number;
    averagePrice: number;
    high52: number;
    low52: number;
    lastPrice: number;

}