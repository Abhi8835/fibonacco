num = int(input("enter the number : "))
first_num = 0
second_num = 1
result = 0
while (result <= num):
    print(result)
    first_num = second_num
    second_num = result
    result = first_num + second_num
