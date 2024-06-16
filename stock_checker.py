"""Exports class to be used by other scripts for checking stocks."""
import requests
from dotenv import dotenv_values

class Stock():
    """To be instantiated and its methods called for the purpose of doing something at a given minute time interval"""

    def __init__(self, stock_symbol):
        self.stock_symbol = stock_symbol
        self.api_secret = dotenv_values('.env')['API_KEY']
        self.stock_data = None

    def update_stock_data(self):
        url = f'https://api.twelvedata.com/quote?symbol={self.stock_symbol}&apikey={self.api_secret}'

        try:
            response = requests.get(url).json()
            self.stock_data = response
        except Exception as exc:
            print(exc)
    
    def get_stock_data(self):
        return self.stock_data
                
    def get_stock_percent_change(self):
        percent_change = self.stock_data['percent_change']
        return abs(float(percent_change))





