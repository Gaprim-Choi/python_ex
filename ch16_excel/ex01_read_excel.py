import pandas as pd
df = pd.read_excel('./ch16_excel/학생시험성적.xlsx')
print(df)

df = pd.read_excel('./ch16_excel/학생시험성적.xlsx', sheet_name=1)
print(df)

df = pd.read_excel('./ch16_excel/학생시험성적.xlsx', sheet_name='2차시험')
print(df)

df = pd.read_excel('./ch16_excel/학생시험성적.xlsx', sheet_name='2차시험', index_col=0)
print(df)
df = pd.read_excel('./ch16_excel/학생시험성적.xlsx',sheet_name='2차시험', index_col='학생')
print(df)