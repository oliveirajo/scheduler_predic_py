from TimeRange import TimeRange
from Friend import Friend
from custom_list import CustomList
import helpers_123 as h 

""" a day have 1439 min -> (60 min x 24 hours) - 1 """
def main():
    #maintain a list of available minutes on the day
    available_minutes = CustomList(range(1440))
    
    f1 = Friend("Jonhy")
    f1.add_busy_ranges(TimeRange(start_time="08:00", end_time="10:00")) # not available from 8am until 10 am
    
    f2 = Friend("Zezocas")
    f2.add_busy_ranges(TimeRange(start_time="08:00", end_time="14:00")) # 720 until 840 he is not available
    f2.add_busy_ranges(TimeRange(start_time="18:00", end_time="23:30"))
    
    f3 =  Friend("Sara")
    f3.add_busy_ranges(TimeRange(start_time="17:00", end_time="23:00"))
    
    for m in available_minutes[:]: # the [:] allows us to work on a copy of the original list.
        for r in Friend.all_busy_minutes_range:
            if m in r:
                available_minutes.remove_if_exist(m)
    
    for tr in h.prettify_available_minutes(available_minutes):
        print(f"You can meet in {tr}")

if __name__ == "__main__":
    main()