# coding:utf-8
# 引入app配置
from flask import jsonify  # JSON
from flask import render_template #读取页面
# coding:utf-8
from flask import Flask  # 默认
import pymysql
# app入口定义
app = Flask(__name__)
#链接数据库
conn=pymysql.connect(host='localhost',user='root',passwd='123456',db='demo')
def connect_mysql(conn):
    #判断链接是否正常
  conn.ping(True)
  #建立操作游标
  cursor=conn.cursor()
  #设置数据输入输出编码格式
  cursor.execute('set names utf8')
  return cursor  

#首页
@app.route('/')
def index():
    return render_template('index.html')

#地点薪资图页面(地图)
# 图表形式参考链接：http://echarts.baidu.com/demo.html#map-china-dataRange
@app.route('/zwyx/dd_index')
def zwyx_dd_view():
    return render_template('zwyx_dd.html')
# 地点和薪资
@app.route('/zwyx/dd')
def show_zwyx_dd():
    #建立链接游标
    cursor=connect_mysql(conn)
    # 初始化返回的字典
    returnDate = {}
    returnDate['status'] = 0
    # 查询地点和薪资的关系，职位总数，平均薪资
    sql='select count(ca_list.Id) as count_zw,avg(ca_list.zwyx) as avg_zwyx,ca_dd.province from ca_list inner join ca_dd on ca_dd.Id=ca_list.dd_id group by dd_id order by count_zw desc'
    #执行sql语句
    cursor.execute(sql)
    #取出所有结果集
    dd_zwyx_list = cursor.fetchall()
    #平均薪资
    avg_zwyx={}
    #总职位数
    count_zw={}
    if dd_zwyx_list:
        #循环遍历重新构建数据
        for value in dd_zwyx_list:
            #取得地点名
            dd_name=value[2]
            #判断总职位数是否存在地点名
            if not count_zw.has_key(dd_name):
                #地点名不存在则创建记录并存入对应数值
                count_zw[dd_name]={'name':dd_name,'value':value[0]}
            else:
                #存在则在原来基础上增加新的数值
                count_zw[dd_name] = {'name': dd_name, 'value': (value[0]+count_zw[dd_name]['value'])}
            # 判断平均薪资是否存在地点名
            if not avg_zwyx.has_key(dd_name):
                #不存在则创建记录并存入对应数值
                avg_zwyx[dd_name] = {'name': dd_name, 'value': round(value[1],2)}
            else:
                #存在则重新计算平均薪资
                avg_zwyx[dd_name] = {'name': dd_name, 'value': round((round(value[1],2) + avg_zwyx[dd_name]['value'])/2,2)}
        #重新构建数据
        return_count_zw=[]
        return_avg_zwyx=[]
        for item in count_zw:
            return_count_zw.append(count_zw[item])
        for item in avg_zwyx:
            return_avg_zwyx.append(avg_zwyx[item])
        #数据汇总
        returnDate['count_zw']=return_count_zw
        returnDate['avg_zwyx'] = return_avg_zwyx
        returnDate['status'] = 1
    #关闭游标链接
    cursor.close()
    return jsonify(returnDate)

#学历薪资图页面（柱状图）
# 参考链接:http://echarts.baidu.com/demo.html#bar-stack
@app.route('/zwyx/xl_index')
def zwyx_xl_view():
    return render_template('zwyx_xl.html')
# 学历和薪资
@app.route('/zwyx/xl')
def show_zwyx_xl():
    #建立链接游标
    cursor=connect_mysql(conn)
    #设置数据输入输出编码格式
    cursor.execute('set names utf8')
    returnDate = {}
    returnDate['status'] = 0
    returnDate['data'] = {}
    # 查询地点和薪资的关系，职位总数，平均薪资
    sql = 'select count(ca_list.Id) as count_zw,avg(ca_list.zwyx) as avg_zwyx,ca_xl.xl_name,max(zwyx),min(zwyx) from ca_list inner join ca_xl on ca_xl.Id=ca_list.xl_id group by xl_id order by count_zw desc'
    # 执行sql语句
    cursor.execute(sql)
    # 取出所有结果集
    xl_zwyx_list = cursor.fetchall()
    if xl_zwyx_list:
        returnDate['status'] = 1
        #总职位数
        count_zw=[]
        #平均薪资
        avg_zw=[]
        #学历名
        xl_list=[]
        #最大薪资
        max_xz=[]
        #最小薪资
        min_xz=[]
        #循环遍历存入数据
        for item in xl_zwyx_list:
            count_zw.append(item[0])
            avg_zw.append(round(item[1],2))#精度保留2位小数
            xl_list.append(item[2])
            max_xz.append(item[3])
            min_xz.append(item[4])
        #数据json化
        returnDate['count_zw'] = count_zw
        returnDate['avg_zw'] = avg_zw
        returnDate['xl_list'] = xl_list
        returnDate['max_xz'] = max_xz
        returnDate['min_xz'] = min_xz
    cursor.close()
    return jsonify(returnDate)

