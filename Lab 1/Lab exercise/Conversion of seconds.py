'''
10. Write a program to convert seconds to day, hour, minutes and seconds.
'''
second=int(input("Enter the value for seconds:"))
day=(((second//60)//60)//24)
print(f"Total day for given seconds: {day}")
hour=((second//60)//60)
print(f"The hour for given seconds: {hour}")
minute=(second//60)
print(f"The minute for given seconds is: {minute}")
remaining_second=(second%60)
print(f"The remaining second:{remaining_second}")