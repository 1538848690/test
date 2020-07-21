# 单例模式：
# 开发模式：单例模式


class Student:
    pass


s = Student()
s1 = Student()
s2 = Student()
print(s)
print(s1)
print(s2)


class Singleton:
    # 私有化
    __instance = None
    name = 'jack'

    # 重写__new__
    def __new__(cls, *args, **kwargs):
        print('---------->__new__')
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            print('-------->2')
            return cls.__instance

    def show(self, n):
        print('----------->', Singleton.name, n)


s = Singleton()
s1 = Singleton()

print(id(s))
print(id(s1))
s.show(234)
s1.show(32)