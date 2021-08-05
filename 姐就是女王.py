import random
print('-------------开始游戏-------------')
list1=['普通','稀有','传奇']
name=list1[random.randint(0,len(list1)-1)]
print(name)
num=10
if name == "普通" :
    while True:
        i=0  #从0开始
        list2 =[]
        while i<3: #判断 i是否小于三 i小于三运行下面的代码
            i = i+1 #每次循环都加1
            a=random.randint(5,20)
            list2.append(a)
        #while = 初始值 while判断这个初始值是否大于一个值
        print(list2)
        num1 = list2[random.randint(0, len(list2) - 1)] #这是两边随机取出来的数字num1
        print(num1)
        list3=[1,2] #1 ==加号  2 等于减号
        name2 = list3[random.randint(0, len(list3) - 1)]  #随机的加减
        if name2 ==1 : #随机的加减如果等于1 进行加法运算
            num = num1 + num
            print(num)  #初始num 加上一个随机取出来的数字
        elif name2 ==2 : #随机的加减如果等于1 进行减法运算
            num = num1 - num
            print(num)  #初始num 加上一个随机取出来的数字
        if num > 100 :
            print("任务成功你的分数为",num)
            break
        elif num <= 0:
            print("任务失败你的分数为",num)
            break
if name == "稀有" :
    num =30
    while True:
        print("稀有为",num)
        i = 0  # 从0开始
        list2 = []
        while i < 3:  # 判断 i是否小于三 i小于三运行下面的代码
            i = i + 1  # 每次循环都加1
            a = random.randint(5, 20)
            list2.append(a)
        # while = 初始值 while判断这个初始值是否大于一个值
        print(list2)
        num1 = list2[random.randint(0, len(list2) - 1)]  # 这是两边随机取出来的数字num1
        print(num1)
        list3 = [1, 2]  # 1 ==加号  2 等于减号
        name2 = list3[random.randint(0, len(list3) - 1)]  # 随机的加减
        if name2 == 1:  # 随机的加减如果等于1 进行加法运算
            num = num1 + num
            print(num)  # 初始num 加上一个随机取出来的数字
        elif name2 == 2:  # 随机的加减如果等于1 进行减法运算
            num = num1 - num
            print(num)  # 初始num 加上一个随机取出来的数字
        if num > 100:
            print("任务成功你的分数为", num)
            break
        elif num <= 0:
            print("任务失败你的分数为", num)
            break
if name == "传奇" :
    while True:
        print("此时的分数为",num)
        i = 0  # 从0开始
        list2 = []
        while i < 3:  # 判断 i是否小于三 i小于三运行下面的代码
            i = i + 1  # 每次循环都加1
            a = random.randint(5, 20)
            list2.append(a)
        # while = 初始值 while判断这个初始值是否大于一个值
        print(list2)
        num1 = list2[random.randint(0, len(list2) - 1)]  # 这是两边随机取出来的数字num1
        print(num1)
        list3 = [1]  # 1 ==加号  2 等于减号
        name2 = list3[random.randint(0, len(list3) - 1)]  # 随机的加减
        if name2 == 1:  # 随机的加减如果等于1 进行加法运算
            num = num1 + num
            print(num)  # 初始num 加上一个随机取出来的数字
        if num > 100:
            print("任务成功你的分数为", num)
            break





