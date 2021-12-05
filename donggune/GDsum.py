import matplotlib
import matplotlib.pyplot as plt
from numpy.core.numeric import NaN
import pandas as pd
import numpy as np
 
from math import pi
from matplotlib.path import Path
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D


""" --------------------Excel Data 입력---------------------- """
df = pd.read_excel('./donggune/testV1.xlsx', sheet_name='최종(적합성)')
print(df)
df = df.replace({'좋아함':1,'잘할수있음':1,'하고싶음':1,'그렇다':1})
df = df.replace({'관심없음':0,'싫어함':0,'중간정도':0,'잘할수없음':0,'관심없음':0,'하고싶지않음':0,'아니다':0})
df = df.transpose()
print(df)

""" --------------------항목별 데이터 재정리---------------------- """
df_S = df[(df[0] == 'S')]
df_S_sum = pd.DataFrame(df_S.sum(axis=0), columns=['S_항목'])
df_A = df[(df[0] == 'A')]
df_A_sum = pd.DataFrame(df_A.sum(axis=0), columns=['A_항목'])
df_R = df[(df[0] == 'R')]
df_R_sum = pd.DataFrame(df_R.sum(axis=0), columns=['R_항목'])
df_I = df[(df[0] == 'I')]
df_I_sum = pd.DataFrame(df_I.sum(axis=0), columns=['I_항목'])
df_C = df[(df[0] == 'C')]
df_C_sum = pd.DataFrame(df_C.sum(axis=0), columns=['C_항목'])
df_E = df[(df[0] == 'E')]
df_E_sum = pd.DataFrame(df_E.sum(axis=0), columns=['E_항목'])
total = pd.concat([df_S_sum,df_A_sum,df_R_sum,df_I_sum,df_C_sum,df_E_sum],axis=1)
total = total.drop([0])
print(total)


""" --------------------출력될 그래프 font 설정---------------------- """
matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # '맑은 고딕'으로 설정
matplotlib.rcParams['axes.unicode_minus'] = False
""" matplotlib.rcParams["figure.figsize"] = (15, 4) """


""" --------------------전체 질문자에 대한 그래프 생성---------------------- """
for i, j in total.iterrows():
    labels = total.columns[:]
    num_labels = len(labels)
    
    angles = [x/float(num_labels)*(2*pi) for x in range(num_labels)] ## 각 등분점
    angles += angles[:1] ## 시작점으로 다시 돌아와야하므로 시작점 추가
    print(angles)
    
    my_palette = plt.cm.get_cmap("Set2", len(total.index))
 
    fig = plt.figure(figsize=(8,8))
    fig.set_facecolor('white')
    ax = fig.add_subplot(polar=True)
    color = 'green'
    print(i)
    data = total.iloc[i-1].tolist()
    data += data[:1]
    print (data)
    
    if data != NaN:
        ax.set_theta_offset(pi / 2) ## 시작점
        ax.set_theta_direction(-1) ## 그려지는 방향 시계방향

        plt.xticks(angles[:-1], labels, fontsize=13) ## 각도 축 눈금 라벨
        ax.tick_params(axis='x', which='major', pad=15) ## 각 축과 눈금 사이에 여백을 준다.


        ax.set_rlabel_position(0) ## 반지름 축 눈금 라벨 각도 설정(degree 단위)
        plt.yticks([0,8,17,26,34],['0','8','17','26','34'], fontsize=10) ## 반지름 축 눈금 설정
        plt.ylim(0,34)

        ax.plot(angles, data, color=color, linewidth=2, linestyle='solid', label='검사자 기록') ## 레이더 차트 출력
        ax.fill(angles, data, color=color, alpha=0.4) ## 도형 안쪽에 색을 채워준다.
        print(angles)
        print(ax)
plt.show()
