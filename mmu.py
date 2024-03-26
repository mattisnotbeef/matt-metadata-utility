#matt's metadata utility : modifies file metadata (quickly!!)

#BIG NOTE : only modifies mp3 files

#before use do: pip install mutagen

import mutagen
from mutagen.id3 import ID3, TIT2, TALB, TPE1, TPE2, TCOM, TCON, TDRC, TRCK
import os

router = os.getcwd()
specfilemp3 = '.mp3'

folder = os.listdir(router)

#quick edit
def quick_edit_mp3():
    length = len(folder)
    indexer = 0
    name = folder[indexer]
    while indexer < length:
        name = folder[indexer]
        if name == 'mmu.py' or name[-4:].lower() != specfilemp3: 
            indexer += 1
        if name != 'mmu.py' and name[-4:].lower() == specfilemp3:
           print(name)
           tags = ID3(name)
           songtitle = str(input('Enter a track title:\n'))
           album = str(input('Enter an album title:\n'))
           artist = str(input('Enter an artist name:\n'))
           trackno = str(input('Enter a track number:\n'))
           tags['TIT2'] = TIT2(encoding=3, text=songtitle)
           tags['TALB'] = TALB(encoding=3, text=album)
           tags['TPE1'] = TPE1(encoding=3, text=artist)
           tags['TRCK'] = TRCK(encoding=3, text=trackno)
           tags.save()
           indexer += 1

#quick edit + rename
def quick_edit_mp3_rename():
    length = len(folder)
    indexer = 0
    name = folder[indexer]
    while indexer < length:
        name = folder[indexer]
        if name == 'mmu.py' or name[-4:].lower() != specfilemp3: 
            indexer += 1
        if name != 'mmu.py' and name[-4:].lower() == specfilemp3:
           print(name)
           tags = ID3(name)
           songtitle = str(input('Enter a track title:\n'))
           album = str(input('Enter an album title:\n'))
           artist = str(input('Enter an artist name:\n'))
           trackno = str(input('Enter a track number:\n'))
           tags['TIT2'] = TIT2(encoding=3, text=songtitle)
           tags['TALB'] = TALB(encoding=3, text=album)
           tags['TPE1'] = TPE1(encoding=3, text=artist)
           tags['TRCK'] = TRCK(encoding=3, text=trackno)
           tags.save()
           os.rename(str(name), str(songtitle) + specfilemp3)
           indexer += 1

#full edit
def full_edit_mp3():
    length = len(folder)
    indexer = 0
    name = folder[indexer]
    while indexer < length:
        name = folder[indexer]
        if name == 'mmu.py' or name[-4:].lower() != specfilemp3: 
            indexer += 1
        if name != 'mmu.py' and name[-4:].lower() == specfilemp3:
           print(name)
           tags = ID3(name)
           songtitle = str(input('Enter a track title:\n'))
           album = str(input('Enter an album title:\n'))
           band = str(input('Enter a band\n'))
           artist = str(input('Enter an artist name:\n'))
           composer = str(input('Enter a composer:\n'))
           genre  = str(input('Enter a genre:\n'))
           year = str(input('Enter a year:\n'))
           trackno = str(input('Enter a track number:\n'))
           tags['TIT2'] = TIT2(encoding=3, text=songtitle)
           tags['TALB'] = TALB(encoding=3, text=album)
           tags['TPE2'] = TPE2(encoding=3, text=band)
           tags['TPE1'] = TPE1(encoding=3, text=artist)
           tags['TCOM'] = TCOM(encoding=3, text=composer)
           tags['TCON'] = TCON(encoding=3, text=genre)
           tags['TDRC'] = TDRC(encoding=3, text=year)
           tags['TRCK'] = TRCK(encoding=3, text=trackno)
           tags.save()
           indexer += 1

