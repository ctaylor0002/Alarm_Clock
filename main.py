from alarm_clock import AlarmClock

alarm = AlarmClock('11:51', False, '')


#Print the current_time of the original instantiation of the AlarmClock Class 
#Then change the time and reprint
print(alarm.current_time)
alarm.set_time()
print(alarm.current_time)

#Toggle Alarm Clock
chk = False
if alarm.alarm_status == True:
    while chk == False:
        question = input("Would you like to turn off the alarm? y/n ")
        if question == 'y':
            alarm.toggle_alarm()
            chk = True
        elif question == 'n':
            print(f"Alarm is still set for {alarm.alarm_time}")
            chk = True
        else:
            print("Invalid input. Try again")

#Set alarm time

alarm.set_alarm(alarm.current_time)

