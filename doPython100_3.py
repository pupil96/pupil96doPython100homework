# 一个整数，它加上100后是一个完全平方数，再加上268又是一个完全平方数。求这个数（100000以类）
import math

count = 0  # 设置一个计数器，将符合要求的 +1
numlist = []  # 用来存放符合要求的数
for i in range(1, 100000):
    p = i + 100  # 假设的一个完全平方数
    q = p + 268  # 假设的另一个完全平方数
    x = int(math.sqrt(p))  # 如果是完全平方数，则整型转换不会有精度损失
    y = int(math.sqrt(q))
    print("i: %s \n p: %s \n q: %s \n x: %s \n y: %s \n" % (i, p, q, x, y))
    if x**2 == p and y**2 == q:
        print("---------\n---------\n the nuber is: ", i)
        count += 1
        numlist.append(i)

print("count:%s \nnumlist:%s" % (count, numlist))
