from inputs import get_input_item
from music import create_songlist, C_MUSIC_CARRIER_CASSETTE, C_MUSIC_CARRIER_MP3,\
     C_MUSIC_CARRIER_STREAMING, C_MUSIC_CARRIER_CD, C_MUSIC_CARRIER_VINYL
"""
music
    mp3
    streaming
    cd
    vinyl
    casette

    genre
    uitvoerder
    titel
    duur

    lijst steken
    output
      -> alles of 1 of meerdere types
"""

def do_output(music: list):
    """
    wat wenst u te zien
    alles, of een bepaalde type
    """ 
    print('Maak een selectie van het type dat u wenst te zien: ')
    print('0 - alles')
    print('{} - mp3'.format(C_MUSIC_CARRIER_MP3))    
    print('{} - streaming'.format(C_MUSIC_CARRIER_STREAMING))
    print('{} - cd'.format(C_MUSIC_CARRIER_CD))    
    print('{} - vinyl'.format(C_MUSIC_CARRIER_VINYL))
    print('{} - vinyl'.format(C_MUSIC_CARRIER_CASSETTE))
    inp = get_input_item('geef het getal van het type dat u wenst te zien: ', 1)

    for x in music:
        if inp == 0 or (x.music_type == inp):
            print(x)            


def main():
    songs = create_songlist()
    do_output(songs)

if __name__ == '__main__':
    main()