#公司规模薪资图页面（饼图）
# 参考链接：http://echarts.baidu.com/demo.html#pie-roseType
@app.route('/zwyx/gsgm_index')
def zwyx_gsgm_view():
    return render_template('zwyx_gsgm.html')
# 公司规模和薪资（饼图）
@app.route('/zwyx/gsgm')
def show_zwyx_gsgm():
    #建立链接游标
    cursor=connect_mysql(conn)
    returnDate = {}
    returnDate['status'] = 0
    # 查询地点和薪资的关系，职位总数，平均薪资
    sql = 'select count(ca_list.Id) as count_zw,avg(ca_list.zwyx) as avg_zwyx,ca_gsgm.gsgm_name from ca_list inner join ca_gsgm on ca_gsgm.Id=ca_list.gsgm_id group by gsgm_id order by count_zw desc'
    # 执行sql语句
    cursor.execute(sql)
    # 取出所有结果集
    gsgm_zwyx_list =cursor.fetchall()
    if gsgm_zwyx_list:
        returnDate['status'] = 1
        # 总职位数
        count_zw = []
        # 平均薪资
        avg_zw = []
        # 公司规模名
        gsgm_list = []
        # 循环遍历存入数据
        for item in gsgm_zwyx_list:
            count_zw.append({'name':item[2],'value':item[0]})
            avg_zw.append({'name':item[2],'value':round(item[1],2)})
            gsgm_list.append(item[2])
        returnDate['count_zw'] = count_zw
        returnDate['avg_zw'] = avg_zw
        returnDate['gsgm_list'] = gsgm_list
    cursor.close()
    return jsonify(returnDate)

# 公司性质薪资图页面（折线图）
# 参考链接：http://echarts.baidu.com/demo.html#line-marker
@app.route('/zwyx/gsxz_index')
def zwyx_gsxz_view():
    return render_template('zwyx_gsxz.html')
# 公司性质和薪资
@app.route('/zwyx/gsxz')
def show_zwyx_gsxz():
    #建立链接游标
    cursor=connect_mysql(conn)
    returnDate = {}
    # 查询地点和薪资的关系，职位总数，平均薪资
    sql = 'select count(ca_list.Id) as count_zw,avg(ca_list.zwyx) as avg_zwyx,ca_gsxz.gsxz_name,max(zwyx),min(zwyx) from ca_list inner join ca_gsxz on ca_gsxz.Id=ca_list.gsxz_id group by gsxz_id order by count_zw desc'
    # 执行sql语句
    cursor.execute(sql)
    # 取出所有结果集
    gsxz_zwyx_list = cursor.fetchall()
    if gsxz_zwyx_list:
        returnDate['status'] = 1
        # 总职位数
        count_zw = []
        # 平均薪资
        avg_zw = []
        # 公司规模名
        gsxz_list = []
        # 最大薪资
        max_xz = []
        # 最小薪资
        min_xz = []
        # 循环遍历存入数据
        for item in gsxz_zwyx_list:
            count_zw.append({'name': item[2], 'value': item[0]})
            avg_zw.append({'name': item[2], 'value': round(item[1], 2)})
            gsxz_list.append(item[2])
            max_xz.append(item[3])
            min_xz.append(item[4])
        #数据json化
        returnDate['count_zw'] = count_zw
        returnDate['avg_zw'] = avg_zw
        returnDate['gsxz_list'] = gsxz_list
        returnDate['max_xz'] = max_xz
        returnDate['min_xz'] = min_xz
    cursor.close()
    return jsonify(returnDate)

# 经验薪资图页面（雷达图）
# 参考链接：http://echarts.baidu.com/demo.html#radar-custom
@app.route('/zwyx/jy_index')
def zwyx_jy_view():
    return render_template('zwyx_jy.html')
