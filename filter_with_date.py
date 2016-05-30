from datetime import datetime
from datetime import timedelta
import glob
import os
import re
import shutil


PATH = r'D:\responsibility\daily\logs\files'

def filter(filename, start, end):
    '''start ==> start date like this 2016 Jan 07(length: 11)
    end ==> end date
    This function get lines from start to end date
    [start, end)
    '''
    assert(os.path.isabs(filename))
    startflg = False
    temp_file = create_temp_file(filename)
    date_pattern = r'(\d{4} [a-zA-Z]{3} \d{2})'
    pattern = '%Y %b %d'
    ptobj = re.compile(date_pattern)
    
    print('in file: {}'.format(filename))
    
    with open(filename) as f, open(temp_file, 'w') as fw:
        for line in f:
            m = ptobj.match(line)
            if m:
                date = datetime.strptime(m.group(1), pattern).date()
                if date < start:
                    continue
                elif  date == end:
                    return
                elif startflg != True:
                    startflg = True
            if startflg == True:
                fw.writelines(line)

def create_temp_file(filename):
    temp_file = os.path.join(filename + '.tmp')
    return temp_file
    


def main():
    today = datetime.today().date()
    start_date = today - timedelta(1, 0, 0)
    end_date = today
    
    for file in glob.glob(os.path.join(PATH, '*.log')):
        abspath = os.path.join(PATH, file)
        filter(abspath, start_date, end_date)
        shutil.move(create_temp_file(abspath), abspath)


if __name__ == '__main__':
    main()
