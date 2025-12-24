n = int(input('Введите натуральное число n: '))

three = 0
last = 0
even = 0
sum_5 = 0
pr_7 = 1
zero_five = 0

last_num = n % 10

while n > 0:
    num = n % 10

    if num == 3:
        three +=1

    if num == last_num:
        last += 1

    if num % 2 == 0:
        even +=1

    if num > 5:
        sum_5 += num

    if num > 7:
        pr_7 *= num

    if num == 0 or num == 5:
        zero_five +=1

    n = n // 10

print(three)
print(last)
print(even)
print(sum_5)
print(pr_7)
print(zero_five)
