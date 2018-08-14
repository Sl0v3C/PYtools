# encoding:utf-8
#!/usr/bin/python3

def cal(base, year, rate):
    return float(base * ((1.0 + rate) ** year))

def calAll(base, year, rate):
    if (year == 1):
        return cal(base, 1, rate)
    else:
        return cal(base, year, rate) + calAll(base, year - 1, rate)

YEAR = [6, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]

def main():
    base = int(input("每年交多少钱： "))
    year = int(input("交多少年： "))
    rate = float(input("平均年化利率： "))
    #print(calAll(base, year, rate))

    for i in YEAR:
        if (i < year):
            sumAll = calAll(base, i, rate)
        else:
            sumAll = cal(calAll(base, year, rate), i - year, rate)
        print i, u"年后可以获得：%f 万" % (sumAll / 10000)

if __name__ == "__main__":
    main()

