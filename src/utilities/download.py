import requests, os, re
# from com.helper.logger import *



log_folder = r'logs'

downloads_log = os.path.join(log_folder, 'downloads.log')
downloads_folder = r'downloads'

def set_download_folder(folder):
    global downloads_folder
    downloads_folder = r'downloads'



num_set = set()
url_set = set()
if os.path.exists(downloads_log):
    with open(downloads_log, 'r') as f:
        lines = f.readlines()
        for line in lines:
            try:
                num_set.add(line.split(' - ')[0].split(':')[1])
                url_set.add(line.split(' - ')[1].strip())
            except:
                pass
            


def check_filename(string):
    'remove numbers'
    string = re.sub(r'\d+', '', string)
    string = string.replace('%', '_')
    string = string.replace('-', '_')
    string = string.replace('Konachan', '')
    string = string.replace('.com', '')
    return string
    



def download_media(number, url):
    if number != -1:
        if number in num_set or url in url_set:
            return
    else:
        if url in url_set:
            print('Already downloaded', number)
            return
    filename = url.split('/')[-1]
    filename = check_filename(filename)
    r = requests.get(url, stream=True)
    # print('Downloading', filename)
    if r.status_code == 200:
        with open(f'{downloads_folder}\\{filename}', 'wb') as f:
            for chunk in r:
                f.write(chunk)
    if number != -1:
        num_set.add(number)
    url_set.add(url)
    with open(downloads_log, 'a') as f:
        f.write(f'num:{number} - {url}\n')
        # print('Downloaded', number)