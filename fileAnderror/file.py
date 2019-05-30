"""open函数
参数：文件名，操作模式，编码信息
操作模式：'r' 读取，‘w’写入（会先截断之前的内容）,'x'写入（如果文件已经存在会产生异常）
'a'追加（将内容写入到已有文件的末尾）,'b'二进制模式,'t'文本模式（默认）
'+'更新（既可以读又可以写）
"""

"""
在Python中，我们可以将那些在运行时可能会出现状况的代码放在try代码块中，在try代码块
的后面可以跟上一个活或多个except来捕获可能出现的异常状况。如下所示，读取文件的过程
中，文件找不到会引发FileNotFoundError，指定了未知编码会引发LookupError,
而如果读取文件时无法按指定方式解码会引发UnicodeDecodeError，
我们在try后面跟上了三个except分别处理这三种不同的异常状况。
最后我们使用finally代码块来关闭打开的文件，释放掉程序中获取的外部资源，
由于finally块的代码不论程序正常还是异常都会执行到（甚至是调用了sys模块的exit函数退出Python环境，finally块都会被执行，因为exit函数实质上是引发了SystemExit异常），
因此我们通常把finally块称为“总是执行代码块”，它最适合用来做释放外部资源的操作。
如果不愿意在finally代码块中关闭文件对象释放资源，也可以使用上下文语法，
通过with关键字指定文件对象的上下文环境并在离开上下文环境时自动释放文件资源
"""

import time
from math import sqrt
import json
import requests

def main():
    f = None
    try:
        f = open('致橡树.txt','r',encoding='utf-8')
        print(f.read())
        #with关键词读取
        with open('致橡树.txt', 'r' , encoding='utf-8') as f:
            print(f.read())
        
        #for-in循环逐行读取
        with open('致橡树.txt', 'r', encoding='utf-8') as f:
            for line in f:
                print(line, end=' ')
                time.sleep(0.5)
        print()

        #readlines方法将文件按行读取到一个列表容器中
        with open('致橡树.txt') as f:
            lines = f.readlines()
        print(lines)

    except FileNotFoundError:
        print('无法打开指定的文件')
    except LookupError:
        print('指定了未知的编码')
    except UnicodeDecodeError:
        print('读取文件时解码错误')
    # finally:
    #     if f:
    #         f.close()

"""
文件的写入
在使用open函数时指定好文件名并将文件模式设置为'w'即可。
注意如果需要对文件内容进行追加式写入，应该将模式设置为'a'。
如果要写入的文件不存在会自动创建文件而不是引发异常。
下面的例子演示了如何将1-9999之间的素数分别写入三个文件中
（1-99之间的素数保存在a.txt中，100-999之间的素数保存在b.txt中，1000-9999之间的素数保存在c.txt中）
"""
def is_prime(n):
    '''判断是否为素数'''
    #assert断言, 如果后面的判断出错则会抛出异常,参数：条件，抛出的异常
    assert n > 0,'不是一个大于0的数'
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    
    return True if n !=1 else False

def write_prime():
    filenames = ('a.txt','b.txt','c.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename,'w', encoding='utf-8'))
        for number in range(1,10000):
            if is_prime(number):
                if number < 100:
                    fs_list[0].write(str(number) + '\n')
                elif number < 1000:
                    fs_list[1].write(str(number) + '\n')
                else:
                    fs_list[2].write(str(number) + '\n')
    except IOError as ex:
        print(ex)
        print('写文件时发生错误')
    finally:
        for fs in fs_list:
            fs.close()
    print('操作完成')

#读取写入二进制文件，如图片
def write_read_bytes():
    try:
        with open('test.png','rb') as fs1:
            data = fs1.read()
            print(type(data))

        with open('copy.png','wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('指定的文件无法打开')
    except IOError as e:
        print('读写文件时出现错误')
    print('图片读写结束')

#读写json数据，使用json模块
"""
json 模块主要有四个比较重要的函数，分别是：
dump -将Python对象按照json格式序列化到文件中
dumps -将Python对象处理成json格式的字符串
load -将文件中的json数据反序列化成对象
loads -将字符串的内容反序列化成Python对象
"""
def w_json():
    mydict = {
        'name':'伊泽瑞尔',
        'age':25,
        'qq':123456,
        'friends':['拉克丝','锤石'],
        'cars':[
            {'brand':'BYD','max_speed':180},
            {'brand':'Benz','max_speed':280},
            {'brand':'BMW','max_speed':320}
        ]
    }
    try:
        with open('data.json','w',encoding='utf-8') as fs:
            json.dump(mydict,fs)
    except IOError as e:
        print(e)
    print('保存json数据完成')

#通过json模块解析json数据并显示新闻标题
def getNews():
    resp = requests.get('http://api.tianapi.com/guonei/?key=7e3873b2fc05c937698f052b13adc6c3&num=10')
    data_model = json.loads(resp.text)
    for news in data_model['newslist']:
        print(news['title'])
if __name__ == "__main__":
    getNews()
    
