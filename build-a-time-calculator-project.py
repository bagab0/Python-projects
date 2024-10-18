def add_time(start, duration, starting_day=None):
    # Define days of the week
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Split and parse the start time
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(":"))

    # Convert start hour to 24-hour format for easier calculations
    if period == "PM" and start_hour != 12:
        start_hour += 12
    elif period == "AM" and start_hour == 12:
        start_hour = 0

    # Parse the duration time
    duration_hour, duration_minute = map(int, duration.split(":"))

    # Add duration to start time
    total_minutes = start_minute + duration_minute
    additional_hours = total_minutes // 60
    final_minutes = total_minutes % 60

    total_hours = start_hour + duration_hour + additional_hours
    final_hour = total_hours % 24
    days_later = total_hours // 24

    # Convert back to 12-hour format
    if final_hour == 0:
        final_hour = 12
        final_period = "AM"
    elif final_hour < 12:
        final_period = "AM"
    elif final_hour == 12:
        final_period = "PM"
    else:
        final_hour -= 12
        final_period = "PM"

    # Handle the day of the week if provided
    if starting_day:
        starting_day = starting_day.capitalize()
        start_day_index = days_of_week.index(starting_day)
        end_day_index = (start_day_index + days_later) % 7
        end_day = days_of_week[end_day_index]
        day_output = f", {end_day}"
    else:
        day_output = ""

    # Handle the "(next day)" or "(n days later)" output
    if days_later == 1:
        day_output += " (next day)"
    elif days_later > 1:
        day_output += f" ({days_later} days later)"

    # Return the final result in the proper format
    return f"{final_hour}:{final_minutes:02d} {final_period}{day_output}"

# Usage examples:

# Test cases:
print(add_time("3:00 PM", "3:10"))  # Returns: 6:10 PM
print(add_time("11:30 AM", "2:32", "Monday"))  # Returns: 2:02 PM, Monday
print(add_time("11:43 AM", "00:20"))  # Returns: 12:03 PM
print(add_time("10:10 PM", "3:30"))  # Returns: 1:40 AM (next day)
print(add_time("11:43 PM", "24:20", "tueSday"))  # Returns: 12:03 AM, Thursday (2 days later)
print(add_time("6:30 PM", "205:12"))  # Returns: 7:42 AM (9 days later)
