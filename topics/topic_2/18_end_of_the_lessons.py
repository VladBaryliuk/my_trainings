def end_of_the_lessons(number_of_lesson):
    hours = 9
    minutes = 0
    for i in range(1,number_of_lesson+1):
        minutes += 45
        if i < number_of_lesson:
            if i % 2 == 0:
                minutes += 15
            else:
                minutes += 5
        if minutes >= 60:
            hours += 1
            minutes -= 60
    print(hours, minutes)
end_of_the_lessons(int(input()))