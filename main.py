from alarm_clock import AlarmClock

alarm = AlarmClock('11:51', False, '')


#Print the current_time of the original instantiation of the AlarmClock Class 
#Then change the time and reprint
print(alarm.current_time)   #Print the Current Time
alarm.set_time()            #Change the current Time
print(alarm.current_time)

#Toggle Alarm Clock
alarm.toggle_alarm()


#alarm.set_alarm(alarm.current_time)

