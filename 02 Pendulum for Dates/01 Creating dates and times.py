from datetime import datetime
import time
import pendulum

# TODO: create a new datetime using pendulum
dt1 = pendulum.datetime(2020, 7, 28)
print(dt1)

print(isinstance(dt1, datetime))

print(dt1.timezone.name)

print("...\n")
# TODO: convert the time to another time zone

dt2 = dt1.in_timezone("Europe/Paris")
print(dt2)
print("...\n")


# TODO: create a new datetime using the now() function
#Europe/London
dt3 = pendulum.now("Asia/Kolkata")
print(dt3)
print(dt3.timezone.name)
print("...\n")

# TODO: Use the local function:

here = pendulum.local(2020, 7, 28)
print(here)
print(here.timezone.name)
print("...\n")

# TODO: Use today, tomorrow, yesterday

today = pendulum.today()
tom = pendulum.tomorrow()
yest = pendulum.yesterday("Asia/Kolkata")
print(today)
print(tom)
print(yest)
print("...\n")

# TODO: create a datetime from a system timestamp
t = time.time()
print(t)
dt4 = pendulum.from_timestamp(t)
print(dt4)
