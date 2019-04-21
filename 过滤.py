import datetime

 

time = str(datetime.datetime.now())[:-7]

 

dirty = ['fuck','狗日的','犊子','麻批','仙人板板','R你妈','操你','草你']

 

class Player(object):

 

    def __init__(self,name):

        self.name = name

 

    def talk(self):

        self.string = raw_input("input-write:")

        # self.string = '你个狗日的，R你妈哟，操你个仙人板板，个老麻批'

        self.log()

        for i in dirty:

            self.string = self.string.replace(i,'雅蠛蝶')

        print "{}  {}-speak:{}".format(time,self.name,self.string,)

 

    def log(self):

        with open('zanghua.txt','a') as f:

            f.write("{}  {}-speak:{}n".format(time,self.name,self.string))

 



t1 = Player('white')

t2 = Player('black')

t3 = Player('green')

while True:

    n = raw_input('change Player:')

    if n == '1':

        t1.talk()

    elif n == '2':

        t2.talk()

    elif n == '3':

        t3.talk()

    elif n == 'q':

        print 'Bye'

        break

    else:

        print "尼玛在逗我?"