#full edit + rename
def full_edit_mp3_rename():
    length = len(folder)
    indexer = 0
    name = folder[indexer]
    while indexer < length:
        name = folder[indexer]
        if name == 'mmu.py' or name[-4:].lower() != specfilemp3: 
            indexer += 1
        if name != 'mmu.py' and name[-4:].lower() == specfilemp3:
           print(name)
           tags = ID3(name)
           songtitle = str(input('Enter a track title:\n'))
           album = str(input('Enter an album title:\n'))
           band = str(input('Enter a band\n'))
           artist = str(input('Enter an artist name:\n'))
           composer = str(input('Enter a composer:\n'))
           genre  = str(input('Enter a genre:\n'))
           year = str(input('Enter a year:\n'))
           trackno = str(input('Enter a track number:\n'))
           os.rename(str(name), str(songtitle) + specfilemp3)
           tags['TIT2'] = TIT2(encoding=3, text=songtitle)
           tags['TALB'] = TALB(encoding=3, text=album)
           tags['TPE2'] = TPE2(encoding=3, text=band)
           tags['TPE1'] = TPE1(encoding=3, text=artist)
           tags['TCOM'] = TCOM(encoding=3, text=composer)
           tags['TCON'] = TCON(encoding=3, text=genre)
           tags['TDRC'] = TDRC(encoding=3, text=year)
           tags['TRCK'] = TRCK(encoding=3, text=trackno)
           tags.save()
           os.rename(str(name), str(songtitle) + specfilemp3)
           indexer += 1
           
#part auto edit
def part_auto_edit_mp3():
    length = len(folder)
    indexer = 0
    name = folder[indexer]
    album = str(input('Enter an album title:\n'))
    artist = str(input('Enter an artist name:\n'))
    year = str(input('Enter a year:\n'))
    while indexer < length:
        name = folder[indexer]
        if name == 'mmu.py' or name[-4:].lower() != specfilemp3: 
            indexer += 1
        if name != 'mmu.py' and name[-4:].lower() == specfilemp3:
           print(name)
           tags = ID3(name)
           songtitle = str(input('Enter a track title:\n'))
           trackno = str(input('Enter a track number:\n'))
           tags['TIT2'] = TIT2(encoding=3, text=songtitle)
           tags['TALB'] = TALB(encoding=3, text=album)
           tags['TDRC'] = TDRC(encoding=3, text=year)
           tags['TPE1'] = TPE1(encoding=3, text=artist)
           tags['TRCK'] = TRCK(encoding=3, text=trackno)
           tags.save()
           indexer += 1

#part auto edit + rename
def part_auto_edit_mp3_rename():
    length = len(folder)
    indexer = 0
    name = folder[indexer]
    album = str(input('Enter an album title:\n'))
    artist = str(input('Enter an artist name:\n'))
    year = str(input('Enter a year:\n'))
    while indexer < length:
        name = folder[indexer]
        if name == 'mmu.py' or name[-4:].lower() != specfilemp3: 
            indexer += 1
        if name != 'mmu.py' and name[-4:].lower() == specfilemp3:
           print(name)
           tags = ID3(name)
           songtitle = str(input('Enter a track title:\n'))
           trackno = str(input('Enter a track number:\n'))
           tags['TIT2'] = TIT2(encoding=3, text=songtitle)
           tags['TALB'] = TALB(encoding=3, text=album)
           tags['TDRC'] = TDRC(encoding=3, text=year)
           tags['TPE1'] = TPE1(encoding=3, text=artist)
           tags['TRCK'] = TRCK(encoding=3, text=trackno)
           tags.save()
           os.rename(str(name), str(songtitle) + specfilemp3)
           indexer += 1
           
#program home
while True:
    prompt = int(input('Welcome to matt\'s metadata utility, please choose one of the following to get started:\n1 to modify track metadata track by track\n2 thoroughly modify metadata track by track\n3 partially autofill metadata, then fill in song name and track# track by track\n0 to quit\n'))
    
#program quit
    if prompt == 0:
        print('Goodbye')
        break

#quick editor
    elif prompt == 1:
        chooser = str(input('Rename files as well?\ny for yes or anything else to ignore\n'))
        if chooser == 'y':
            quick_edit_mp3_rename()
        else:
            quick_edit_mp3()

#thorough editor
    elif prompt == 2:
        chooser = str(input('Rename files as well?\ny for yes or anything else to ignore\n'))
        if chooser == 'y':
            full_edit_mp3_rename()
        else:
            full_edit_mp3()

#partial auto edit
    elif prompt == 3:
        chooser = str(input('Rename files as well?\ny for yes or anything else to ignore\n'))
        if chooser == 'y':
            part_auto_edit_mp3_rename()
        else:
            part_auto_edit_mp3()
        
#invalid input
    else:
        print('Invalid input!')
