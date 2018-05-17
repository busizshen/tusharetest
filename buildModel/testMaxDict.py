#coding=utf-8
import pandas as pd

# dict = {'Alice': 2341, 'Beth': 9102, 'Cecil': 3258}
# dict = sorted(dict.items(),key=lambda item:item[1],reverse=1)
# for i in range(0,2):
#     print(dict[i])

dict=[[1,2,3,4,5,6],[2,3,4,5,6,7],[3,4,5,6,7,8],[4,5,6,7,8,9],[5,6,7,8,9,10]]
datas=pd.DataFrame(dict)
i = 0
for data in datas:
    print(data.iloc[i].values[0])
    print(data.iloc[i].values[1])
    i = i+1