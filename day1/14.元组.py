#一：基本使用：tuple
# 1 用途：记录多个值，当多个值没有改的需求，此时用元组更合适
# 2 定义方式：在()内用逗号分隔开多个任意类型的值
t = (1,2,'大海',(2,3),['红海',2,3])
print(t)
print(type(t))
print(t[0])
# t[0]=5
print(t)
print(t[4][0])
