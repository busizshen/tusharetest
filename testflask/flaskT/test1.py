import tushare as ts
import pandas as pd
from IPython.display import HTML

StockCode='300036'

#历年前十大股东持股情况
#df1为季度统计摘要，data1为前十大持股明细统计
df1, data1 = ts.top10_holders(code=StockCode, gdtype='1') #gdtype等于1时表示流通股，默认为0

df1 = df1.sort_values('quarter', ascending=True)

qts = list(df1['quarter'])
data = list(df1['props'])

lgdstr = """
var axisData = """ + str(qts) + """;
var data = """ + str(data) + """;
var links = data.map(function (item, i) {
    return {
        source: i,
        target: i + 1
    };
});
links.pop();
option = {
    title: {
        text: '【超图软件】前十大流通股东持股占比'
    },
    tooltip: {
        trigger: 'item'
    },
    xAxis: {
        type : 'category',
        boundaryGap : false,
        data : axisData
    },
    yAxis: {
        type : 'value'
    },
    series: [
        {
            type: 'line',
            layout: 'none',
            coordinateSystem: 'cartesian2d',
            symbolSize: 10,
            label: {
                normal: {
                    show: true
                }
            },
            edgeSymbol: ['circle', 'arrow'],
            edgeSymbolSize: [2, 5],
            data: data,
            links: links,
            lineStyle: {
                normal: {
                    color: '#2f4554'
                }
            }
        }
    ]
};
"""

headstr = """
<div id="showhere" style="width:800px; height:600px;"></div> 
<script> 
require.config({ paths:{ echarts: '//cdn.bootcss.com/echarts/3.2.3/echarts.min', } });
require(['echarts'],function(ec){
var myChart = ec.init(document.getElementById('showhere'));
"""

tailstr = """
myChart.setOption(option);
    });
</script>
"""

print(HTML(headstr + lgdstr + tailstr).data)