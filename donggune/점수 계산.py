import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('./donggune/testUser.xlsx', sheet_name=0)
jj = pd.read_excel('./donggune/testUser.xlsx', sheet_name=1)
jm = pd.read_excel('./donggune/testUser.xlsx', sheet_name=2)

# 직업 적성에 대한 각 항목에 대한 데이터값 연산 전 정리
jj = jj.replace('A', 3)
jj = jj.replace('B', 2)
jj = jj.replace('C', 1)
jj = jj.drop(['문항'],axis=1)

# 직업 만족도에 대한 각 항목에 대한 데이터값 연산 전 정리
jm = jm.replace('A', 3)
jm = jm.replace('B', 2)
jm = jm.replace('C', 1)
jm = jm.drop(['문항'],axis=1)

matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # '맑은 고딕'으로 설정
matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.rcParams["figure.figsize"] = (15, 4)

product_plot = jj.plot(grid=True, title='각 문항별 점수')
product_plot = jm.plot(grid=True, title='각 문항별 점수')
plt.ylim([0, 5])
plt.show()


jj = jj.transpose()
jm = jm.transpose()

# 만족도 조사에 대한 합산 값 연산
jj_sum = pd.DataFrame(jj.sum(axis=1)/3, columns=['평균'])
jm_sum = pd.DataFrame(jm.sum(axis=1)/3, columns=['평균'])

# 각 설문에 대한 답변 점수의 총 합산값 출력
print('당신의 직업 적성 평가는\n' ,jj_sum.loc['답변'])
print('당신의 직업 만족도 평가는\n',jm_sum.loc['답변'])