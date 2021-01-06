# coding:utf-8
# !/usr/bin/python3


def cal_month(base, rate):
    return float(base * (1.0 + rate))


def cal(base, year, rate):
    return float(base * ((1.0 + rate) ** year))


def cal_all(base, year, rate):
    if year == 1:
        return cal(base, 1, rate)
    else:
        return cal(base, year, rate) + cal_all(base, year - 1, rate)


YEAR = [6, 10, 15, 20, 25, 29]


def main():
    base = int(input("每年交多少钱： "))
    year = int(input("交多少年： "))
    rate = float(input("平均年化利率： "))
    sum_all = 0

    for i in YEAR:
        if i < year:
            sum_all = cal_all(base, i, rate)
        else:
            sum_all = cal(cal_all(base, year, rate), i - year, rate)
        print i, u"年后可以获得：%f 万" % (sum_all / 10000)

    mon_rate = rate / 12
    print u"30年后即60岁时每月领取4399元，按照年话利率转成月话利率来进行计算"
    for year in range(30, 76):
        for j in range(1, 13):
            sum_all -= 4399
            sum_all = cal_month(sum_all, mon_rate)

        print year + 30, u"岁时领取了每月的4399后还可以获得：%f 万" % (sum_all / 10000)


if __name__ == "__main__":
    main()

