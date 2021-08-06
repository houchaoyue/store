dict1={"13号线":{"回龙观":{"朱辛庄":{'110':{'恭喜你回家了'}}}}}
name=input("你要乘几号线")
if  name=="13号线":
    print(dict1["13号线"])
    name1 = input("你要到哪站")
    if name1 =="回龙观":
        print(dict1["13号线"]["回龙观"])
        name2 = input('你的小区叫什么')
        if name2 == '朱辛庄':
            print(dict1['13号线']['回龙观']['朱辛庄'])
            name3 = input("你的门牌号是")
            if name3 == '110':
                print(dict1['13号线']['回龙观']['朱辛庄']['110'])
            else:
                print('你记错了')
        else:
            print('你迷路了')
    else:
        print('你回不去了')
else:
    print('再见')

