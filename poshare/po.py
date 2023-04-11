from poshare import Xueqiu, Guoren
from typing import Dict

class Po:
    conf: Dict[type, type] = {}

    @staticmethod
    def config(conf):
        Po.conf = conf
        Xueqiu.config({
            'cookie': conf.get('xueqiu.cookie')
        })
        Guoren.config({
            'cookie': conf.get('guoren.cookie')
        })

    def __new__(cls, platform='xueqiu', symbol=None):
        if platform == 'xueqiu':
            return Xueqiu(symbol)
        elif platform == 'guoren':
            return Guoren(symbol)
        else:
            raise ValueError(f'不支持的平台: {platform}')
        
    #历史走势
    def history(self):
        pass

    #持仓
    def position(self):
        pass

    #历史调仓
    def rebalancing(self):
        pass

    #最新调仓
    def last_rebalancing(self):
        pass