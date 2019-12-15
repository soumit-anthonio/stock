using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using Newtonsoft.Json;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using stock_core_api.models;
using System.Diagnostics;
using IronPython.Hosting;
using Microsoft.Scripting.Hosting;
using Newtonsoft.Json;

namespace stock_core_api.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class StockController : ControllerBase
    {
        private readonly ILogger<StockController> _logger;

        public StockController(ILogger<StockController> logger)
        {
            _logger = logger;
        }

        [HttpGet]
        [Route("fetchstockinfo/{symbol_name}/date/{date}")]
        public List<Stock> Get(string symbol_name, string date)
        {
            string fileName = @"E:\stock\soumit.py "+ symbol_name+" "+date;

            Process p = new Process();
            p.StartInfo = new ProcessStartInfo(@"C:\Users\Soumit\AppData\Local\Programs\Python\Python38-32\python.exe", fileName)
            {
                RedirectStandardOutput = true,
                UseShellExecute = false,
                CreateNoWindow = true
            };
            p.Start();

            string output = p.StandardOutput.ReadToEnd();
            p.WaitForExit();

           





            using (StreamReader r = new StreamReader("E://stock/data/_data.json"))
            {
                var json = r.ReadToEnd();

                List<Stock> stocks = new List<Stock>();
                var result = JsonConvert.DeserializeObject<Dictionary<string, dynamic>>(json);
                foreach (var key in result.Keys)
                {
                    Stock s = new Stock();
                    double ticks = double.Parse(key);
                    TimeSpan time = TimeSpan.FromMilliseconds(ticks);
                    DateTime startdate = new DateTime(1970, 1, 1) + time;
                    s.Date = startdate;
                    s.Symbol = (string)result.FirstOrDefault(x => x.Key == key).Value["Symbol"];
                    s.Series = (string)result.FirstOrDefault(x => x.Key == key).Value["Series"];
                    s.PrevClose = (decimal)result.FirstOrDefault(x => x.Key == key).Value["Prev Close"];
                    s.Open = (decimal)result.FirstOrDefault(x => x.Key == key).Value["Open"];
                    s.High = (decimal)result.FirstOrDefault(x => x.Key == key).Value["High"];
                    s.Low = (decimal)result.FirstOrDefault(x => x.Key == key).Value["Low"];
                    s.Close = (decimal)result.FirstOrDefault(x => x.Key == key).Value["Close"];
                    s.Volume = (int)result.FirstOrDefault(x => x.Key == key).Value["Volume"];
                    stocks.Add(s);
                }

                return stocks.OrderByDescending(x=>x.Date).ToList();
            }





                
        }
        public T GetFirstInstance<T>(string propertyName, string json)
        {
            using (var stringReader = new StringReader(json))
            using (var jsonReader = new JsonTextReader(stringReader))
            {
                while (jsonReader.Read())
                {
                    if (jsonReader.TokenType == JsonToken.PropertyName
                        && (string)jsonReader.Value == propertyName)
                    {
                        jsonReader.Read();

                        var serializer = new JsonSerializer();
                        return serializer.Deserialize<T>(jsonReader);
                    }
                }
                return default(T);
            }
        }
    }
}
