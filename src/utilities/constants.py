import configparser
import os

CONFIG_FILE_LOC = r'config.ini'


if not os.path.exists(CONFIG_FILE_LOC):
    print('Config file missing, Will iniialize a new config file.')

try:
    parser = configparser.ConfigParser()
    parser.read(CONFIG_FILE_LOC)
    print("Successfully read config file.")
except:
    print("Failed to read config file. Exiting program.")


# download_folder = config
sections = parser.sections()

LOG_FOLDER = parser['PATHS']['LOG_FOLDER']
DOWNLOAD_FOLDER = parser['PATHS']['DOWNLOAD_FOLDER']
WALLPAPER_FOLDER = parser['PATHS']['WALLPAPER_FOLDER']


PAGE_LIMIT = parser['GENERAL']['PAGE_LIMIT']
POST_LIMIT = parser['GENERAL']['POST_LIMIT']
LOGGING = parser['GENERAL']['LOGGING']

# [POST_TYPE
SAFE = parser['POST_TYPE']['SAFE']
EXPLICIT = parser['POST_TYPE']['EXPLICIT']
NSFW = parser['POST_TYPE']['NSFW']
BLACKLIST_TAGS = parser['POST_TYPE']['BLACKLIST_TAGS']

# [IMAGE_TYPE
EXTENSION = parser['IMAGE_TYPE']['EXTENSION']
ASPECT_RATIO = parser['IMAGE_TYPE']['ASPECT_RATIO']
MINIMUM_WIDTH = parser['IMAGE_TYPE']['MINIMUM_WIDTH']
MINIMUM_HEIGHT = parser['IMAGE_TYPE']['MINIMUM_HEIGHT']

MAKE_WALLPAPER = parser['WALLPAPER']['MAKE_WALLPAPER']
HEIGHT = parser['WALLPAPER']['HEIGHT']
WIDTH = parser['WALLPAPER']['WIDTH']


sites = []

if parser['SITES']['konachan.com']:
    sites.append('konachan.com')
if parser['SITES']['yande.re']:
    sites.append('yande.re')
if parser['SITES']['danbooru.donmai.us']:
    sites.append('danbooru.donmai.us')
if parser['SITES']['gelbooru.com']:
    sites.append('gelbooru.com')
if parser['SITES']['rule34.xxx']:
    sites.append('rule34.xxx')
if parser['SITES']['rule34.paheal.net']:
    sites.append('rule34.paheal.net')
if parser['SITES']['safebooru.org']:
    sites.append('safebooru.org')
if parser['SITES']['derpibooru.org']:
    sites.append('derpibooru.org')
    