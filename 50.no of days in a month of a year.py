#no of days in a month of a year
year=int(input('Enter the year:'))
month=int(input('Enter the month of the year:'))
days=[31,28,31,30,31,30,31,31,30,31,30,31]
if month==2 and ((year%4==0 and year%100!=0)or year%400==0):
    print('29 days')
else:
    print(days[month-1],'days')
    