# 闭包函数
# 闭包
# 闭指的是:该函数是一个内部函数
# 包指的是:指的是该内部的函数名字在外部被引用
# # # 1、函数定义阶段:
# # # 只检测函数体的语法( 工厂合不合格)，不执行函数体代码 （不使用工厂）
# def factory():#  制造一个工厂
#     print('正在制造手机')# 代码相对于员工或者机器
# # # 2、函数调用阶段:
# # # 1 先找到名字   (找到工厂的位置)
# # # # 2 根据名字调用代码   ( 加了括号执行工厂进行加工)
# #
# factory()

# 闭包
# 闭指的是:该函数是一个内部函数
# 包指的是:指的是该内部的函数名字在外部被引用
# def outer():# 没有调用outer(),但是创造了outer这个函数
#     # 1 只检测函数体outer的语法( 工厂合不合格)，不执行函数体代码 （不使用工厂）
#     print('外面的函数正在运行')
#     def inner():
#         print('里面的函数正在运行')
#     return inner# 3返回inner函数的内存地址  想象成一个钥匙 控制里面工厂
#
# # 创造了inner这个函数
# # print(outer())
# # # 4 得到里面工厂的钥匙 钥匙取一个名字innera
# #
# inner=outer() #2 定义了inner函数
# # print(inner)
# # # 5 里面钥匙加括号就可以开启里面的工厂
# inner()

# 为函数体传值的方式一：参数
# def func(x,y):
#     print(x+y)
# func(1,2)
# func(1,2)
# func(1,2)
# func(1,2)
# 为函数体传值的方式二：闭包
# def outer(x,y):
#     def func():
#         print(x + y)
#     return func
#
# func=outer(1,2)
# func()
# func()
# func()
# func()






