#-*-coding:utf-8-*-


def save():
    file = open("2.txt", "w")
    line = "1但是的斯科拉的金凯撒大家看啥接口了撒开机1\n"
    file.write(line)
    file.close()

if __name__ == "__main__": 
    save()