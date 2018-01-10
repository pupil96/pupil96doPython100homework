# 输入三个整数，把这个三个数由小到大输出


def my_print_list(my_list):
    for n in my_list:
        print("%s  " % n, end="")


# 方法一：一切从偷懒开始
def my_func1():
    my_list = []
    for i in range(3):
        temp_num = int(input("please input a integer:"))
        my_list.append(temp_num)

    my_list.sort()
    my_print_list(my_list)


# 方法二：自力更生
def my_func2():
    my_print_list(my_sort(my_get_intlist()))


def my_get_intlist():
    my_list = []
    conuter = 1
    while conuter <= 3:
        # noinspection PyBroadException
        try:
            temp_num = int(input("please input a integer:"))
            my_list.append(temp_num)
        except Exception:
            print("illegal input")
            conuter -= 1
        conuter += 1
    return my_list


def my_sort(int_list):
    length = len(int_list)
    for num1 in range(length):
        for num2 in range(length - num1 - 1):
            if int_list[num2] > int_list[num2+1]:
                int_list[num2] = int_list[num2] + int_list[num2+1]
                int_list[num2+1] = int_list[num2] - int_list[num2+1]
                int_list[num2] = int_list[num2] - int_list[num2+1]

    return int_list


if __name__ == "__main__":
    my_func1()
    print()
    my_func2()
