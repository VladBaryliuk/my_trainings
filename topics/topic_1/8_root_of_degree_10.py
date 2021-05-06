sum_variable = 179 ** 10

def root_of_degree(sum_variable):
    number = ""
    sum_variable = str(sum_variable)
    for i in range(4):
        number += sum_variable
    return int(number)

print(pow(root_of_degree(sum_variable), 0.1))

