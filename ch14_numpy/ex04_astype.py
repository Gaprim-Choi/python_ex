# 배열의 데이터 타입 변환

import numpy as np

print(np.array(['1.5','0.62','2','3.14','3.141592']))
"""
['1.5' '0.62' '2' '3.14' '3.141592']
"""

str_a1 = np.array(['1.567','0.123','5.123','9','8'])
num_a1 = str_a1.astype(float)
print(str_a1) # 저장한 원본 문자 타입 출력
"""
['1.567' '0.123' '5.123' '9' '8']
"""
print(num_a1) # 문자 타입에서 float 타입으로 변환하여 출력 출력

"""
[1.567 0.123 5.123 9.    8.   ]
"""

print(str_a1.dtype) #<U5
print(num_a1.dtype) #float64

str_a2 = np.array(['1','3','5','7','9'])
num_a2 = str_a2.astype(int)

print(num_a2) # 문자 타입에서 int 타입으로 변환하여 출력 출력
"""
[1 3 5 7 9]
"""

print(str_a2.dtype) #<U1
print(num_a2.dtype) #int32

num_f1 = np.array([10,21,0.549,4.75,5.98])
num_i1 = num_f1.astype(int)


print(num_i1) # float 를 int 로 변환 하여 출력
"""
[10 21  0  4  5]
"""

print(num_f1.dtype) # float64
print(num_i1.dtype) # int32