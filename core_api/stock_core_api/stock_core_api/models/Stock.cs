using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace stock_core_api.models
{
    public class Stock
    {
        public DateTime Date { get; set; }
        public string Symbol { get; set; }
        public string Series { get; set; }
        public decimal PrevClose { get; set; }
        public decimal Open { get; set; }
        public decimal High { get; set; }
        public decimal Low { get; set; }
        public decimal Close { get; set; }
        public int Volume { get; set; }
    }
}