# 经验和薪资
@app.route('/zwyx/jy')
def show_zwyx_jy():
    #建立链接游标
    cursor=connect_mysql(conn)
    returnDate = {}
    returnDate['status'] = 0
    sql = 'select count(ca_list.Id) as count_zw,avg(ca_list.zwyx) as avg_zwyx,ca_jy.jy_name,max(zwyx),min(zwyx) from ca_list inner join ca_jy on ca_jy.Id=ca_list.jy_id group by jy_id order by count_zw desc'
    # 执行sql语句
    cursor.execute(sql)
    # 取出所有结果集
    jy_zwyx_list = cursor.fetchall()
    if jy_zwyx_list:
        # 总职位数
        count_zw = []
        # 平均薪资
        avg_zw = []
        # 经验分类名
        jy_list = []
        # 最大薪资
        max_xz = []
        # 最小薪资
        min_xz = []
        # 循环遍历存入数据
        returnDate['status'] = 1
        for item in jy_zwyx_list:
            count_zw.append(item[0])
            avg_zw.append(round(item[1], 2))
            jy_list.append({'text':item[2]})
            max_xz.append(item[3])
            min_xz.append(item[4])
        #数据json化
        returnDate['count_zw'] = count_zw
        returnDate['avg_zw'] = avg_zw
        returnDate['jy_list'] = jy_list
        returnDate['max_xz'] = max_xz
        returnDate['min_xz'] = min_xz
    cursor.close()
    return jsonify(returnDate)

# 职位名称薪资图页面（象形柱图）
# 参考链接：http://echarts.baidu.com/demo.html#pictorialBar-dotted
@app.route('/zwyx/zwmc_index')
def zwyx_zwmc_view():
    return render_template('zwyx_zwmc.html')
# 职位名称和薪资
@app.route('/zwyx/zwmc')
def show_zwyx_zwmc():
    #建立链接游标
    cursor=connect_mysql(conn)
    returnDate = {}
    returnDate['status'] = 0
    sql = 'select count(ca_list.Id) as count_zw,avg(ca_list.zwyx) as avg_zwyx,ca_zwmc.zwmc_name,max(zwyx),min(zwyx) from ca_list inner join ca_zwmc on ca_zwmc.Id=ca_list.zwmc_id group by ca_list.zwmc_id order by count_zw desc'
    # 执行sql语句
    cursor.execute(sql)
    # 总职位数
    count_zw = {}
    # 平均薪资
    avg_zw = {}
    # 职位名
    zwmc_list = []
    # 最大薪资
    max_xz = {}
    # 最小薪资
    min_xz = {}
    zwmc_list.append('其他')
    count_zw['其他'] = 0
    avg_zw['其他'] = 0
    max_xz['其他'] = 0
    min_xz['其他'] = 0
    zwmc_zwyx_list=cursor.fetchall()
    #打开职位分类文本
    file = open('ca_list.txt', 'r')
    lines = file.readline()
    if zwmc_zwyx_list:
        #提取数据
        for row in zwmc_zwyx_list:
            #提取文本数据
            for item in lines.split():
                #判断是否包含
                if item in row[2]:
                    #如果判断职位列表里是否存在该项
                    if item in zwmc_list:
                        #存在则处理数据
                        count_zw[item] = count_zw[item] + row[0]
                        avg_zw[item] = round((avg_zw[item] + row[1]) / 2, 2)
                        max_xz[item] = max(max_xz[item], row[3])
                        min_xz[item] = min(min_xz[item], row[4])
                    else:
                        # 不存在则添加数据
                        zwmc_list.append(item)
                        count_zw[item] = row[0]
                        avg_zw[item] = round(row[1], 2)
                        max_xz[item] = row[3]
                        min_xz[item] = row[4]
                else:
                    #如果没有找到对应的分类，则增加相应数据
                    count_zw['其他'] = count_zw['其他'] + row[0]
                    #如果数据还没有对应数值，则增加第一条数据
                    if count_zw['其他'] == 0:
                        avg_zw['其他'] = row[1]
                    else:
                        avg_zw['其他'] = round((count_zw['其他'] + row[1]) / 2, 2)
                    max_xz['其他'] = max(max_xz['其他'], row[3])
                    min_xz['其他'] = min(min_xz['其他'], row[4])
        #重新构建数据
        return_count_zw=[]
        return_avg_zw = []
        return_max_xz = []
        return_min_xz = []
        #重新规划数据
        for value in count_zw:
            return_count_zw.append(count_zw[value])
        for value in avg_zw:
            return_avg_zw.append(avg_zw[value])
        for value in max_xz:
            return_max_xz.append(max_xz[value])
        for value in min_xz:
            return_min_xz.append(min_xz[value])
        #json数据
        returnDate['status'] = 1
        returnDate['count_zw'] = return_count_zw
        returnDate['avg_zw'] = return_avg_zw
        returnDate['zwmc_list'] = zwmc_list
        returnDate['max_xz'] = return_max_xz
        returnDate['min_xz'] = return_min_xz
    cursor.close()
    return jsonify(returnDate)

