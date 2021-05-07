def mkad(v,t):
    sum_variable = v * t
    if v > 0:
        if sum_variable > 109:
            print(sum_variable % 109)
        else:
            print(sum_variable)
    if v < 0:
        sum_variable = abs(sum_variable)
        if sum_variable < 109:
            print(109 - sum_variable)
        else:
            while sum_variable > 109:
                sum_variable = sum_variable - 109
            print(sum_variable)
v = int(input())
t = int(input())
mkad(v,t)
