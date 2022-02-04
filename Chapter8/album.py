def make_album(artist, album_title, tracks=0):
    '''Create an dictionary from user input of artist and album title'''
    if tracks > 0:
        return {'artist': artist, 'album title': album_title, 'track count': tracks }
    else:
        return {'artist': artist, 'album title': album_title }
print(make_album('Creed', 'Greatist Hits', 13))
print(make_album('Led Zepplin', 'House of the Holy'))
print(make_album('Def Leppard', 'Hysteria', 12))

quit = False
while quit != True:
    artist = input('Enter the artist for the album you want to create: ')
    album = input('Enter the album title: ')
    trackCount = int(input('Enter the number of tracks or 0 if you do not know: '))
    print(make_album(artist, album, trackCount))
    userResponse = input('Do you want to enter another? Enter N to quit: ')
    if userResponse.lower() == 'n':
        quit = True
