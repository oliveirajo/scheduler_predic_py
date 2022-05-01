def timerange_to_minutes(t_str):
    """
    Return amount of minutes for time ranges in format HH:MM
    :param t_str:
    :return:
    """
    #05:00
    hour = int(t_str.split(":")[0])
    minutes = int(t_str.split(":")[1])
    hour_to_minutes = hour * 60 
    
    return hour_to_minutes + minutes
    
def minutes_to_timerange_str(m):
    """
    Return a timerange string in format of H:MM fo the given integer
    :param m:
    :return:
    """
    hour = m // 60
    hour_str = f"{hour:02d}"
    minutes = m % 60
    minutes_str = f"{minutes:02d}"
    
    return f"{hour_str}:{minutes_str}"
    
def prettify_available_minutes(l: list):
    grouped_list = [] # a nested list
    list_resettable = []
    
    # Group the list so that [[0, 1, 2],[60, 61, 62]]
    for element in l:
        if list_resettable == []:
            list_resettable.append(element)
            continue
        if list_resettable[-1] + 1 == element:
            list_resettable.append(element)
        else:
            grouped_list.append(list_resettable[:])
            list_resettable.clear()
            list_resettable.append(element)
            
    grouped_list.append(list_resettable)
    
    
    time_range = []
    for group in grouped_list:
        start_time = minutes_to_timerange_str(m=group[0])
        end_time = minutes_to_timerange_str(m=group[-1])
        time_range_str = f"{start_time} - {end_time}"
        time_range.append(time_range_str)
        
    return time_range



print(minutes_to_timerange_str(1439))