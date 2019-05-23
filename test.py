import math
import time
import os

from random import randint

#双重循环输出乘法表
def table():
    for i in range(1,10):
        for j in range(1,i + 1):
            print ('%d*%d=%d' % (i,j,i*j),end='\t')
        print ()    



#输出2~99之间的素数

def prime():
    for num in range(2,100):
        is_prime = True
        for factor in range(2,int(math.sqrt(num)) + 1):
            if num % factor == 0:
                is_prime = False
                break
        if is_prime:
            print(num,end=' ')

'''
找出1~9999之间的所有完美数
完美数是除自身外其他所有因子的和正好等于这个数本身的数
'''

def perfect():
    strat = time.clock()
    for num in range(1,10000):
        sum = 0
        for factor in range(1,int(math.sqrt(num)) + 1):
            if num % factor == 0:
                sum += factor
                if factor > 1 and num / factor != factor:
                    sum += num / factor
        if sum == num and num != 1:
            print(num)
    end = time.clock()
    print("执行时间:",(end - strat), "秒")


def roll_dice(n=2):
    # 摇骰子
    # :patam n: 骰子的个数
    # :return 所有骰子点数之和
    total = 0
    for _ in range(n):
        total += randint(1,6)
    return total
#在参数名前面的*表示args是一个可变参数
#就是在调用add函数时可以传入0个或多个参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total

#在屏幕上显示跑马灯文字
def paomadeng():
    content = '人生苦短，我用Python。Life is short, I use Python'
    while True:
        #清理屏幕,不同系统的命令不同
        os.system('clear') #os.system('cls')
        #打印内容
        print(content)
        #休眠200毫秒
        time.sleep(0.2)
        #通过字符串的切片，不断的把content的第一个字符去掉拼接到句尾，形成循环
        content = content[1:] + content[0]

#生成指定长度的验证码，验证码由大小写字符组成
def generate_code(code_len=4):
    """
    生成指定长度的验证码

    :param code_len: 验证码的长度(默认4个字符)

    :return: 由大小写英文字母和数字构成的随机验证码
    """
    #所有可取的字符
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #取随机下标的最大值
    last_pos = len(all_chars) - 1
    code = ''
    #循环设定的长度的次数，每次随机一个下标取值拼接成code
    for _ in range(code_len):
        index = randint(0,last_pos)
        code += all_chars[index]
    return code



