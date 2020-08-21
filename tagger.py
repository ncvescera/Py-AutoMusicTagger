import sys
from mutagen.id3 import ID3, TIT2, TALB, TPE1, TPE2, TRCK
from os import listdir
from os.path import isfile, join

album = ""
path = ""

# python3 script dir_path album_name
def main(argv):
    global path
    global album 

    path   = argv[0]
    album  = argv[1]

    _onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

    #no_number(_onlyfiles)
    number_on_end(_onlyfiles)
    
        
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


if __name__ == "__main__":
    main(sys.argv[1:])
