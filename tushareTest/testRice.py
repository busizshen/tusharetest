def stop(context):
    # 循环查看持仓的每个股票
    for stock in context.portfolio.positions:
        # 如果股票最新价格除以平均成本小于0.8，即亏损超过20%
        if context.portfolio.positions[stock].price/context.portfolio.positions[stock].avg_cost < 0.8:
            # 调整stock的持仓为0，即卖出
            # order_target(stock, 0)
            # 输出日志：股票名 止损
            print ("\n%s 止损" % stock)