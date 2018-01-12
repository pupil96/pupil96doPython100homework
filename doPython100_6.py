# use * print C
# ******
# *
# *
# *
# ******

#       *****
#     *
#    *
#    *
#    *
#     *
#       *****

# y=ax^2+bx+c


def drawstar(i_times=1):
    print("***"*i_times, end="")


def drawspace(i_times=1):
    print("   "*i_times, end="")


print("Hello Python world")
print("use * print graph like C")
print("print two kinds of function to print.")
print("1.hardprint\n2.calculateprint")
select = int(input("please input 1/2 to choose the function:"))

if select == 1:
    print('the function1 works:')
    print('*'*10)
    for i in range(5):
        print('*         ')
    print('*'*10)

else:
    print("function1 wasn't been choosen")

if select == 2:
    print('the function2 works:')
    ln = 12  # 一个与宽度挂钩的系数
    for i in range(1, 24):  # 打印一个占24行的C
        times = int((ln-i)**2*0.1)+1  # 一元二次 弧线 的打印次数
        drawspace(times)  # 打印空格
        drawstar()  # 打印星好--C的轨迹
        drawstar()
        drawstar()

        if times == 3:  # 希望打印出中间厚的效果
            print('*')  # 希望能达到一个相对美观的效果  没用 end = ""
        elif times == 2:
            print('**')
        elif times == 1:
            print('***')
        print('')  # 换行
