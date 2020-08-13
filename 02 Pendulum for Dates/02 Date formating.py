from datetime import datetime
import time
import pendulum

# create a datetime and print it.
dt1 = pendulum.datetime(2020, 7, 28, 15, 30)
print(dt1)

# TODO: use some formatting functions
print(dt1.to_date_string())
print(dt1.to_time_string())
print(dt1.to_datetime_string())

print("...")
# TODO: use functions for nice formatting
print(dt1.to_formatted_date_string())
print(dt1.to_day_datetime_string())


print("...")
# TODO: use some common formats
print(dt1.to_cookie_string())
print(dt1.to_iso8601_string())
print(dt1.to_rfc822_string())


print("...")
# TODO: use the format function for pretty printing
print(dt1.format("YYYY MM-DD HH:MM A"))
print(dt1.format("dddd DD MMMM YYYY"))

print("...")
# TODO: use localization
print(dt1.format("dddd DD MMMM YYYY", locale="de"))
print(dt1.format("dddd DD MMMM YYYY", locale="fr"))
