
n = int(input("Enter a number "))


for i in range(2, n):
    num = i
    flag = 1
    for j in range(2 , num-1):
        if num%j == 0:
            flag = 0
            break

    if flag == 1:
        print(num)    