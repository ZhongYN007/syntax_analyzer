import scaner as cs
import bianliang as p
syn = -1
kk = 0


def Irparser():

    global syn, kk
    syn = cs.scanner().typenum
    if syn == 1:
        syn = cs.scanner().typenum
        yucu()
        if syn == 2:
            syn = cs.scanner().typenum
            if syn == 0 and kk == 0:
                print("success")
        else:
            if  kk != 1:
                print("缺end错误")
    else:
        print("缺Begin错误")
        kk = 1


def yucu():  # 判断一个语句的最后是否有;号
    global syn, kk
    statement()
    while syn == 34: # ;
        syn = cs.scanner().typenum
        statement()
    return


def statement():
    global syn, kk
    if syn == 10:
        syn = cs.scanner().typenum
        if syn == 18:  # :=号
            syn = cs.scanner().typenum
            expression()
        else:
            print("赋值符号错误")
            kk = 1
    else:
        print("语句错误")
        kk = 1


def expression():
    global syn, kk
    term()
    while syn == 22 or syn == 23:  # +，-
        syn = cs.scanner().typenum
        term()
    return


def term():
    global syn
    factor()
    while syn == 24 or syn == 25:
        syn = cs.scanner().typenum
        factor()
    return


def factor():
    global syn, kk
    if syn == 10 or syn == 20:  # 标识符，数字
        syn = cs.scanner().typenum
    elif syn == 26:  # （
        syn = cs.scanner().typenum
        expression()
        if syn == 27:  # ）
            syn = cs.scanner().typenum
        else:
            print("输出')'错误")
            kk = 1
    else:
        print("输出表达式错误")
        kk = 1
    return


if __name__ == "__main__":
    f = open("text.txt", "r")
    p.str_input = str(f.read())
    print(p.str_input)
    Irparser()
    f.close()
