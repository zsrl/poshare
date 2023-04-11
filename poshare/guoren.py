import requests
import json
import time
from fake_useragent import UserAgent
class Guoren:
    cookie = None
    ua = UserAgent()

    @staticmethod
    def config(conf):
        Guoren.cookie = conf.get('cookie')
    
    def __init__(self, symbol=None):
        self.symbol =symbol
        self.url = {
            'strategy': 'https://guorn.com/stock/strategy'
        }
        self.s = requests.Session()
        self.s.headers.update({
            'User-Agent': Guoren.ua.random,
            'Cookie': Guoren.cookie
        })

    def strategy(self):
        res = self.s.get(f'{self.url.get("strategy")}?fmt=json&sid={self.symbol}&_={int(time.time())}')
        result = json.loads(res.text)
        return result
