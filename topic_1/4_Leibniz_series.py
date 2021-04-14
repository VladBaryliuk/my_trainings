p = 0
count = 1
j = 0
def learning_p_number():
    global p, count, j
    while j < 10:
        temp=4/count
        count+=2
        if j % 2 != 0:
            p -= temp
        else:
            p+=temp
        j+=1

learning_p_number()    
print(p)

p = 0
count = 1
def learning_p_number():
    global p, count
    for i in range (1, 11, 1):
        temp=4/count
        if i % 2 != 0:
            p += temp
        else:
            p-=temp
        count+=2
learning_p_number()    
print(p)

