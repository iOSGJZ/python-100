
import os
import time
from math import sqrt
"""
在Python中可以使用class关键字定义类，
然后在类中通过之前学习过的函数来定义方法，
这样就可以将对象的动态特征描述出来
"""

class Student(object):
    #__init__是一个特殊方法用于在创建对象时进行初始化操作
    #通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, coures_name):
        print('%s正在学习%s.'%(self.name,coures_name))

    #PEP 8要求标识符的名字用全小写多个单词用下划线连接
    #但是很多程序员和公司更倾向于使用驼峰命名法
    #写在类中的函数，我们通常称之为（对象的）方法，这些方法就是对象可以接收的消息。
    def watch_av(self):
        if self.age < 18:
            print('%s只能观看《喜洋洋》。' % self.name)
        else:
            print('%s正在观看岛国爱情动作片。' % self.name)

#创建和使用对象
def main():
    stu1 = Student('李雷',33)
    stu1.study('python程序设计')
    stu1.watch_av()
    stu2 = Student('韩梅梅',15)
    stu2.study('思想品德')
    stu2.watch_av()    

#访问可见性问题,（私有和公开属性）
#如果希望属性时私有的，再给属性命名时可以用两个下划线作为开头
#但python并没有从语法上严格保证私有属性或方法的私密性，它只是给私有的属性或者方法换了一个名字来“妨碍”对它们的访问
#私有方法只需要通过object._ClassName.__def或属性就可以访问
class Test:
    def __init__(self,foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')

"""
在实际开发中，我们并不建议将属性设置为私有的，
因为这会导致子类无法访问。
所以大多数Python程序员会遵循一种命名惯例
就是让属性名以单下划线开头来表示属性是受保护的，
本类之外的代码在访问这样的属性时应该要保持慎重。
这种做法并不是语法上的规则，
单下划线开头的属性和方法外界仍然是可以访问的，
所以更多的时候它是一种暗示或隐喻
"""

class Clock(object):
    #python中的函数是没有重载的概念的
    #因为python中函数的参数没有类型而且支持缺省参数和可变参数
    #用关键字参数让构造器可以传入任意多个参数来实现其他语言中的构造器重载
    #数字始终
    def __init__(self, **kw):
        """初始化方法
        :param hour: 时
        :param minute: 分
        :param second: 秒
        """
        if 'hour' in kw and 'minute' in kw and 'second' in kw : 
            self._hour = kw['hour']
            self._minute = kw['minute']
            self._second = kw['second']
        else:
            tm = time.localtime(time.time())
            self._hour = tm.tm_hour
            self._minute = tm.tm_min
            self._second = tm.tm_sec


    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0
    
    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)


class Point(object):
    def __init__(self, x=0, y=0):
        """初始化方法
        
        :param x: 横坐标
        :param y: 纵坐标
        """
        self.x = x
        self.y = y

    def move_to(self, x, y):
        """移动到指定位置
        
        :param x: 新的横坐标
        "param y: 新的纵坐标
        """
        self.x = x
        self.y = y  

    def move_by(self, dx, dy):
        """移动指定的增量
        
        :param dx: 横坐标的增量
        "param dy: 纵坐标的增量
        """
        self.x += dx
        self.y += dy

    def distance_to(self,other):
        """计算与另一个点的距离
        
        :param other: 另一个点
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        """对象的字符串表达式"""
        return '(%s, %s)' % (str(self.x),str(self.y))

    def __del__(self):
        """析构器"""
        print('销毁对象')



if __name__ == "__main__":
    main()
    test = Test('hello')
    test._Test__bar()
    print(test._Test__foo)

    p1 = Point(3,5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1, 2)
    print(p2)
    print(p1.distance_to(p2))

    # clock = Clock(hour=23, minute=59, second=58)
    # clock = Clock()
    # while True: 
    #     os.system('clear')
    #     print(clock.show())
    #     time.sleep(1)
    #     clock.run()

