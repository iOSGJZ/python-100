#python中的集合与数学上的集合是一致的，不允许有重复元素，而且可以进行交集、并集、差集等运算
def main():
    #有重复元素时Python会直接过滤掉
    set1 = {1,2,3,3,3,3,}
    print(set1)
    print('length=',len(set1))
    set2 = set(range(1,10))
    print(set2)
    set1.add(4)
    set1.add(5)
    #更新一个数组到集合中
    set2.update([11,12])
    print(set1)
    print(set2)
    #discard和remove都可以移除元素，但remove在移除不存在的元素时会引发KeyError
    set2.discard(5)
    print(set2)
    if 4 in set2:
        set2.remove(4)
    print(set2)
    #遍历集合容器
    for elem in set2:
        print (elem ** 2, end=' ')
    print()
    # 将元组转换成集合
    set3 = set((1, 2, 3, 3, 2, 1))
    print(set3.pop())
    print(set3)
     # 集合的交集、并集、差集、对称差运算
    print(set1 & set2)
    # print(set1.intersection(set2))
    print(set1 | set2)
    # print(set1.union(set2))
    print(set1 - set2)
    # print(set1.difference(set2))
    print(set1 ^ set2)
    # print(set1.symmetric_difference(set2))
    # 判断子集和超集
    print(set2 <= set1)
    # print(set2.issubset(set1))
    print(set3 <= set1)
    # print(set3.issubset(set1))
    print(set1 >= set2)
    # print(set1.issuperset(set2))
    print(set1 >= set3)
    # print(set1.issuperset(set3))
#  Python中允许通过一些特殊的方法来为某种类型或数据结构自定义运算符，
# 上面的代码中我们对集合进行运算的时候可以调用集合对象的方法，
# 也可以直接使用对应的运算符，例如&运算符跟intersection方法的作用就是一样的，
# 但是使用运算符让代码更加直观。


if __name__ == "__main__":
    main()