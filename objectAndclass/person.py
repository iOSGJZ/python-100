"""
将属性名以下划线开头，仅仅是暗示属性是受保护的，不建议外接直接访问
使用@property包装器来包装getter和setter方法，使得对属性的访问既安全又方便

python是一门动态语言，动态语言允许我们在程序运行时给对象绑定新的属性或方法，当然
也可以对已绑定的属性和方法解绑。但如果需要限定自定义类型的对象只能绑定某些属性，可以
通过在类中定义__slots__变量来进行限定，只对当前类的对象生效，对子类不起任何作用

"""
from math import sqrt
from abc import ABCMeta, abstractmethod
class Person(object):
    __slots__ = ('_name','_age','_gender')
    def __init__(self, name, age):
        self._name = name
        self._age = age

    #访问器 - getter方法
    @property
    def name(self):
        return self._name

    @property    
    def age(self):
        return self._age

    #修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩英雄联盟' % self._name)
        else:
            print('%s正在玩魔兽世界' % self._name)

#继承和多态
class Student(Person):
    #继承自Person类的学生类
    def __init__(self, name, age, grade):
        super().__init__(name,age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self,grade):
        self._grade = grade
    
    def study(self, course):
        print('%s的%s正在学习%s' % (self._grade, self._name, course))

class Teacher(Person):
    #继承自Person的老师类
    def __init__(self, name, age, title):
        super().__init__(name,age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,title):
        self._title = title

    def teach(self,course):
        print('%s%s正在讲%s' % (self._name,self._title,course))

#抽象类的使用
"""
Pet作为一个抽象类，所谓抽象类就是不能够创建对象的类，这种类的存在就是专门
为了让其他类去继承它。Python从语法层面并没有像Java或C#那样提供对抽象类的
支持，但是我们可以通过abc模块的ABCMete元类和abstractmethod包装器来达到
抽象类的效果，如果一个类中存在抽象方法那么这个类就不能够实例化。在Dog类和
Cat类中make_voice抽象方法进行了重写并给出了不同的实现，当调用时就表现出了
多态行为（同样的方法做了不同的事）.

"""
class Pet(object,metaclass=ABCMeta):
    #宠物类
    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        """发出声音"""
        pass

class Dog(Pet):
    def make_voice(self):
        print('%s: 汪汪汪。。。' % self._nickname)

class Cat(Pet):
    def make_voice(self):
        print('%s: 喵喵喵。。。' % self._nickname)

#静态方法和类方法
"""
有时，我们需要定义一些方法，比如验证传入的参数是否正确，这个方法应该
是这个类调用，而不是这个类的对象调用，使用静态方法来解决 @staticmethod

类方法与静态方法类似，类方法的第一个参数约定名为cls,它代表的是当前类相关的信息
的对象（类本身也是一个对象，有的地方称之为类的元数据对象），通过这个参数可以获取
和类相关的信息并且可以创建出类的对象

"""

class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
    #静态方法
    @staticmethod
    def is_valid(a, b, c):  
        return a+b > c and b +  c > a and a  +  c > b

    #类方法
    @classmethod
    def equilateral_triangle(cls):
        return cls(3,3,3)
    
    #周长
    def perimeter(self):
        return self._a +  self._b + self._c
    #面积
    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))



def main():
    person = Person('王大锤',12)
    person.play()
    person.age = 22
    person.play()
    person._gender = '男'
    # person._job = 'jigong' AttributeError: 'Person' object has no attribute '_job'
    #三角型静态方法的验证
    a,b,c = 3,4,5
    #静态方法和类方法都是通过给类发消息来调用
    if Triangle.is_valid(a,b,c):
        t = Triangle(a,b,c)
        print(t.perimeter())
        #也可以通过给类发消息来调用对象方法但要传入接收消息的对象作为参数
        print(Triangle.perimeter(t))
        print(t.area())
        print(Triangle.area(t))
    else:
        print('无法构成三角型')
    #类方法的使用
    et = Triangle.equilateral_triangle()
    print(et.perimeter())

    #继承和多态的验证
    stu = Student('蒙多',15,'高三')
    stu.study('英语')
    stu.play()
    t = Teacher('凯南',28,'导师')
    t.teach('python从入门到放弃')
    t.play()

    pets = [Dog('大黄'),Cat('加菲'),Dog('小白')]
    for pet in pets:
        pet.make_voice()

if __name__ == "__main__":
    main()