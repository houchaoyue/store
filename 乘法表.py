a=int(input('请输入一个数:'))
for i in range(1, a+1):
    for j in range(1, i + 1):
        print(j, '*', i, '=', i * j, end="  ")
    print()
