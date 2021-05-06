def desks(first_class, second_class, third_class):
    pupils = first_class + second_class + third_class
    pupils = pupils / 2
    pupils = int(pupils + (0.5 if pupils > 0 else -0.5))
    print(pupils)
desks(int(input()), int(input()),int(input()))
