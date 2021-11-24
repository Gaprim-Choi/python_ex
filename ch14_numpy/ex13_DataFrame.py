# DataFrame을 활용한 데이터 생성
# DataFrame: Pandas에서 제공하는 표(table)와 같은 2차원 데이터 처리를 위한 자료구조
import numpy as np
from numpy.core.defchararray import index
import pandas as pd
from pandas.core.frame import DataFrame

print(pd.DataFrame([[0,1,2],[3,4,5],[6,7,8]]))
"""
   0  1  2
0  0  1  2
1  3  4  5
2  6  7  8
"""
data_list = np.array([[10,20,30],[40,50,60],[70,80,90]])
print(data_list)
"""
[[10 20 30]
 [40 50 60]
 [70 80 90]]
"""

print(pd.DataFrame(data_list))
"""
    0   1   2
0  10  20  30
1  40  50  60
2  70  80  90
"""

data = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
index_date = pd.date_range('2019/09-01',periods=4)
columns_list=['A','B','C']
print(pd.DataFrame(data,index=index_date,columns=columns_list))
"""
             A   B   C
2019-09-01   1   2   3
2019-09-02   4   5   6
2019-09-03   7   8   9
2019-09-04  10  11  12
"""

table_data = {'연도':[2015,2016,2016,2017,2017],
              '지사':['한국','한국','미국','한국','미국'],
              '고객 수':[200,250,450,300,500]}

print(table_data)
"""
{'연도': [2015, 2016, 2016, 2017, 2017],
'지사': ['한국', '한국', '미국', '한국', '미국'],
'고객 수': [200, 250, 450, 300, 500]}
"""

print(pd.DataFrame(table_data))
"""
     연도  지사  고객 수
0  2015  한국   200
1  2016  한국   250
2  2016  미국   450
3  2017  한국   300
4  2017  미국   500
"""