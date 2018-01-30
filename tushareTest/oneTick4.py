import os
import pandas as pd

def make_train_test_csv(cls, orgin_data_path=None, all_data_path=None, time_step=60):
    """
    制作股票分类数据
    orgin_data_path:原始数据存放路径
    all_data_path:制作成可被算法接收的文件存放路径
    """
    basic_path = os.path.dirname(os.path.abspath(__file__))
    # 初始化源文件路径和存储文件路径
    if orgin_data_path is None:
        orgin_data_path = os.path.join(basic_path, "origin_data.csv")
    if all_data_path is None:
        all_data_path = os.path.join(basic_path, "all_data.csv")
    # 读取原始数据，只保留需要使用的列
    total_data = pd.read_csv(orgin_data_path,
                             usecols=["open_hfq", "high_hfq", "low_hfq", "close_hfq", "turnover", "volume",
                                      "cir_market_value", "stock_date", "stock_num"])
    # 根据股票代码排序，相同的股票代码按照交易日期排序。
    # inplace参数表示不需要返回排序后的结果，直接覆盖原变量即可
    total_data.sort_values(by=['stock_num', 'stock_date'], inplace=True)

    # 根据股票代码分组
    g_stock_num = total_data.groupby(by=["stock_num"])
    # 针对每一组股票，分别计算收益gate，其定义为：(下下一个交易日的开盘价 / 下一个交易日的开盘价) - 1
    # 对gate乘以100，使之变成百分比形式(0.09 -> 9，表示9%)
    # 使用np.round函数保存两位小数，之后的数字丢弃(9.8346474 - > 9.83)
    total_data["gate"] = np.round((100 * (g_stock_num.shift(-2)["open_hfq"] / g_stock_num.shift(-1)["open_hfq"] - 1)),
                                  2)
    # 重新调整列的顺序，为接下来处理成输入、输出形式做准备
    total_data = total_data[
        ["open_hfq", "high_hfq", "low_hfq", "close_hfq", "turnover", "volume", "cir_market_value", "gate", "stock_date",
         "stock_num"]]

    # 将调整列顺序后的代码，重新按照股票代码分组
    g_stock_num = total_data.groupby(by=["stock_num"])

    # 拿time_step个交易日的数据（默认为60个交易日），进行标准化
    def func_stand(data_one_stock_num, time_step):
        # 通过apply进入函数内的数据，其股票名为data_one_stock_num.name，类型为pd.dataFrame
        # 即，进入此函数的数据为所有名为data_one_stock_num.name的集合
        # dataFrame.shape:(num , 11), num是这个股票出现的次数

        for colu_name in data_one_stock_num.columns:
            if colu_name in ["gate", "stock_date", "stock_num"]:
                continue
            # 只针对输入数据进行标准化，标准化算法为: (原始数据 - 平均值) / 标准差
            # 这里每一次for循环，都拿出了1列数据，针对这一列进行标准化并覆盖原数据
            data_one_stock_num[colu_name] = (
            (data_one_stock_num[colu_name] - data_one_stock_num[colu_name].rolling(time_step).mean()) /
            data_one_stock_num[colu_name].rolling(time_step).std())
        return data_one_stock_num

    # 将经过标准化的数据处理成训练集和测试集可接受的形式
    def func_train_test_data(data_one_stock_num, time_step):
        print("正在处理的股票代码:code:%06d" % data_one_stock_num.name)

        # 提取输入列（对应train_x）
        data_temp_x = data_one_stock_num[
            ["open_hfq", "high_hfq", "low_hfq", "close_hfq", "turnover", "volume", "cir_market_value"]]
        # 提取输出列（对应train_y）
        data_temp_y = data_one_stock_num[["gate", "stock_date", "stock_num"]]
        data_res = []
        # for循环从time_step - 1开始，因为前time_step - 1个数据不满足time_step条件
        # 例如：time_step为60，即需要60个交易日的数据制成训练集的一个输入，但某只股票因为停牌等原因，只有50个交易日的数据。那么它就可以跳过了，不满足最低数目的要求
        for i in range(time_step - 1, len(data_temp_x.index)):
            data_res.append(data_temp_x.iloc[i - time_step + 1: i + 1].values.reshape(1, time_step * 7).tolist() +
                            data_temp_y.iloc[i][["gate", "stock_date", "stock_num"]].values.reshape(1, 3).tolist())
        if len(data_res) != 0:
            # 使用末尾添加的形式，将各个股票的数据依次添加进设定的路径中。
            # index参数表示是否需添加一列序号，header表示是否需要添加列头，mode表示选择哪一种模型进行csv操作（类似于open函数的模型）
            pd.DataFrame(data_res).to_csv(all_data_path, index=False, header=False, mode="a")
        return data_one_stock_num

    # 数据标准化
    data_after_stand = g_stock_num.apply(func_stand, time_step=time_step)
    data_after_stand.dropna(inplace=True)
    # 将数据转成训练集合的形式
    g_stock_num = data_after_stand.groupby(by=["stock_num"])
    # 清空接收路径下的文件，初始化列名
    pd.DataFrame({"0": [], "1": []}).to_csv(all_data_path, index=False)
    g_stock_num.apply(func_train_test_data, time_step=time_step)