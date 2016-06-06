import csv
import argparse
import sys
from collections import namedtuple


def commandline_parse():
    parser = argparse.ArgumentParser(prog='csv_test.py', description='print one'
                                     'or all the columns of csv file')
    parser.add_argument('csvfile', help='csv format fource file')
    parser.add_argument('-c', '--column', help='column name your want to print out')

    args = parser.parse_args()

    
    return args.csvfile, args.column



def process_csv_file(csvfile, column):    
    with open(csvfile, 'rt') as fr:
        csvrd = csv.reader(fr)
        
        rownum = 0
        for row in csvrd:
            if rownum == 0:  # header
                if row[-1].isspace():
                    header = row[:-1]
                else:
                    header = row
                Record = namedtuple('Record', header)
            else:
                row = row[:-1]
                record = Record(*row)
                if column:
                    print(record.SHORT_NAME)
                else:
                    print(row)
                
            rownum += 1
       # print(header)
        

def main():
    csvfile, column_name = commandline_parse()
    process_csv_file(csvfile, column_name)
    pass


if __name__ == '__main__':
    main()