#公司数和地点关系（散点图）
#参考链接：http://echarts.baidu.com/demo.html#scatter-map-brush
@app.route('/dd/gsmc_index')
def dd_gsmc_view():
    return render_template('dd_gsmc.html')
# 公司数和地点
@app.route('/dd/gsmc')
def show_dd_gsmc():
    #建立链接游标
    cursor=connect_mysql(conn)
    returnDate = {}
    returnDate['status'] = 0
    sql = 'select count(distinct ca_list.gsmc_id) as count_gs,ca_dd.dd_name from ca_list inner join ca_dd on ca_dd.Id=ca_list.dd_id group by ca_list.dd_id'
    # 执行sql语句
    cursor.execute(sql)
    # 公司数
    count_gs = []
    gsmc_dd_list = cursor.fetchall()
    if gsmc_dd_list:
        returnDate['status'] = 1
        for item in gsmc_dd_list:
            count_gs.append({'name':item[1],'value':item[0]})
        returnDate['count_gs']=count_gs
    cursor.close()
    return jsonify(returnDate)

# 职位数和地点页面（热力图）
#参考链接：http://echarts.baidu.com/demo.html#heatmap-map
@app.route('/dd/zwmc_index')
def dd_zwmc_view():
    return render_template('dd_zwmc.html')
# 职位名称和薪资
@app.route('/dd/zwmc')
def show_dd_zwmc():
    #建立链接游标
    cursor=connect_mysql(conn)
    returnDate = {}
    returnDate['status'] = 0
    sql = 'select count(distinct ca_list.zwmc_id) as count_zw,ca_dd.dd_name from ca_list inner join ca_dd on ca_dd.Id=ca_list.dd_id group by ca_list.dd_id'
    # 执行sql语句
    cursor.execute(sql)
    # 职位数
    count_zw = []
    gsmc_dd_list = cursor.fetchall()
    if gsmc_dd_list:
        returnDate['status'] = 1
        for item in gsmc_dd_list:
            count_zw.append({'name': item[1], 'value': item[0]})
        returnDate['count_zw'] = count_zw
    cursor.close()
    return jsonify(returnDate)

#职位类型相关关系（综合图）
# 参考链接：http://echarts.baidu.com/demo.html#watermark
@app.route('/dd/type_index')
def dd_type_view():
    return render_template('dd_type.html')
# 公司数和地点
@app.route('/dd/type')
def show_dd_type():
    #建立链接游标
    cursor=connect_mysql(conn)
    returnDate = {}
    returnDate['status'] = 0
    #查询职位类型与地点、职位、公司、平均薪资分布总数的关系
    sql = 'SELECT count(distinct ca_list.dd_id),count(distinct ca_list.zwmc_id),count(distinct ca_list.gsmc_id),avg(ca_list.zwyx),ca_type.`name` from ca_list inner join ca_type ON ca_type.Id =ca_list.type_id GROUP BY ca_list.type_id'
    # 执行sql语句
    cursor.execute(sql)
    type_dd_list = cursor.fetchall()
    # 分布地点数
    dd_type ={}
    # 分布地点最大数
    count_dd_type = 0
    # 职位数
    zw_type = {}
    # 公司数
    gs_type = {}
    # 平均薪资
    avg_xz = {}
    # 平均薪资最大数
    max_avg_xz = 0
    #总平均薪资
    all_avg=0
    returnDate['status'] = 1
    #遍历数据
    for item in type_dd_list:
        dd_type[item[4]]=item[0]
        count_dd_type=max(count_dd_type,item[0])
        zw_type[item[4]]=item[1]
        gs_type[item[4]]=item[2]
        avg_xz[item[4]]=round(item[3],2)
        max_avg_xz=max(max_avg_xz,round(item[3],2))
        if all_avg==0:
            all_avg=round(item[3],2)
        else:
            all_avg=round((all_avg+round(item[3],2))/2,2)
    #Json化数据
    returnDate['dd_type']=dd_type
    returnDate['zw_type'] = zw_type
    returnDate['gs_type'] = gs_type
    returnDate['avg_xz'] = avg_xz
    returnDate['all_avg']=round(all_avg,2)
    returnDate['count_dd_type'] = count_dd_type+20
    returnDate['max_avg_xz'] = round(max_avg_xz+1000.0,2)
    cursor.close()
    return jsonify(returnDate)

# 入口
if __name__ == '__main__':
    # 调试模式
    app.debug = True
    # 外部可访问的服务器
    app.run(host='0.0.0.0')
