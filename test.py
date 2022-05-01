import src.data.helpers_123 as h
from src.data.TimeRange import TimeRange
from src.data.Friend import Friend

f1 = Friend("Jonhy")
f1.add_busy_ranges(TimeRange(start_time="08:00", end_time="10:00")) # not available from 8am until 10 am

print(h.timerange_to_minutes("15:13"))
print(f1)