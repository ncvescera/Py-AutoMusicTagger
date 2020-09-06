import sys
from mutagen.id3 import ID3, TIT2, TALB, TPE1, TPE2, TRCK
from os import listdir
from os.path import isfile, join
import youtube_dl as ydl


SEP     = '-'
path    = "./"
album   = ""
url     = ""


def main(argv):  # python3 script dir_path album_name
    global path
    global album
    global url

    url     = argv[0]

    # check if path is insert
    if len(argv) == 2:
        path    = argv[1]

    # download songs from url
    download(url)

    # get only mp3 files
    _onlyfiles = [
        f for f in listdir(path)
        if isfile(join(path, f)) and '.mp3' in f
        ]

    # print(_onlyfiles)

    # add metadata to songs downloaded with bandcamp format
    bandcamp_format(_onlyfiles)


def download(url: str):  # downlonad songs from url with predefine format
    settings = {
        'outtmpl': path + '%(track_number)s' + SEP + '%(album)s' + SEP + '%(artist)s' + SEP + '%(track)s.mp3'
    }

    with ydl.YoutubeDL(settings) as dl:
        dl.download([url])


def bandcamp_format(songs: list):  # add metatada to songs with bandcamp format
    for song in songs:
        song_data = song.split(SEP)

        _number = song_data[0]
        _album  = song_data[1]
        _artist = song_data[2]
        _band   = _artist
        _title  = song_data[3].replace('.mp3', '')

        tags = ID3()

        tags["TIT2"] = TIT2(encoding=3, text=_title)
        tags["TLAB"] = TALB(encoding=3, text=_album)
        tags["TPE2"] = TPE2(encoding=3, text=_band)
        tags["TPE1"] = TPE1(encoding=3, text=_artist)
        tags["TRCK"] = TRCK(encoding=3, text=_number)

        tags.save(path + song)

'''
def no_number(_onlyfiles):
    for file_ in _onlyfiles:
        _band   = _artist = file_.split('-')[0]
        _title  = file_.split('-')[1]      
        
        tags = ID3()

        tags["TIT2"] = TIT2(encoding = 3, text = _title)
        tags["TLAB"] = TALB(encoding = 3, text = album)
        tags["TPE2"] = TPE2(encoding = 3, text = _band)
        tags["TPE1"] = TPE1(encoding = 3, text = _artist)

        tags.save(path + file_)


def number_on_end(_onlyfiles):
    for file_ in _onlyfiles:
        _band   = _artist = file_.split('-')[0]
        _title  = file_.split('-')[1]
        _number = file_.split('-')[2]
        
        tags = ID3()

        tags["TIT2"] = TIT2(encoding = 3, text = _title)
        tags["TLAB"] = TALB(encoding = 3, text = album)
        tags["TPE2"] = TPE2(encoding = 3, text = _band)
        tags["TPE1"] = TPE1(encoding = 3, text = _artist)
        tags["TRCK"] = TRCK(encoding = 3, text = _number)

        tags.save(path + file_)


def number_on_start(_onlyfiles):
    for file_ in _onlyfiles:
        _number = file_.split('-')[0]
        _band   = _artist = file_.split('-')[1]
        _title  = file_.split('-')[2]
        
        
        tags = ID3()

        tags["TIT2"] = TIT2(encoding = 3, text = _title)
        tags["TLAB"] = TALB(encoding = 3, text = album)
        tags["TPE2"] = TPE2(encoding = 3, text = _band)
        tags["TPE1"] = TPE1(encoding = 3, text = _artist)
        tags["TRCK"] = TRCK(encoding = 3, text = _number)

        tags.save(path + file_)
'''

if __name__ == "__main__":
    main(sys.argv[1:])
