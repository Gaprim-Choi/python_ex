import pandas as pd
import matplotlib.pyplot as plt
s1 = pd.Series([1,2,3,4,5,6,7,8,9,10])
print(s1)
s1.plot()
plt.show()
s2 = pd.Series([1,2,3,4,5,6,7,8,9,10], index = pd.date_range('2019-01-01', periods=10))
print(s2)
s2.plot()
plt.show()
s2.plot(grid=True)
plt.show()
df_rain = pd.read_csv('./ch14_numpy/sea_rain1.csv', index_col="연도" )
print(df_rain)


import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'# '맑은 고딕'으로 설정
matplotlib.rcParams['axes.unicode_minus'] = False
df_rain.plot()
plt.show()
rain_plot = df_rain.plot(grid = True, style = ['r--*', 'g-o', 'b:*', 'm-.p'])
rain_plot.set_xlabel("연도")
rain_plot.set_ylabel("강수량")
rain_plot.set_title("연간 강수량")
plt.show()
year = [2006, 2008, 2010, 2012, 2014, 2016] # 연도
area = [26.2, 27.8, 28.5, 31.7, 33.5, 33.2] # 1인당 주거면적
table = {'연도':year, '주거면적':area}
df_area = pd.DataFrame(table, columns=['연도', '주거면적'])
print(df_area)

df_area.plot(x='연도', y='주거면적', grid = True, title = '연도별 1인당 주거면적')
plt.show()
