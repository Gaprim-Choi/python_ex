import pandas as pd
import numpy as np
KTX_data = {'경부선 KTX': [39060, 39896, 42005, 43621, 41702, 41266, 32427],
 '호남선 KTX': [7313, 6967, 6873, 6626, 8675, 10622, 9228],
 '경전선 KTX': [3627, 4168, 4088, 4424, 4606, 4984, 5570],
 '전라선 KTX': [309, 1771, 1954, 2244, 3146, 3945, 5766],
 '동해선 KTX': [np.nan, np.nan, np.nan, np.nan, 2395, 3786, 6667]}
col_list = ['경부선 KTX', '호남선 KTX', '경전선 KTX', '전라선 KTX', '동해선 KTX']
index_list = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
df_KTX = pd.DataFrame(KTX_data, columns=col_list, index=index_list)
print(df_KTX)
'''
 경부선 KTX 호남선 KTX 경전선 KTX 전라선 KTX 동해선 KTX
2011 39060 7313 3627 309 NaN
2012 39896 6967 4168 1771 NaN
2013 42005 6873 4088 1954 NaN
2014 43621 6626 4424 2244 NaN
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
2015 41702 8675 4606 3146 2395.0
2016 41266 10622 4984 3945 3786.0
2017 32427 9228 5570 5766 6667.0
'''
print(df_KTX.index)
'''
Index(['2011', '2012', '2013', '2014', '2015', '2016', '2017'], dtype='object')
'''
print(df_KTX.columns)
'''
Index(['경부선 KTX', '호남선 KTX', '경전선 KTX', '전라선 KTX', '동해선 KTX'],
dtype='object')
'''
print(df_KTX.values)
'''
[[39060. 7313. 3627. 309. nan]
[39896. 6967. 4168. 1771. nan]
[42005. 6873. 4088. 1954. nan]
[43621. 6626. 4424. 2244. nan]
[41702. 8675. 4606. 3146. 2395.]
[41266. 10622. 4984. 3945. 3786.]
[32427. 9228. 5570. 5766. 6667.]]
'''
print(df_KTX.head())
'''
 경부선 KTX 호남선 KTX 경전선 KTX 전라선 KTX 동해선 KTX
2011 39060 7313 3627 309 NaN
2012 39896 6967 4168 1771 NaN
2013 42005 6873 4088 1954 NaN
2014 43621 6626 4424 2244 NaN
2015 41702 8675 4606 3146 2395.0
'''
print(df_KTX.tail())
'''
 경부선 KTX 호남선 KTX 경전선 KTX 전라선 KTX 동해선 KTX
2013 42005 6873 4088 1954 NaN
2014 43621 6626 4424 2244 NaN
2015 41702 8675 4606 3146 2395.0
2016 41266 10622 4984 3945 3786.0
2017 32427 9228 5570 5766 6667.0
'''
print(df_KTX.head(3))
'''
 경부선 KTX 호남선 KTX 경전선 KTX 전라선 KTX 동해선 KTX
2011 39060 7313 3627 309 NaN
2012 39896 6967 4168 1771 NaN
2013 42005 6873 4088 1954 NaN
'''
print(df_KTX.tail(2))
'''
 경부선 KTX 호남선 KTX 경전선 KTX 전라선 KTX 동해선 KTX
2016 41266 10622 4984 3945 3786.0
2017 32427 9228 5570 5766 6667.0
'''
print(df_KTX[1:2])
'''
 경부선 KTX 호남선 KTX 경전선 KTX 전라선 KTX 동해선 KTX
2012 39896 6967 4168 1771 NaN
'''
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
print(df_KTX[2:5])
'''
 경부선 KTX 호남선 KTX 경전선 KTX 전라선 KTX 동해선 KTX
2013 42005 6873 4088 1954 NaN
2014 43621 6626 4424 2244 NaN
2015 41702 8675 4606 3146 2395.0
'''
print(df_KTX.loc['2011'])
'''
경부선 KTX 39060.0
호남선 KTX 7313.0
경전선 KTX 3627.0
전라선 KTX 309.0
동해선 KTX NaN
Name: 2011, dtype: float64
'''
print(df_KTX.loc['2013':'2016'])
'''
 경부선 KTX 호남선 KTX 경전선 KTX 전라선 KTX 동해선 KTX
2013 42005 6873 4088 1954 NaN
2014 43621 6626 4424 2244 NaN
2015 41702 8675 4606 3146 2395.0
2016 41266 10622 4984 3945 3786.0
'''
print(df_KTX['경부선 KTX'])
'''
2011 39060
2012 39896
2013 42005
2014 43621
2015 41702
2016 41266
2017 32427
Name: 경부선 KTX, dtype: int64
'''
print(df_KTX['경부선 KTX']['2012':'2014'])
'''
2012 39896
2013 42005
2014 43621
Name: 경부선 KTX, dtype: int64
'''
print(df_KTX['경부선 KTX'][2:5])
'''
2013 42005
2014 43621
2015 41702
Name: 경부선 KTX, dtype: int64
'''
print(df_KTX.T)
'''
 2011 2012 2013 2014 2015 2016 2017
경부선 KTX 39060.0 39896.0 42005.0 43621.0 41702.0 41266.0 32427.0
호남선 KTX 7313.0 6967.0 6873.0 6626.0 8675.0 10622.0 9228.0
경전선 KTX 3627.0 4168.0 4088.0 4424.0 4606.0 4984.0 5570.0
전라선 KTX 309.0 1771.0 1954.0 2244.0 3146.0 3945.0 5766.0
동해선 KTX NaN NaN NaN NaN 2395.0 3786.0 6667.0
'''
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
print(df_KTX)
'''
 경부선 KTX 호남선 KTX 경전선 KTX 전라선 KTX 동해선 KTX
2011 39060 7313 3627 309 NaN
2012 39896 6967 4168 1771 NaN
2013 42005 6873 4088 1954 NaN
2014 43621 6626 4424 2244 NaN
2015 41702 8675 4606 3146 2395.0
2016 41266 10622 4984 3945 3786.0
2017 32427 9228 5570 5766 6667.0
'''
print(df_KTX[['동해선 KTX', '전라선 KTX', '경전선 KTX', '호남선 KTX', '경부선 KTX']])
'''
 동해선 KTX 전라선 KTX 경전선 KTX 호남선 KTX 경부선 KTX
2011 NaN 309 3627 7313 39060
2012 NaN 1771 4168 6967 39896
2013 NaN 1954 4088 6873 42005
2014 NaN 2244 4424 6626 43621
2015 2395.0 3146 4606 8675 41702
2016 3786.0 3945 4984 10622 41266
2017 6667.0 5766 5570 9228 32427
'''
