# 有1，2，3，4，四个数字，能组成多少个位数互不相同的，且不重复的三位数。
# 它们都是多少

count = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and j != k and k != j:
                print(i, j, k)
                count += 1
print("total:", count)
