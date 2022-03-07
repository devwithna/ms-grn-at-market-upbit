# -*- coding: utf-8 -*-

import pyupbit

class MarketUpbit(object):    
    def __init__(self):
        self.access='lJk9y8oC2OeUY2oIlKgAAKXoqHpXCmr1Rw39fF1x'
        self.secret='oUEPpLlUJjEbtxszjxIawgoYGPC0cN8Bhx3XMExv'
        self.myMarket = pyupbit.Upbit(self.access, self.secret);
        pass
    
    
    def get_ohlcv(self, ticker, days):
        df = pyupbit.get_ohlcv(ticker, interval="day", count=days)
        return df.to_json();

                

