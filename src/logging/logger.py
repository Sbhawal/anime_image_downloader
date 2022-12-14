import os

from src.utilities.constants import LOG_FOLDER

LOG_FILE = os.path.join(LOG_FOLDER, 'downloads.log')
print_log_file = os.path.join(LOG_FOLDER, 'print.log')

if not os.path.isdir(LOG_FOLDER):
    os.mkdir(LOG_FOLDER)

NUM_SET = set()
LINK_SET = set()

if os.path.isfile(LOG_FILE):
    with open(LOG_FILE, 'r') as f:
        lines = f.readlines()
        for line in lines:
            try:
                num, link = line.split(' - ')
                NUM_SET.add(num.split(':')[1].strip())
                LINK_SET.add(link)
            except:
                pass

def log_print(string,hidden=''):
    print_log = open(print_log_file, 'a')
    print(string)
    print(f'{string.strip()} + \t{hidden}', file=print_log)
    print_log.close()