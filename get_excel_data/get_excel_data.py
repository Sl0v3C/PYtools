# encoding: utf-8
# coding: utf-8
"""
Dump excel file to excel_data_Sheet1, ...
excel_data_Sheet1 will contains the data which in Sheet1, and split by "\t"
So you can just copy then into another excel file, it will keep the original format.
"""
from pyexcel_xls import get_data
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def read_xls_file(name):
    xls_data = get_data(name)

    return xls_data


def main():
    if len(sys.argv) != 2:
        print "Please input excel file name"
        print "Usage:"
        print "      python %s excel_to_dump" % sys.argv[0]
    else:
        filename = sys.argv[1]
        xls_data = read_xls_file(filename)
        for sheet in xls_data:
            out = open("./excel_data_%s" % sheet, "wb")
            for line in xls_data[sheet]:
                data = ''
                for item in line:
                    string = unicode(item).decode().encode('utf-8') + "\t"
                    data += string
                out.write(data + "\n")
            out.close()


if __name__ == '__main__':
    main()
