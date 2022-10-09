from myClass import *

print(MyClass.classVar)
MyClass.setClassVar()
print(MyClass.classVar)
MyClass.classVar = 19
print(MyClass.classVar)

mc = MyClass()
print(mc.classVar)
mc.setClassVar()
print(mc.classVar)
