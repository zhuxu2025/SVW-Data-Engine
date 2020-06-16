"""
Action3: 对汽车质量数据进行统计
数据集：car_complain.csv
600条汽车质量投诉
Step1，数据加载
Step2，数据预处理
拆分problem类型 => 多个字段
Step3，数据统计
对数据进行探索：品牌投诉总数，车型投诉总数
哪个品牌的平均车型投诉最多
"""

import pandas as pd
result=pd.read_csv('car_complain.csv')
#print(result)
#数据预处理
problems=result.problem.str.get_dummies(',')
tags=problems.columns
result = result.drop('problem', 1).join(problems)

# 按品牌统计投诉总数
df1= result.groupby(['brand'])['id'].agg(['count'])
df1['品牌投诉总数']=df1.sort_values('count', ascending=False)
print(df1)
df1.to_csv("./brand.csv",index=False)

# 按车型统计投诉总数
df2= result.groupby(['car_model'])['id'].agg(['count'])
df2['车型投诉总数']=df2.sort_values('count',ascending=False)
print(df2)
df2.to_csv("./car_model.csv",index=False)

# 按品牌车型投诉平均数
df3 = result.groupby(['brand']).car_model.nunique()
df4 = pd.merge(df3, df1, on=['brand'])
df4['品牌车型投诉平均数']=df4.apply(lambda x:x[1]/x[0],axis=1)
df4=df4.sort_values(by='品牌车型投诉平均数',ascending=False)
print(df4)
df4.to_csv("./average.csv",index=False)