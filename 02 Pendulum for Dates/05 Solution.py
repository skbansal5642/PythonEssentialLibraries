from datetime import datetime
import time
import pendulum

# getting today's date and time
now = pendulum.now("Asia/Kolkata")

# can use this way also for date only
# today = pendulum.today()

print("Today is: {0}".format(now.format("dddd, MMMM DD")))

# fixed date for International Clash Day
icd = pendulum.datetime(now.year, 2, 7)
print("International Clash Day is: {0}".format(icd.format("dddd, MMMM DD")))

# compare which date is bigger
if now > icd:
	# find the difference b/w both dates
	old_days = now - icd
	print("International Clash Day went by {0} days ago".format(old_days.days))
	
	# getting the date for ICD of next year
	icd = icd.add(years=1)


# calculate the difference b/w today and next ICD date.
coming_days = icd - now
print("It's {0} days until International Clash Day".format(coming_days.days))
