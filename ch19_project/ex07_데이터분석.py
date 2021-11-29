# 이미지 저장기능은 제가 보고 싶어서 추가 했습니다.
# 데이터 분석
from wordcloud import WordCloud
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

data_folder = './ch19_project/seoul_expense/'
years = [2017, 2018, 2019]

df_expense_all = pd.DataFrame()

for year in years:
    expense_list_year_dir = data_folder + str(year) + '/'
    expense_list_tidy_file = "{}_expense_list_tidy.csv".format(year)

    path_file_name = expense_list_year_dir + expense_list_tidy_file

    df_expense = pd.read_csv(path_file_name)
    df_expense_all = df_expense_all.append(df_expense, ignore_index=True)

# font 설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False


# 요일별 업무추진비 집행 횟수 분석
expense_date_time = pd.to_datetime(df_expense_all['집행일시'])

week_day_name = ["월", "화", "수", "목", "금", "토", "일"]

df_expense_all['집행일시_요일'] = [week_day_name[weekday]
                             for weekday in expense_date_time.dt.weekday]

expense_weekday = df_expense_all['집행일시_요일'].value_counts()
print(expense_weekday)

expense_weekday = expense_weekday.reindex(index=week_day_name)
print(expense_weekday)


expense_weekday.plot.bar(rot=0)
plt.title("요일별 업무추진비 집행 횟수")
plt.xlabel("요일")
plt.ylabel("집행 횟수")
image_file = './ch19_project/img/expense_weekday_total1.png'  # 이미지 파일 경로 및 이름
plt.savefig(image_file, dpi=400)  # 그래프를 이미지 파일로 저장
plt.show()


# 요일별 업무추진비 집행 금액 분석
expense_weekday_total = pd.pivot_table(df_expense_all, index=['집행일시_요일'],
                                    values=['집행금액'], aggfunc=sum)

print(expense_weekday_total)

eok_won = 100000000
expense_weekday_total = expense_weekday_total.reindex(index=week_day_name)

(expense_weekday_total/eok_won).plot.bar(rot=0)
plt.ylabel('집행금액(억원)')
plt.title("요일별 업무추진비 집행금액")
image_file = './ch19_project/img/expense_weekday_total2.png'  # 이미지 파일 경로 및 이름
plt.savefig(image_file, dpi=400)  # 그래프를 이미지 파일로 저장
plt.show()


# 시간때별 업무추진비 집행 횟수 분석
df_expense_all['집행일시_시간'] = [hour for hour in expense_date_time.dt.hour]

expense_hour_num = df_expense_all['집행일시_시간'].value_counts()
print(expense_hour_num)

work_hour = [(k+8) % 24 for k in range(24)]
expense_hour_num = expense_hour_num.reindex(index=work_hour)
print(expense_hour_num)

expense_hour_num.plot.bar(rot=0)
plt.title("시간별 업무추진비 집행 횟수")
plt.xlabel("집행 시간")
plt.ylabel("집행 횟수")
image_file = './ch19_project/img/expense_hour_num1.png'  # 이미지 파일 경로 및 이름
plt.savefig(image_file, dpi=400)  # 그래프를 이미지 파일로 저장
plt.show()

# 시간때별 업무추진비 집행 금액 분석
expense_hour_total = pd.pivot_table(df_expense_all, index=['집행일시_시간'],
                                    values=['집행금액'], aggfunc=sum)

eok_won = 100000000
expense_hour_total = expense_hour_total.reindex(index=work_hour)

(expense_hour_total/eok_won).plot.bar(rot=0)
plt.ylabel('집행금액(억원)')
plt.title("시간별대 업무추진비 집행금액")
image_file = './ch19_project/img/expense_hour_num2.png'  # 이미지 파일 경로 및 이름
plt.savefig(image_file, dpi=400)  # 그래프를 이미지 파일로 저장
plt.show()