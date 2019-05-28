import math
import time
import os

from random import randint,randrange,sample

"""
vscode两项设置
1.自动补全加上括号 python.autoComplete.addBrackets
2.自动补全后无提示的问题  Snippets Prevent Quick Suggestions
"""


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


#返回给定文件名的后缀名

def get_suffix(filename,has_dot=False):
    """
    获取文件名的后缀名
    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点，默认否
    :return 文件的后缀名
    """
    #rfind()函数 返回字符串最后一次出现的位置，如没有则返回-1,从右到左查找
    pos = filename.rfind('.')
    #如果找到.且不在开头和结尾，如果has_dat为否则往后取一位，使用切片的方式
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''

# 设计一个函数返回传入的列表中最大和第二大的元素的值,使用了冒泡排序

def max2(x):
    m1,m2 = (x[0],x[1]) if x[0] > x[1] else (x[1],x[0])
    for index in range(2,len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2

#判断指定的年月日是这一年的第几天

def is_leap_year(year):
    """
    判断指定的年份是不是闰年
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def which_day(year, month, date):
    """
    计算传入的日期是这一年的第几天
    return: 第几天
    """
    #这里是取数组的元素，如果为true则取list【1】为false则取list[0]
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total + date
#打印杨辉三角
def yhsj():
    num = int(input('Number of rows:'))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col],end='\t')
        print()

#双色球选号程序,对双色球规则不太了解，大致就是随机数，其中random模块的sample函数从列表中选择不重复的n个元素
def display(balls):
    '''
    输出列表中的双色球号码
    '''
    for index,ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|',end='')
        print('%02d' % ball, end='')
    print()

def random_select():
    '''
    随机选择一组号码
    '''
    red_balls = [x for x in range(1,34)]
    selected_balls = []
    selected_balls = sample(red_balls,6)
    selected_balls.sort()
    selected_balls.append(randint(1,16))
    return selected_balls

def lottery():
    '''
    投注
    '''
    n = int(input('机选几注: '))
    for _ in range(n):
        display(random_select())


#约瑟夫环问题
"""
《幸运的基督徒》
有15个基督徒和15个非基督徒在海上遇险，
为了能让一部分人活下来不得不将其中15个人扔到海里面去，
有个人想了个办法就是大家围成一个圈，
由某个人开始从1报数，报到9的人就扔到海里面，他后面的人接着从1开始报数，
报到9的人继续扔到海里面，直到扔掉15个人。由于上帝的保佑，
15个基督徒都幸免于难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。
"""

def joseph_circle():
    persons = [True] * 30
    counter, index, number = 0, 0 ,0
    while counter < 15:
        if persons[index]:
            number +=1
            if number == 9:
                persons[index] = False
                counter += 1
                number = 0
        index += 1
        index %= 30
    for person in persons:
        print('基督徒' if person else '非基督徒',end=' ')
    print()

#井字棋游戏

def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])


def jinggame():
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn = 'x'
        counter = 0
        os.system('clear')
        print_board(curr_board)
        while counter < 9:
            move = input('轮到%s走棋, 请输入位置: ' % turn)
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            os.system('clear')
            print_board(curr_board)
        choice = input('再玩一局?(yes|no)')
        begin = choice == 'yes'
jinggame()