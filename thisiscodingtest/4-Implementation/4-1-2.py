n = int(input())

count = 0

hour_flag = False
min_flag = False
sec_flag = False

# for hour in range(0, n + 1):
#     if(str(hour).find('3') >= 0):
#         hour_flag = True
#     else:
#         hour_flag = False
#     for minute in range(0, 60):
#         if(str(minute).find('3') >= 0):
#             min_flag = True
#         else:
#             min_flag = False
#         for second in range(0, 60):
#             if(str(second).find('3') >= 0):
#                 sec_flag = True
#             else:
#                 sec_flag = False
#             if(hour_flag or min_flag or sec_flag):
#                 count += 1

for hour in range(n + 1):
    for minute in range(60):
        for second in range(60):
            if '3' in str(hour) + str(minute) + str(second):
                count += 1

print(count)
