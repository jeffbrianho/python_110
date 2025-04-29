# # Some people believe that Fridays that fall on the 13th day of the month are unlucky days.
# #  Write a function that takes a year as an argument and returns the number of Friday the 13ths 
# # in that year. You may assume that the year is greater than 1752, which is when the United Kingdom 
# # adopted the modern Gregorian Calendar. You may also assume that the same calendar will remain in
# #  use for the foreseeable future.

# """
# I: year
# O: integer representing the number of FRI13 in that year

# JFMAMJJASOND
# 31 28 31 30 31 30 31 31 30 31 30 31

# """
# import datetime

# def has_13th(year, month):
#     date_13th = datetime.date(year, month, 13)
#     return date_13th.weekday() == 4

# def friday_the_13ths(year):
#     amount_of_days = 0
#     for month in range(1, 13):
#         if has_13th(year, month):
#             amount_of_days += 1
#     return amount_of_days


# print(friday_the_13ths(1986) == 1)      # True
# print(friday_the_13ths(2015) == 3)      # True
# print(friday_the_13ths(2017) == 2)      # True

# # Their answer
# import datetime

# def friday_the_13ths(year):
#     thirteenths = [datetime.date(year, month, 13)
#                    for month in range(1, 13)]

#     count = 0
#     for day in thirteenths:
#         if day.weekday() == 4:
#             count += 1

#     return count
import datetime
print(datetime.date(2025, 6, 13).weekday())
