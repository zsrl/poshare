# poshare

poshare是一个获取公开投资组合的工具，po时`portfolio`的缩写，share代表分享。

## 雪球

```python
from poshare import Xueqiu

Xueqiu.config({
    'cookie': 'your xueqiu cookie'
})

xq = Xueqiu(symbol='ZH1254937')

# 组合名称
xq.cube_name
# 组合信息
xq.cube_info
# 股票配置（环形图）
xq.cube_pie_data
# 详细仓位
xq.cube_tree_data


# 调仓历史
xq.history()
# 收益率走势
xq.all()
# 业绩平级(雷达图)
xq.summary()
# 最新调仓
xq.show_origin()
```


## 果仁

```python
from poshare import Gouren

Gouren.config({
    'cookie': 'your guoren cookie'
})

gr = Gouren(symbol='2032861.R.247270131703851')

# 策略详情
gr.strategy()

```