#-*-coding:utf-8-*-
import time, sys, danmu

reload(sys)
sys.setdefaultencoding( "utf-8" )

def pp(msg):
    print(msg.encode(sys.stdin.encoding, 'ignore').decode(sys.stdin.encoding))
dmc = danmu.DanMuClient('https://www.douyu.com/71017')  #123455  4897321
if not dmc.isValid(): print('Url not valid')
@dmc.danmu
def danmu_fn(msg):
    pp('[%s] %s' % (msg['NickName'], msg['Content']))
    file = open("3.txt", "a+")
    line = 'insert into danmu (name,txt) values (\''+msg['NickName']+'\',\''+msg['Content']+'\'); ' +" \n"
    file.write(line)
    file.close()
@dmc.gift
def gift_fn(msg):
    pp('[%s] sent a gift!' % msg['NickName'])
@dmc.other
def other_fn(msg):
    pp('Other message received')
dmc.start(blockThread = True)

