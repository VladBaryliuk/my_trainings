def electric_clocks(seconds):
    hours = seconds // 3600
    seconds -= hours * 3600
    minutes = seconds // 60
    seconds -= minutes * 60
    print(hours, minutes, seconds, sep=":")


electric_clocks(int(input()))
