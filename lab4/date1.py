import datetime
#ex1
# date = datetime.datetime.today() - datetime.timedelta(days=5)
# print(date)

#ex2
# print(datetime.datetime.today() - datetime.timedelta(days=1))
# print(datetime.datetime.today())
# print(datetime.datetime.today() + datetime.timedelta(days=1))

#ex3
# cur_datetime = datetime.datetime.now()
# without = cur_datetime.replace(microsecond=0)
# print("current datetime:",  cur_datetime)
# print("without microseconds:",  without)

#ex4
# date1 = datetime.datetime(2024, 2, 15, 12, 44, 15)  
# date2 = datetime.datetime(2024, 2, 22, 13, 55, 12)
# dif = date2 - date1
# print(dif.total_seconds())