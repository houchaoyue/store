import random

print("====================================")
print("|-------中国工商银行账户管理系统-------|")
print("|-------1、开户              -------|")
print("|-------2、存钱              -------|")
print("|-------3、取钱              -------|")
print("|-------4、转账              -------|")
print("|-------5、查询              -------|")
print("|-------6、退出              -------|")
print("====================================")
bank = {
    101: {
        "password": "123456",
        "money": 100,
        "address":"回龙观"
    },
    102: {
        "password": "123456",
        "money": 100,
    },
    103: {
        "password": "123456",
        "money": 100,
    }
}

bank_name = "中国工商银行起码路支行"  # 写死的银行地址
def bank_adduser(account, username, password, country, province, street, door):
    if len(bank) > 100:
        # 超出了银行上限
        return 3
    if account in bank:
        # 如果名字  在    bank  执行下面的代码
        return 2
    bank[account] = {
        # 键一个名字       ：值来自传入的参数:account
        "username": username,
        "password": password,
        "country": country,
        "province": province,
        "street": street,
        "door": door,
        "money": 0,
        "brnk_name": bank_name  # 直接调用全局参数
    }
    return 1


def useradd():
    username = input("请输入您的用户名")
    password = input("请输入您的密码")
    print("请输入您的详细信息")
    country = input("请输入您国家")
    province = input("请输入您省份")
    street = input("请输入您街道")
    door = input("请输入您的门牌号")
    account = random.randint(10000000, 99999999)  # 随机生成8位账号
    status = bank_adduser(account, username, password, country, province, street, door)
    if status == 3:
        print("对不起，改银行的用户已满，请到其他银行办理")
    if status == 2:
        print("对不起，改用户已经开户，不要重复")
    if status == 1:
        print("恭喜你正常开户，以下是您的信息")
        info = '''
          ------------个人信息------------
            用户名:%s
            账号：%s
            密码：*****
            国籍：%s
            省份：%s
            街道：%s
            门牌号：%s
            余额：%s
            开户行名称：%s
        '''
        print(info % (username, account, country, province, street, door, bank[account]["money"], bank_name))


# 存款
def bank_cunkuan(account, money):
    if account in bank:
        bank[account]['money'] = bank[account]['money'] + money
        return True
    else:
        return False


def deposit():
    account = int(input("请输入您的账号"))
    money = int(input('请输入你要存多少钱'))
    yanzheng = bank_cunkuan(account, money)
    if yanzheng is False:
        print('存款失败，用户名错误')
    elif yanzheng is True:
        print('存款成功')


# 取款
def bank_qukuan(account, password, money):
    if account in bank:
        if bank[account]["password"] == password:
            if money <= bank[account]['money']:
                bank[account]['money'] = bank[account]['money'] - money
                return 0  # 取钱成功
            else:
                return 3  # 钱不够
        else:
            return 2
    else:
        return 1


def quqian():
    account = int(input("请输入您的账号"))
    password = input('请输入您的密码')
    money = int(input('请输入你要取多少钱'))
    status = bank_qukuan(account, password, money)
    if status == 3:
        print('您的账户余额不足')
    if status == 2:
        print('您的密码不正确')
    if status == 1:
        print('您的账号错误')
    if status == 0:
        print('取款成功')

#转账
account = 101 #转出账号
account1 = 102 #转入账号
def bank_zhuanzhang(account,account1,password,money):
    if account in bank and account1 in bank :
        if bank[account]['password'] == password:
            if money <= bank[account]['money']:
                bank[account]['money'] = bank[account]['money'] - money
                bank[account1]['money'] = bank[account]['money'] + money
                return 0 #转账成功
            else:
                return 3 #钱不够
        else:
            return 2 #密码错误
    else:
        return 1 #账号错误

def zhuanqian():
    account = int(input('请输入转出账号'))
    account1 = int(input('请输入转入账号'))
    password = input('请输入转出账号密码')
    money = int(input('请输入转账金额'))
    status = bank_zhuanzhang(account,account1,password,money)
    if status == 3:
        print('您的账户余额不足')
    if status == 2:
        print('密码错误')
    if status == 1:
        print('账号错误')
    if status == 0:
        print('转账成功')

#查询账户
def bank_cxzh(account,password):
    if account in bank:
        if bank[account]['password'] == password:
            return 0
        else:
            return 1
    else:
        return 2
def chaxun():
    account = int(input('请输入您的账号'))
    password = input('请输入您的密码')
    status = bank_cxzh(account,password)
    if status == 2:
        print('账号错误')
    if status == 1:
        print('密码错误')
    if status == 0:
        print("查询成功，以下查询结果")
        info = '''
                      ------------个人信息------------
                        账号：%s
                        密码：*****
                        余额：%s
                        居住地址：%s
                        开户行名称：%s
        '''
        print(info % (account, bank[account]["money"], bank[account]["address"],bank_name))
while True:
    num = input("请输入您要办的业务：")
    if num == "1":
        useradd()
    elif num == "2":
        deposit()
    elif num == "3":
        quqian()
    elif num == "4":
        zhuanqian()
    elif num == "5":
        chaxun()
    elif num == "6":
        print("再见")
        break
    else:
        print("别瞎搞")
        break
