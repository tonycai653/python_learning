import datetime
import os
import shutil
import re
import csv


today_date = datetime.date.today()
delta = datetime.timedelta(days=1)
yesterday_date = today_date - delta

months = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5,
              'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10,
              'Nov': 11, 'Dec': 12}


def get_date(line):        
        splits = line.split()
        if len(splits) >= 3:
            year, month, day, *_ = splits
        else:
            return None
        if year.isdigit() and month in months:
            year = int(year)
            month = months[month]
            day = int(day)
            return datetime.date(year, month, day)
        

def truncate(logfile, start_date=yesterday_date, end_date=today_date):
    '''get log content's date between start_date and end_date,
       end_date not included. [start_date, end_date)'''
    tempfile = 'tmp_' + str(os.getpid())
    with open(logfile, 'rt') as fr, open(tempfile, 'wt') as fw:
        sf = False
        for line in fr:           
                line_date = get_date(line)
                if line_date is None:
                    if sf  == True:
                        fw.writelines(line) #write this line to temp file
                    continue
                elif line_date < start_date:
                    continue
                elif line_date == start_date:
                    sf = True
                    fw.writelines(line)
                elif line_date == end_date:
                    break
                else:
                    fw.writelines(line)  
    shutil.move(tempfile, logfile)


tr_entry = {'Carrier': 'Input received for  with carrier ID -([\w_]*)',
            'TrunkGroup': 'Input received for Trunk Group  with Trunk Group ID -(\d+)',
            'TrunkGroupClass':'Input received for  Trunk Group Class Id -(\d+)'}


def process(logfile, outputfile='SURF.csv'):
    with open(logfile, 'rt') as fr, open(outputfile, 'wt') as fw:
        csvout = csv.writer(fw, lineterminator='\n')
        for line in fr:
            for tr, entry in tr_entry.items():
                #print(tr, entry)
                m = re.search(entry, line)
                if m:
                    row = [get_date(line).isoformat(), '', 'SURF', tr,
                           m.group(1), '', 'SUCCESS', '', ''] 
                    csvout.writerow(row)

if __name__ == '__main__':
    log = 'SURF_TIBCO.log'
    print('Starting truncating')
    truncate(log)
    print('Truncation complete')

    print('*' * 50)
    print('Starting processing')
    process(log)
    print('Proessing complete')

    
            
            
            

