#As a developer, I want to use Python’s proper snake_case for variable names.

#As a developer, I want to create a AlarmClock class.

#As a developer, I want the AlarmClock class to have class variables to keep track of the AlarmClock’s current time, whether the alarm is on or off, and the time the alarm is set
#to. (You can use arbitrary strings to represent the time, it does not need to accurately tell the current time or change over time).

#As a developer, I want the AlarmClock class to have a method to set (or change) the current time and print to the console the current time.

#As a developer, I want the AlarmClock class to have a method to toggle the alarm on or off.

#As a developer, I want the AlarmClock class to have a method to set the current alarm time and print to the console the current alarm time.

#As a developer, I want to import the AlarmClock class into main.py so I can instantiate it as a new AlarmClock object and call methods on it.

#1. Print the clock’s time to the terminal

#2. Call the alarm clock’s change time method to change the time

#3. Toggle the alarm clock’s on off switch

class AlarmClock:

    def __init__(self, current_time, alarm_status, alarm_time):
        self.current_time = current_time
        self.alarm_status = alarm_status
        self.alarm_time = alarm_time

    def set_time(self):
        self.current_time = input("Please input the current time (Ex 12:00). ")

    def toggle_alarm(self):
        if self.alarm_status == True:
            self.alarm_status = False
        else:
            self.alarm_status = True

    def set_alarm(self, current_time):
        self.alarm_time = input("Please input the time of your alarm (Ex 12:00). ")
        self.alarm_status = True    #This will allow the user to set an alarm without toggling first
        print(f"It is currently {self.current_time}, this alarm will go off at {self.alarm_time} ")
        