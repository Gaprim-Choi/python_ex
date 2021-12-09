import matplotlib
import matplotlib.pyplot as plt
from numpy.core.numeric import NaN
import pandas as pd
from PIL import Image
 
from math import pi
from matplotlib.path import Path
from matplotlib.spines import Spine 
from pandas.core.reshape.melt import wide_to_long


pd.set_option('display.max_row',20)
pd.set_option('display.max_columns',20)

""" --------------------Excel Data 입력---------------------- """
df = pd.read_excel('./donggune/testV1.xlsx', sheet_name='최종(적합성)')
jd = pd.read_excel('./donggune/2. 직업코드표.xlsx', sheet_name='진로코드분류표 (3)')
ja = pd.read_excel('./donggune/3. 코드 유형별 특징.xlsx', sheet_name=0)
df = df.replace({'좋아함':1,'잘할수있음':1,'하고싶음':1,'그렇다':1})
df = df.replace({'관심없음':0,'싫어함':0,'중간정도':0,'잘할수없음':0,'관심없음':0,'하고싶지않음':0,'아니다':0})
df = df.transpose()
print(df)

""" --------------------항목별 데이터 재정리---------------------- """
df_S = df[(df[0] == 'S')]
df_S_sum = pd.DataFrame(df_S.sum(axis=0), columns=['S'])
df_A = df[(df[0] == 'A')]
df_A_sum = pd.DataFrame(df_A.sum(axis=0), columns=['A'])
df_R = df[(df[0] == 'R')]
df_R_sum = pd.DataFrame(df_R.sum(axis=0), columns=['R'])
df_I = df[(df[0] == 'I')]
df_I_sum = pd.DataFrame(df_I.sum(axis=0), columns=['I'])
df_C = df[(df[0] == 'C')]
df_C_sum = pd.DataFrame(df_C.sum(axis=0), columns=['C'])
df_E = df[(df[0] == 'E')]
df_E_sum = pd.DataFrame(df_E.sum(axis=0), columns=['E'])
total = pd.concat([df_S_sum,df_A_sum,df_R_sum,df_I_sum,df_C_sum,df_E_sum],axis=1)
total = total.drop([0])

""" --------------------다각형 그래프의 사용될 이미지 소스 설정---------------------- """
box1 = {'boxstyle': 'round',
        'ec': (1.0, 0.5, 0.5),
        'fc': (1.0, 0.8, 0.8)}

font1 = {'family': 'Malgun Gothic',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16}


""" --------------------출력될 그래프 font 설정---------------------- """
matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # '맑은 고딕'으로 설정
matplotlib.rcParams['axes.unicode_minus'] = False
""" matplotlib.rcParams["figure.figsize"] = (15, 4) """



k=0
""" --------------------전체 질문자에 대한 그래프 생성---------------------- """
for i, j in total.iterrows():#임의의 변수 i,j를 total List 수량만큼 반복하는 for문생성

    
    labels = total.columns[:]#total의 컬럼과 동일한 수량,동일한 내용의 labels 리스트 생성
    num_labels = len(labels)#labels 리스트의 수량 카운트
    
    angles = [x/float(num_labels)*(2*pi) for x in range(num_labels)] ## 각 등분점
    angles += angles[:1] ## 시작점으로 다시 돌아와야하므로 시작점 추가

    ##이미지 면적, 배경 및 도형 색상 설정
    fig = plt.figure(figsize=(8,8)) 
    fig.set_facecolor('white')
    ax = fig.add_subplot(polar=True)
    color = 'green'

    data = total.iloc[i-1].tolist()# 
    data += data[:1]# 다각형 그래프의 원점으로 돌아오는 선을 그리기 위해 시작점을 한번 더 생성
    
    if data != NaN:
        ax.set_theta_offset(pi / 2) ## 시작점
        ax.set_theta_direction(-1) ## 그려지는 방향 시계방향

        plt.xticks(angles[:-1], labels, fontsize=13) ## 각도 축 눈금 라벨
        ax.tick_params(axis='x', which='major', pad=15) ## 각 축과 눈금 사이에 여백을 준다.


        ax.set_rlabel_position(0) ## 반지름 축 눈금 라벨 각도 설정(degree 단위)
        plt.yticks([0,8,17,26,34],['0','8','17','26','34'], fontsize=10) ## 반지름 축 눈금 설정
        plt.ylim(0,34)

        ax.plot(angles, data, color=color, linewidth=2, linestyle='solid', label='검사자 '+str(i)+' 검사 기록') ## 레이더 차트 출력
        ax.fill(angles, data, color=color, alpha=0.4) ## 도형 안쪽에 색을 채워준다.
        for x, y, name in zip(angles, data, data): ## 도형 각 점에 data 값을 가지는 라벨 표현
            plt.text(x, y, name, bbox=box1) 
    plt.savefig('./donggune/imgGraph/검사자'+str(i)+'의 검사그래프', dpi=300) ## 결과 그래프를 이미지로 저장
