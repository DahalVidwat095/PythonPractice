'''Yoy live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each of the 10 stops on
the way. How long will the bus journey take? Alternatively, you could run to university. You jog the first
mile at 7mph; then run the next two at 15mph; before jogging the last at 7mph again. Will this be quicker or
 slower than the bus?'''
Distance_from_university=4
Speed_of_bus=25
Total_stop_time=20
Time_taken_by_bus=((Distance_from_university/Speed_of_bus)*60)
total_time=Time_taken_by_bus+Total_stop_time
print(f"The total time for bus journey is {total_time} minutes.")


jog_one=(1/7)*60
jog_two=(2/15)*60
jog_three=(1/7)*60
total_walk_time=jog_one+jog_two+jog_three
print(f"The time taken by running is {total_walk_time} minutes.")
if (total_time>total_walk_time):
    print("Taking bus is slower than walking.")
else :
    print("Taking bus is faster than walking.")