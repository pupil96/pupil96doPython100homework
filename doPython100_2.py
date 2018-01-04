# q2 企业发放的奖金根据利润提成。利润低于或等于10万元，奖金可以提成10%：利润高于10万元，低于20万元时，低于
# 10万元的部分按10%提成，高于10万元的提成7.5%；以此类推：20~40：5%；40~60:3%;60~100:1.5%;100~x:1%.
# 从键盘输入当月利润，返回奖金总数

def calculatebonus(profit):
    if profit <= 100000:
        bonus = profit * 0.1
        return bonus
    elif profit <= 200000:
        bonus = 100000 * 0.1 + (profit - 100000) * 0.075
        return bonus
    elif profit <= 400000:
        bonus = 100000 * 0.1 + 100000 * 0.075 + (profit-200000) * 0.05
        return bonus
    elif profit <= 600000:
        bonus = 100000*0.1 + 100000 * 0.075 + 200000 * 0.05 + (profit - 400000) * 0.03
        return bonus
    elif profit <= 1000000:
        bonus = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + (profit-600000) * 0.015
        return bonus
    elif profit > 1000000:
        bonus = 100000*0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + 400000 * 0.015 + (profit - 1000000) * 0.01
        return bonus
    else:
        print("something was wrong!")


outprofit = int(input("please input the profit: "))
newbonus = calculatebonus(outprofit)
print("------the final bonus------\n :", newbonus)
