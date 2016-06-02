def func(year, month, day, hour, minute, second):
    if 1900 < year < 2100 and 1 <= month <= 12 \
        and 1 <= day <= 31 and 0 <= hour < 24 \
        and 0 <= minute < 60 and 0 <= second < 60:
            return 1


month_names = ['January', 'February', 'March', 'April', 
               'May', 'June', 'July', 'August', 'Sep',
               'Oct', 'Nov', 'Dec']

print(func(2016, 11, 2, 12, 42, 22))

for month in month_names:
    print(month)


print('hello'
        'world')
