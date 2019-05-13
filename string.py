def main():
    str1 = 'hello, world!'
    # 通过len函数计算字符串的长度
    print (len(str1))
    # 获得字符串首字母大写的拷贝
    print(str1.capitalize())
    # 获得字符串变大写后的拷贝
    print(str1.upper())
    #从字符串中查找子串所在位置
    print(str1.find('or'))#返回的是下标
    print(str1.find('shit'))#未包含则返回-1
    # 与find类似但找不到子串的时候会引发异常
    # print(str1.index('or'))
    #检查字符串是否以置顶的字符串开头,返回bool
    print(str1.startswith('He'))
    print(str1.startswith('hel'))
    #检查字符串是否以置顶的字符串结尾
    print(str1.endswith('!'))
    #将字符串以指定的宽度居中并在两侧填充指定的字符
    print(str1.center(50,'*'))
    #将字符串以指定的宽度靠右放置左侧填充指定的字符
    print(str1.rjust(49,"*"))
    print(str1.ljust(49,"*"))
    
    str2 = 'abc123456'
    #从字符串中取出指定位置的字符，以下标计算
    print(str2[2])
    #字符串切片，也就是字符串截取,[]为左包含右不包含
    print(str2[2:5])  # c12
    print(str2[2:])  # c123456
    print(str2[2::2])  # c246
    print(str2[::2])  # ac246
    print(str2[::-1])  # 654321cba
    print(str2[-3:-1])  # 45
    #检查字符串是否由数字构成
    print(str2.isdigit())
    #检查字符串是否由字母构成
    print(str2.isalpha())
    #检查字符串是否由字母和数字构成
    print(str2.isalnum)
    #去除字符串左右两侧的空格的拷贝
    str3 = '    54101194@qq.com '
    print (str3.strip())
if __name__ == "__main__":
    main()