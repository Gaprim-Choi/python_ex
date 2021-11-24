import numpy as np

A = np.array([0,1,2,3]).reshape(2,2)
print(A)
"""
[[0 1]
 [2 3]]
"""

B = np.array([3,2,0,1]).reshape(2,2)
print(B)
"""
[[3 2]
 [0 1]]
"""

print(A.dot(B))

"""
[[0 1]
 [6 7]]
"""

print(np.dot(A,B))

"""
[[0 1]
 [6 7]]
"""

print(np.transpose(A)) # 대각선 축 기준 반전 표현
"""
[[0 2]
 [1 3]]
"""

#행렬 A의 역행렬
#A = [[a,b]
#     [c,d]]
#Aⁿ =1/(ad-bc) A^t (※n=-1)