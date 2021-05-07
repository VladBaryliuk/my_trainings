def electric_clocks(minutes):
    hours = minutes // 60
    minutes -= hours * 60
    while hours > 23:
        hours -= 24
    if minutes > 59:
        minutes -= 59
        hours += 1
    print(hours, minutes)
electric_clocks(int(input()))
