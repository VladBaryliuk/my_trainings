def leap_year(year_number):
    if year_number % 4 == 0 and year_number % 100 != 0 or year_number % 400 == 0:
        print("YES")
    else:
        print("NO")


leap_year(int(input()))
