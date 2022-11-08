import bianliang as p


class WORD(object):
    def __init__(self, typenum, word):
        self.typenum = typenum
        self.word = word

# 获取字符到缓冲区中
def getchar():
    # print("input:%d" % p_input)
    p.ch = p.str_input[p.p_input]
    p.p_input += 1
    return p.ch


# 去掉空格
def delete_blank():
    while p.ch == " " or p.ch == 10:
        p.ch = p.str_input[p.p_input]
        p.p_input += 1


# 将字符拼接为字符串
def concat(str1):
    str1 += p.ch
    return str1


# 判断是否为字母
def letter():
    if ('a' <= p.ch <= 'z') or ('A' <= p.ch <= 'Z'):
        return True
    else:
        return False


# 判断是否为数字
def digit():
    if '0' <= p.ch <= '9':
        return True
    else:
        return False


# 判断是否为关键字
def reserve(str1):
    for find_str in p.rwtab:
        if str1 == find_str:
            return p.rwtab.index(find_str) + 1

    return 10


# 回退一位
def retract():
    p.p_input -= 1


def dtb(token):
    return bin(int(token))


def scanner():
    token = ""
    myword = WORD(10, "")
    getchar()
    delete_blank()
    if letter():
        while letter() or digit():
            token += p.ch
            getchar()
        retract()
        myword.typenum = reserve(token)
        myword.word = token
        return myword
    elif digit():
        while digit():
            token += p.ch
            getchar()
        retract()
        myword.typenum = 20
        myword.word = dtb(token)
        return myword
    elif p.ch == '=':
        getchar()
        if p.ch == '=':
            myword.typenum = 39
            myword.word = "=="
            return myword
        retract()
        myword.typenum = 21
        myword.word = "="
        return myword
    elif p.ch == '+':
        myword.typenum = 22
        myword.word = '+'
        return myword
    elif p.ch == '-':
        myword.typenum = 23
        myword.word = '-'
        return myword
    elif p.ch == '*':
        myword.typenum = 24
        myword.word = '*'
        return myword
    elif p.ch == '/':
        myword.typenum = 25
        myword.word = '/'
        return myword
    elif p.ch == '(':
        myword.typenum = 26
        myword.word = '('
        return myword
    elif p.ch == ')':
        myword.typenum = 27
        myword.word = ')'
        return myword
    elif p.ch == '[':
        myword.typenum = 28
        myword.word = '['
        return myword
    elif p.ch == ']':
        myword.typenum = 29
        myword.word = ']'
        return myword
    elif p.ch == '{':
        myword.typenum = 30
        myword.word = '{'
        return myword
    elif p.ch == '}':
        myword.typenum = 31
        myword.word = '}'
        return myword
    elif p.ch == ',':
        myword.typenum = 32
        myword.word = ','
        return myword
    elif p.ch == ':':
        getchar()
        if p.ch == "=":
            myword.typenum = 18
            myword.word = ":="
            return myword
        myword.typenum = 33
        myword.word = ':'
        return myword
    elif p.ch == ';':
        myword.typenum = 34
        myword.word = ';'
        return myword
    elif p.ch == '>':
        getchar()
        if p.ch == '=':
            myword.typenum = 37
            myword.word = '>='
            return myword
        retract()
        myword.typenum = 35
        myword.word = '>'
        return myword
    elif p.ch == '<':
        getchar()
        if p.ch == '=':
            myword.typenum = 38
            myword.word = '<='
            return myword
        retract()
        myword.typenum = 36
        myword.word = '<'
        return myword
    elif p.ch == '!':
        getchar()
        if p.ch == '=':
            myword.typenum = 40
            myword.word = '!='
            return myword
        retract()
        myword.typenum = -1
        myword.word = 'ERROR'
        return myword
    elif p.ch == '\0':
        myword.typenum = 1000
        myword.word = 'OVER'
        return myword
    elif p.ch == '#':
        myword.typenum = 0
        myword.word = '#'
        return myword
    else:
        myword.typenum = -1
        myword.word = 'ERROR'
        return myword



