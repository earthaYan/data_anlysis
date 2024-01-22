import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# 加载数据
df_trade=pd.read_csv('sam_tianchi_mum_baby_trade_history.csv')
df_baby=pd.read_csv('sam_tianchi_mum_baby.csv')
# 数据处理
df_trade['day']=pd.to_datetime(df_trade.day.astype('str'))
df_trade['year']=df_trade.day.dt.year
df_trade['quarter']=df_trade.day.dt.quarter
df_trade['month']=df_trade.day.dt.month
df_trade=df_trade[(df_trade.buy_mount>=1)&(df_trade.buy_mount<=189)]
df_baby=df_baby[df_baby.gender!=2]
df_baby['birthday']=pd.to_datetime(df_baby.birthday.astype('str'))
df_baby=df_baby[df_baby.birthday>'2010-01-01']
# 数据分析
# 根据时间节点查看销量趋势
# year_stats=df_trade.groupby(by='year')['buy_mount'].sum()
# 创建 Matplotlib 图形对象
# plt.figure(figsize=(10,5))
# 每年销售量
# sns.barplot(x=year_stats.index,y=year_stats.values)
# plt.title('sales for years')
# plt.xlabel('Year')
# plt.ylabel('sales')
# plt.show()
# 每季度
# year_quarter_stats = df_trade.groupby(by=['year', 'quarter'])['buy_mount'].sum()
# plt.figure(figsize=(10, 5))
# x_list = [str(idx[0]) + "/Q" + str(idx[1]) for idx in year_quarter_stats.index]
# y_list = [int(value) for value in year_quarter_stats.values]
# sns.barplot(x=x_list, y=y_list)
# plt.title("sales for Year/Season")
# plt.xlabel("(Year/Season)")
# plt.ylabel("sales")
# plt.show()
# 每月销售分析
# year_month_stats = df_trade.groupby(by=['year', 'month'])['buy_mount'].sum()
# plt.figure(figsize=(30, 5))
# x_list = [str(idx[0]) + "/" + str(idx[1]) for idx in year_month_stats.index]
# y_list = [int(value) for value in year_month_stats.values]
# sns.barplot(x=x_list, y=y_list)
# plt.title("sales for Year/Month")
# plt.xlabel("(Year/Month)")
# plt.ylabel("sales")
# plt.show()
# 每日销量
df_trade_201312 = df_trade[(df_trade.day >= '2013-12-01') & (df_trade.day <= '2013-12-30')]
day_stats = df_trade_201312.groupby(by='day')['buy_mount'].sum()

plt.figure(figsize=(30, 5))
x_list = [str(idx.month) + '-' + str(idx.day) for idx in day_stats.index]
y_list = [int(value) for value in day_stats.values]
sns.barplot(x=x_list, y=y_list)

plt.title("sales for Day(2013/12)")
plt.xlabel("Date")
plt.ylabel("sales")
plt.show()
