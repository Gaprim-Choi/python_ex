# pandas = excel 테이블 구조와 비슷한 자료구조
# Series를 활용한 데이터 생성

from numpy.lib.function_base import insert
import pandas as pd
import numpy as np

s1 = pd.Series([10,20,30,40,50])
print(s1)
"""
0    10
1    20
2    30
3    40
4    50
dtype: int64
"""

print(s1.index) 
"""RangeIndex(start=0, stop=5, step=1)"""

print(s1.values) 
"""[10 20 30 40 50]"""

s2 = pd.Series(['a','b','c', 1, 2, 3])
print(s2)
"""
0    a
1    b
2    c
3    1
4    2
5    3
dtype: object
"""

s3 = pd.Series([np.nan, 10, 30])
print(s3)
"""
0     NaN
1    10.0
2    30.0
dtype: float64
"""

index_data = ['2018-10-07','2018-10-08','2018-10-09','2018-10-10']
s4=pd.Series([200,195,np.nan,205],index=index_data)
print(s4)
"""
2018-10-07    200.0
2018-10-08    195.0
2018-10-09      NaN
2018-10-10    205.0
dtype: float64
"""

s5 =pd.Series({'국어':100,'영어':95,'수학':80})
print(s5)
"""
국어    100
영어     95
수학     80
dtype: int64
"""