# 输出9+9 9*9口诀，
# 进阶要求为 角 一致 (↙↖↗↘ 1*9 =9) or (↙↖↗↘ 9*9 =81)

# ↙
for i in range(1, 10):
    for j in range(1, i+1):
        print("%s*%s=%s\t" % (i, j, i*j), end="")
    print("")

print("------")
# ↖
for row in range(1, 10):  # 行
    for column in range(row, 10):  # 列
        print("%s*%s=%s\t" % (row, column, row * column), end="")
    print("")

print("------")
# ↗
for row in range(1, 10):  # 行
    for spacetimes in range(0, row-1):
        print("%s %s %s\t" % (' ', ' ', ' '), end="")
    for column in range(row, 10):  # 列
        print("%s*%s=%s\t" % (row, column, row * column), end="")
    print("")

print("------")
# ↘
for row in range(1, 10):
    for spacetimes in range(0, 9-row):
        print("%s %s %s\t" % (' ', ' ', ' '), end="")
    for column in range(1, row+1):
        print("%s*%s=%s\t" % (row, column, row * column), end="")
    print("")

