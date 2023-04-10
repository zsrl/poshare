import requests
import json
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import re
from poshare.config import CONFIG

ua = UserAgent()

class Xueqiu:

    def __init__(self, symbol=None):
        self.symbol =symbol
        self.url = {
            'html': 'https://xueqiu.com/P/',
            'all': 'https://xueqiu.com/cubes/nav_daily/all.json',
            'summary': 'https://xueqiu.com/cubes/rank/summary.json'
        }
        self.s = requests.Session()
        self.s.headers.update({
            'User-Agent': ua.random,
            'Cookie': CONFIG.get('xueqiu.cookie')
        })
        soup = self._html()
        self.cube_name = self._get_variable(soup, 'cubeName')
        self.cube_info = self._get_variable(soup, 'SNB.cubeInfo')
        self.cube_pie_data = self._get_variable(soup, 'SNB.cubePieData')
        self.cube_tree_data = self._get_variable(soup, 'SNB.cubeTreeData')
    
    def _get_variable(self, soup, key):
        script_tag = soup.find('script', text=lambda text: text and f'{key}' in text)
        script_content = script_tag.text
        pattern = re.compile(rf"{key}\s*=\s*(.*?);", re.DOTALL)
        variable_value = re.search(pattern, script_content).group(1)
        return json.loads(variable_value)

    def _html(self):
        res = self.s.get(f'{self.url.get("html")}{self.symbol}')
        html_content = res.text
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup


    def all(self):
        res = self.s.get(f'{self.url.get("all")}?cube_symbol={self.symbol}')
        result = json.loads(res.text)
        return result

    def summary(self):
        res = self.s.get(f'{self.url.get("summary")}?symbol={self.symbol}&ua=web')
        result = json.loads(res.text)
        return result