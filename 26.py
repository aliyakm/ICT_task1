from datetime import date
from datetime import datetime

date1 = date.today()
print("Date: ", date1)

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time:", current_time)