k=0
for i in total.iterrows():
    
    k= k+1

    total_new = total.transpose() ## 데이터 정리를 위한 배열 재 정리
    test = total_new.sort_values(by=k, ascending=False).head(4) ## 검사자의 검사결과를 오름차순 점수로 정렬/상위 N개 추출
    ori_type = df[k][1]## 검사자의 검사결과를 오름차순 점수로 정렬/상위 N개 추출
    사용자정보 = str(k)+'번 참가자님의 직업 코드는' + ori_type +' 입니다.' 
    검사결과 = ''

    # 각 항목별 상위 분류에 대해 Text 출력을 위해 글로 정리
    if (test[k][0] == test[k][1] == test[k][2])or(test[k][1] == test[k][2] == test[k][3]):
        type_sum1 = '재검사가 필요한 검사자 입니다.'
    elif test[k][0] == test[k][1]:
        type_sum1 = test.index[0] + test.index[1]
        type_sum2 = test.index[1] + test.index[0]
    elif test[k][1] == test[k][2]:
        type_sum1 = test.index[0] + test.index[1]
        type_sum2 = test.index[0] + test.index[2]
    else:
        type_sum1 = test.index[0] + test.index[1]
        type_sum2 = 'nan'
    
    if type_sum1 == '재검사가 필요한 검사자 입니다.':
        검사결과 = '재검사가 필요한 검사자 입니다.'
    else:
        if type_sum2 in 'nan':
            검사결과 = '당신의 적성코드는 "'+ type_sum1 +'" 입니다.'
        else:
            검사결과 = '당신의 적성코드는 "'+ type_sum1 + "," + type_sum2 +'" 입니다.'


    listI = [type_sum1 , type_sum2]
    for i in range(len(type_sum1)):
        typeStr = listI[i]
        if typeStr in 'nan':
            break
        elif ori_type[0] == typeStr[0]:
            if ori_type[1] == typeStr[1]:
                str1 = '매우 높음'
            else:
                str1 = '높음'
        elif ori_type[1] == typeStr[0]:
            if ori_type[0] == typeStr[1]:
                str1 = '보통'
            else:
                str1 = '낮음'
        elif typeStr[1] in ori_type:
            str1 = '매우 낮음'
        else:
            str1 = '일치하지 않음'
        strX = '당신의 직업코드 "' + ori_type + '"과(와)' + listI[i] + " 의 일치도는 "+ str1 +"입니다."
        
        if i == 0:
            일치율1 = strX
            str1 = listI[i]
            일치율2 = 'nan'
        else :
            일치율2 = strX
            str2 = listI[i]
    
    testStr = ja.filter(ja.filter(regex=test.index[0]))
    testStr = str(testStr.loc[0])
    testStr = testStr.replace('\nName: 0, dtype: object','')
    타입성향1 = testStr
    testStr = ja.filter(ja.filter(regex=test.index[1]))
    testStr = str(testStr.loc[0])
    testStr = testStr.replace('\nName: 0, dtype: object','')
    타입성향2 = testStr
    testStr = ja.filter(ja.filter(regex=test.index[2]))
    testStr = str(testStr.loc[0])
    testStr = testStr.replace('\nName: 0, dtype: object','')
    타입성향3 = testStr

    fig, ax =plt.subplots(1,1, figsize=(15,10))

    if 일치율2 == 'nan':
        data=[['사용자정보',사용자정보],
              ['검사결과',검사결과],
              ['일치도',일치율1],
              ['귀하의 성향1',타입성향1],
              ['귀하의 성향2',타입성향2]]
        m = 3
    else:
        m = 4
        if str1[1] == str1[2]:
            data=[['사용자정보',사용자정보],
                  ['검사결과',검사결과],
                  ['일치도',일치율1],
                  ['일치도',일치율2],
                  ['귀하의 성향1',타입성향1],
                  ['귀하의 성향2',타입성향2]]
            m = 4
        else:
            data=[['사용자정보',사용자정보],
                  ['검사결과',검사결과],
                  ['일치도',일치율1],
                  ['일치도',일치율2],
                  ['귀하의 성향1',타입성향1],
                  ['귀하의 성향2',타입성향2],
                  ['귀하의 성향2',타입성향3]]
                  
    column_labels=["기준", "결과"]
    ax.axis('off')
    test = ax.table(cellLoc="left", cellText=data,colLabels=column_labels,loc="center")
    
    cellDict = test.get_celld()
    for i in range(0,len(column_labels)):
        print(i)
        cellDict[(0,i)].set_height(.05)
        l=0
        for j in range(1,len(data)+1):
            if l < m:
                cellDict[(j,i)].set_height(.05)
            else :
                cellDict[(j,i)].set_height(0.1)
            l=l+1
    fig = plt.gcf()
    test.auto_set_font_size(False)
    test.set_fontsize(5)
    test.scale(0.6, 0.6)
    plt.savefig('./donggune/imgChart/검사자'+str(k)+'의 검사결과표.png', bbox_inches= None, dpi=300 )

k=0
for i in total.iterrows():
    k= k+1
    print(k)
    image1 = Image.open('./donggune/imgGraph/검사자'+str(k)+'의 검사그래프.png')
    image2 = Image.open('./donggune/imgChart/검사자'+str(k)+'의 검사결과표.png')
    plt.subplot(2, 1, 1)
    plt.imshow(image1)
    plt.title('검사자'+str(k)+'의 검사그래프')
    plt.axis("off")
    plt.subplot(2, 1, 2)
    plt.imshow(image2)
    plt.title('검사자'+str(k)+'의 검사결과표')
    plt.axis("off")

    plt.savefig('./donggune/resultImg/검사자'+str(k)+'의 검사서.png',
            bbox_inches= None,
            dpi=300
            )