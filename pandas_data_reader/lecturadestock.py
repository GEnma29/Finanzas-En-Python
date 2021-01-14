import pandas_datareader.data as web
import matplotlib.pyplot as plt
from datetime import date

# TEst for Fintual 
class Portfolio ():

    def __init__(self,year,mes,day,year2,mes2,day2,company):
        self.year = year
        self.mes = mes
        self.day = day
        self.year2 = year2
        self.mes2 = mes2
        self.day2 = day2
        self.company = company

        newdate = date(self.year,self.mes,self.day)
        newdate2 = date(self.year2,self.mes2,self.day2)
        google = web.DataReader("GOOGL","yahoo",newdate,newdate2)
        google.head()
        google['Open'].plot(label= 'GOOGL Open price',figsize =(15,75))
        google['Close'].plot(label= 'GOOGL Close price')
        plt.legend()
        plt.title('Google Stock Prices')
        plt.ylabel('Stock Price')
        plt.show()

Portfolio(2020,4,9,2020,9,27,Google)
