import datetime

now = datetime.datetime.now()
str_now = str(now)
str_now = str_now.split(' ')
str_now_date = str_now[0]
str_now_time = str_now[1].split(':')
str_now_time = str_now_time[0] + '-' + str_now_time[1] + '-' + str_now_time[2].split('.')[0]
str_now = str_now_date + '_' + str_now_time
print(str_now)

str_now_date_split = str_now_date.split('-')
year = str_now_date_split[0]
month = str_now_date_split[1]
print(year, month)