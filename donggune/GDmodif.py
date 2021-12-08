from numpy.core.numeric import NaN
import pandas as pd
import numpy as np
 
from matplotlib.path import Path
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D


""" --------------------Excel Data 입력---------------------- """
df = pd.read_excel('./donggune/testV0.xlsx', sheet_name='최종(적합성)')
jd = pd.read_excel('./donggune/2. 직업코드표.xlsx', sheet_name='진로코드분류표 (3)')
ja = pd.read_excel('./donggune/3. 코드 유형별 특징.xlsx', sheet_name=0)
print(df)
print(jd)
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
total = pd.DataFrame(pd.concat([df_S_sum,df_A_sum,df_R_sum,df_I_sum,df_C_sum,df_E_sum],axis=1))
print(total)
total = total.drop([0])

j=0
for i in total.iterrows():
    j= j+1

    total_new = total.transpose()
    test = total_new.sort_values(by=j, ascending=False).head(4)
    print(test[j])
    print(test.index[1])
    
    ori_type = df[j][1]
    
    if test[j][1] == test[j][2] == test[j][3]:
        print('재검사가 필요한 검사자 입니다.')
    elif test[j][0] == test[j][1]:
        type_sum1 = test.index[0] + test.index[1]
        type_sum2 = test.index[1] + test.index[0]
    elif test[j][1] == test[j][2]:
        type_sum1 = test.index[0] + test.index[1]
        type_sum2 = test.index[1] + test.index[2]
    else:
        type_sum1 = test.index[0] + test.index[1]
        type_sum2 = NaN

    if type_sum2 != NaN:
        print('당신은'+ type_sum1 +'타입이 적성입니다.')
    else:
        print('당신은 "'+ type_sum1 + "," + type_sum2+'" 타입이 적성입니다.')

    listI = [type_sum1 , type_sum2]

    for i in range(len(type_sum1)):
        typeStr = listI[i]
        if ori_type[0] == typeStr[0]:
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
        print(listI[i] + "과의 일치율 "+ str1 +"입니다.")

"""     print(jd[(jd['코드'] == type_sum1)])
    print(jd[(jd['코드'] == type_sum2)]) """