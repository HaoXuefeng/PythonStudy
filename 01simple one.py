"""
print('HelloWorld')
print('I love study')
print('I like playing games with friends')
print('I like singing songs')
print()
print("OK, let's begin")
print('首先是计算一个整数的平方，并把结果返回到另一个变量里')


def fun(a):
    return a * a


n = input("请输入一个数字：")
n = int(n)
b = fun(n)
print('{0}输入数字的平方是{1}'.format(n, b))
"""

print("接下来我要打印一个乘法表，你想让他打印到几行呢？")
print("你输入的数字会决定乘法表打印的行数，所以应在1~9之间\n（PS：我觉得可以输入更多的说，所以我说你输入20试试？）")


# 这个函数是从1到a全部相乘并且把结果和过程打印出来
def mult(a):
    for i in range(1, a+1):
        print("{} * {} = {}".format(i, a, i * a), end='\t')
    return None


jug = 0
while jug == 0:
    x = input("请输入你想让这货打印到几乘几：\n")
    x = int(x)
    if x <= 0:
        print("别闹，不大于0你还想让我打印？")
    else:
        jug = 1
        print("恭喜你得到了自己想要的答案，按下回车来确认成果吧~")
        input()
for j in range(1, x+1):
    mult(j)
    print()   # 这是一行注释，注释的用法是#号后面要加空格
