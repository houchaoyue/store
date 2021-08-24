from threading import Thread
import time
breads = 0

class Cook(Thread):
    username = ''
    bread = 0

    def run(self) -> None:
        global breads
        while True:
            if breads ==500:
                time.sleep(0.2)
            elif breads < 500:
                time.sleep(0.2)
                self.bread +=1
                breads +=1
                print("厨师{}已做了{}个面包".format(self.username, self.bread))
                print("销售柜台总共有{}个面包".format(breads))

class Customer(Thread):
    username = ''
    wallet = 3000
    count = 0#面包的计数器

    def run(self) -> None:
        global breads
        while True:
            if int(self.wallet) > 0:
                if breads >= 500:
                    breads = breads -1
                    self.wallet = self.wallet -3
                    self.count = self.count +1
                    print("顾客{}已买了{}个面包,还剩{}元".format(self.username, self.count,self.wallet))
                elif breads == 0:
                    time.sleep(0.2)
            elif int(self.wallet) == 0:
                print("顾客{}已消费完".format(self.username))
                break

cook1 = Cook()
cook2 = Cook()
cook3 = Cook()
cook1.username = "张三"
cook2.username = "李四"
cook3.username = "王五"
shopper1 = Customer()
shopper2 = Customer()
shopper3 = Customer()
shopper4 = Customer()
shopper5 = Customer()
shopper6 = Customer()
shopper1.username = "1"
shopper2.username = "2"
shopper3.username = "3"
shopper4.username = "4"
shopper5.username = "5"
shopper6.username = "6"
cook1.start()
cook2.start()
cook3.start()
shopper1.start()
shopper2.start()
shopper3.start()
shopper4.start()
shopper5.start()
shopper6.start()










