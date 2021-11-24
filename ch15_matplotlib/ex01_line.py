import matplotlib.pyplot as plt
data1 = [10, 14, 19, 20, 25]
plt.plot(data1)
plt.show()


import numpy as np
x = np.arange(-4.5, 5, 0.5) # 배열 x 생성. 범위: -4.5, 5, 0.5씩 증가
y = 2*x**2 # 수식을 이용해 배열 x에 대응하는 배열 y 생성

plt.plot(x,y)
plt.show()