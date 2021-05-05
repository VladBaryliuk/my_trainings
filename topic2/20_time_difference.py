def time_difference(was_hours, was_minutes, was_seconds, now_hours, now_minutes, now_seconds):
    now_hours -= was_hours
    now_minutes -= was_minutes
    now_seconds -= was_seconds
    seconds_passed = 0
    now_minutes = now_minutes * 60
    now_hours = now_hours * 3600
    seconds_passed += now_seconds
    seconds_passed += now_minutes
    seconds_passed += now_hours
    print(seconds_passed)

time_difference(int(input()), int(input()), int(input()), int(input()), int(input()), int(input()))