# 天生我才必有用
# 日语
with open('text1.txt',mode='w',encoding='shift_jis')as f1:
    f1.write('生まれながらにしてわたくし私はかならず必ずやく役にたつ立つ')

with open('text1.txt',mode='r',encoding='shift_jis')as f1:
    a=f1.read()
    print(a)

# ！！！总结非常重要的两点！！！
#1、保证不乱码的核心法则就是，字符按照什么标准而编码的，
# 就要按照什么标准解码，此处的标准指的就是字符编码
#2、在内存中写的所有字符，一视同仁，都是unicode编码，比如我们打开编辑器，
# 输入一个“你”，我们并不能说“你”就是一个汉字，此时它仅仅只是一个符号，
# 该符号可能很多国家都在使用，根据我们使用的输入法不同这个字的样式可能也不太一样。
# 只有在我们往硬盘保存或者基于网络传输时，
# 才能确定”你“到底是一个汉字，还是一个日本字，这就是unicode转换成其他编码格式的过程了