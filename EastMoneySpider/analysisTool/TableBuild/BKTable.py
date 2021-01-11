# -*- coding: utf-8 -*-
from HTMLTable import HTMLTable
import time
def getBKTable():
    # 标题
    table = HTMLTable(caption='板块资金流向 %s' % time.strftime("%Y-%m-%d", time.localtime()))

    # 表头行
    table.append_header_rows((
        ('板块名', '板块指数', '涨幅', '换手率', '上涨下跌',),
        (),
    ))

    # 合并单元格
    table[0][0].attr.rowspan = 2
    table[0][1].attr.rowspan = 2
    table[0][2].attr.colspan = 2

    # 数据行
    table.append_data_rows((
        ('牛仔裤', 110, 10, 20),
        ('T恤', 20, 20, -9),
        ('Nike鞋', 50, 22, 10),
    ))

    # 标题样式
    table.caption.set_style({
        'font-size': '18px',
        'color':'#000000',
    })

    # 表格样式，即<table>标签样式
    table.set_style({
        'border-collapse': 'collapse',
        'word-break': 'keep-all',
        'white-space': 'nowrap',
        'font-size': '16px',
    })

    # 统一设置所有单元格样式，<td>或<th>
    table.set_cell_style({
        'border-color': '#000',
        'border-width': '1px',
        'border-style': 'solid',
        'padding': '5px',
    })

    # 表头样式
    table.set_header_row_style({
        'color': '#fff',
        'background-color': '#48a6fb',
        'font-size': '18px',
    })

    # 覆盖表头单元格字体样式
    table.set_header_cell_style({
        'padding': '15px',
    })

    # 调小次表头字体大小
    table[1].set_cell_style({
        'padding': '8px',
        'font-size': '15px',
    })

    # 遍历数据行，如果增长量为负，标红背景颜色
    for row in table.iter_data_rows():
        if row[2].value < 0:
            row.set_style({
                'background-color': '#ffdddd',
            })

    html = table.to_html()
    return html

if __name__ == '__main__':
    print(getBKTable())