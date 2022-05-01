import helpers_123 as h

from TimeRange import TimeRange
from dataclasses import dataclass, field
from typing import ClassVar

@dataclass
class Friend:
    all_busy_minutes_range : ClassVar[list] = []
    name : str
    busy_time_ranges :  list[TimeRange] = field(default_factory=list, repr=False)
    
    def add_busy_ranges(self, obj:TimeRange):
        self.busy_time_ranges.append(obj)
        # add the minutes range objet to a classs atrribute:
        Friend.all_busy_minutes_range.append(obj.minutes_range)
        
"""f1 = Friend("d")
f1.add_busy_ranges(TimeRange(start_time="08:00", end_time="10:00")) # not available from 8am until 10 am
f1.add_busy_ranges(TimeRange(start_time="11:00", end_time="15:00")) # not available from 8am until 10 am        
print(Friend.all_busy_minutes_range) # 
"""
        
    
"""
f1 = Friend("Joel")
f1.add_busy_ranges(TimeRange(start_time="09:00", end_time="17:00"))
f1.add_busy_ranges(TimeRange(start_time="18:00", end_time="23:00"))
print(f1.busy_time_ranges)

print(f1)"""