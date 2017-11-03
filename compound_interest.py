#!/usr/bin/python3

def cal(base, year, rate):
    return float(base * ((1.0 + rate) ** year))

YEAR = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]

def main():
    one = int(input("第一年交多少钱： "))
    two = int(input("第二年交多少钱： "))
    three = int(input("第三年交多少钱： "))
    avg = float(input("平均年化利率： "))
    for i in YEAR:
        print(i, "年后可以获得：%f 万" % ((cal(one, i, avg) + cal(two, i - 1, avg) + cal(three, i - 2, avg)) / 10000))

if __name__ == "__main__":
    main()

