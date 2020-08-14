# encoding: utf-8
# author:   AimerNeige
# github:   https://www.github.com/AimerNeige
# site:     https://AimerNeige.com

DOWNLOAD_LINK = [
    'URL_1',
    'URL_2',
    'URL_3'
]

USE_FILE_SAVE_DOWNLOAD_LINK = False
DOWNLOAD_LINK_FILE_PATH = '/home/aimerneige/Downloads/links.txt'

USE_PROXY = True
PROXY_URL = 'socks5://127.0.0.1:1080'

__TITLE__       = '%(title)s'
__UPLOADER__    = '%(uploader)s'
__UPLOAD_DATE__ = '%(upload_date)s'
__PLAYLIST__    = '%(playlist)s'
__EXT__         = '%(ext)s'
OUT_REDEFINE    = False
RESET_PATH      = False
SAVE_PATH       = '/home/aimerneige/Downloads/YouTube/'
FILE_NAME       = __TITLE__ + ' by ' + __UPLOADER__ + ' on ' + __UPLOAD_DATE__ + ' in ' + __PLAYLIST__ + '.' + __EXT__
# FILE_NAME       = 'Out_Video_Name'

DOWNLOAD_SUBTITLE = True
SET_SUBTITLE_LANG = False
SUBTITLE_LANGS = (
    'en',
    'zh'
)
SUBTITLE_LANG = 'en'

AUDIO_ONLY = False

REDEFINE_AUDIO_FORMAT = False
AUDIO_FORMATS = (
    'mp3',
    'wav',
    'ogg'
)
AUDIO_FORMAT = 'mp3'

REDEFINE_VIDEO_FORMAT = False
VIDEO_FORMATS = (
    'mp4',
    'mkv',
    'avi'
)
VIDEO_FORMAT = 'mp4'

DOWNLOAD_ALL     = True
DOWNLOAD_SPECIFY = False
PLAYLIST_SPECIFY = [1, 2, 4, 6, 8, 9]
DOWNLOAD_RANGE   = False
WITH_BEGIN       = True
PLAYLIST_BEGIN   = 3
WITH_END         = True
PLAYLIST_END     = 10

SPEED_LIMIT       = False
SPEED_LIMIT_VALUE = '50K'

RESUME_DOWNLOAD = False

SAVE_COMMAND_TO_FILE = False

# config end

command = 'youtube-dl'

if USE_PROXY:
    command = command + ' --proxy ' + '"' + PROXY_URL + '"'

if OUT_REDEFINE:
    out = ' -o "'
    if RESET_PATH:
        out = out + SAVE_PATH
    out = out + FILE_NAME + '"'
    command = command + out

if DOWNLOAD_SUBTITLE:
    if SET_SUBTITLE_LANG:
        command = command + ' --write-srt --sub-lang ' + SUBTITLE_LANG
    else:
        command = command + ' --write-auto-sub' 

if AUDIO_ONLY:
    command = command + ' -X'

if REDEFINE_AUDIO_FORMAT:
    command = command + ' --audio-format ' + AUDIO_FORMAT

if REDEFINE_VIDEO_FORMAT:
    command = command + ' --format ' + VIDEO_FORMAT

if not DOWNLOAD_ALL:
    if DOWNLOAD_SPECIFY:
        command = command + ' --playlist-items '
        specify = [str(i) for i in PLAYLIST_SPECIFY]
        command = command + ','.join(specify)
    elif DOWNLOAD_RANGE:
        if WITH_BEGIN:
            command = command + ' --playlist-start ' + str(PLAYLIST_BEGIN)
        if WITH_END:
            command = command + ' --playlist-end ' + str(PLAYLIST_END)

if SPEED_LIMIT:
    command = command + ' -r ' + SPEED_LIMIT_VALUE

if RESUME_DOWNLOAD:
    command = command + '-c'

links = ' '
if USE_FILE_SAVE_DOWNLOAD_LINK:
    links = links + '-a ' + DOWNLOAD_LINK_FILE_PATH
else:
    for link in DOWNLOAD_LINK:
        links = links + '"' + link + '"' + ' '

command = command + links

if SAVE_COMMAND_TO_FILE:
    with open('command.txt', 'w') as f:
        f.write(command)

print(command)
