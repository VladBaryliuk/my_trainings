def sharing_numbers(a, b):
    help_variable = a
    a = b
    b = help_variable
    print(a, b)

sharing_numbers(int(input()), int(input()))
