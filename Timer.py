import os, time

sound_file = '/home/suman/Automation_Scripts/Alarm.ogg'

def get_next(hour, minute, second):
	total = hour * 3600 + minute * 60 + second
	total -= 1
	hour = total // 3600
	minute = (total - hour * 3600) // 60
	second = (total - hour * 3600 - minute * 60)
	return (hour, minute, second)

def start(hour, minute, second):
	while hour > 0 or minute > 0 or second > 0:
		formatted = str(hour).zfill(2) + ":" + str(minute).zfill(2) + ":" + str(second).zfill(2)
		print("Time Remaining:",formatted, flush = True)
		hour, minute, second = get_next(hour, minute, second)
		time.sleep(0.99)
		os.system("clear")

if __name__ == '__main__':
	hour, minute, second = map(int, input("Enter time in the format hh:mm:ss: ").split(':'))
	start(hour, minute, second)
	formatted = str(hour).zfill(2) + ":" + str(minute).zfill(2) + ":" + str(second).zfill(2)
	print("Timer for {} finished...".format(formatted))
	os.system('paplay ' + sound_file)
