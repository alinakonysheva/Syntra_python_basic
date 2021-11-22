from exc1_main import C_STOPCHAR
from inputs import get_input_item

genres = ['unknown', 'pop', 'rock', 'opera', 'dance', 'trance', 'hardstyle']

C_MUSIC_CARRIER_MP3 = 1
C_MUSIC_CARRIER_STREAMING = 2
C_MUSIC_CARRIER_CD = 3
C_MUSIC_CARRIER_VINYL = 4
C_MUSIC_CARRIER_CASSETTE = 5

C_STOPCHAR = 'n'


class Music():
    __genre_type = 0
    __duration = 0   # in seconds
    __artist = ''
    __title = ''
    _type = 0

    def __init__(self, artist, title, genre_type, duration=0):
        self.artist = artist
        self.title = title
        self.genre_type = genre_type
        self.duration = duration

    @property
    def genre_type(self):  
        return self.__genre_type

    @genre_type.setter
    def genre_type(self, value):
        self.__genre_type = value

    @property
    def genre(self):
        return genres[self.genre_type]
    
    @property
    def artist(self):
        return self.__artist

    @artist.setter
    def artist(self, value):
        self.__artist = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def duration(self) -> int:
        """
        Returns:
            [int]: duration in seconds
        """
        return self.__duration

    @duration.setter
    def duration(self, value):
        return self.__duration

    @property
    def music_type(self):
        return self._type

    def __str__(self):
        return '{} - {} - {} - {}'.format(self.artist, self.title, self.genre, self.duration)


class Mp3(Music):
    _type = C_MUSIC_CARRIER_MP3


class Streaming(Music):
    _type = C_MUSIC_CARRIER_STREAMING


class Cd(Music):
    _type = C_MUSIC_CARRIER_CD


class Vinyl(Music):
    _type = C_MUSIC_CARRIER_VINYL


class Casette(Music):
    _type = C_MUSIC_CARRIER_CASSETTE
    

def create_song(music_type: int, artist: str, title: str, genre_type: int, duration: int=0) -> Music:
    if music_type == C_MUSIC_CARRIER_STREAMING:
        return Streaming(artist, title, genre_type, duration)
    elif music_type == C_MUSIC_CARRIER_MP3:
        return Mp3(artist, title, genre_type, duration)
    elif music_type == C_MUSIC_CARRIER_CD:
        return Cd(artist, title, genre_type, duration)
    elif music_type == C_MUSIC_CARRIER_VINYL:
        return Vinyl(artist, title, genre_type, duration)
    elif music_type == C_MUSIC_CARRIER_CASSETTE:
        return Casette(artist, title, genre_type, duration)


C_MUSIC_CARRIER_MP3 = 1
C_MUSIC_CARRIER_STREAMING = 2
C_MUSIC_CARRIER_CD = 3
C_MUSIC_CARRIER_VINYL = 4
C_MUSIC_CARRIER_CASSETTE = 5


def print_carriers():
    """prints the list of available music carriers
    """
    print('De verschillende types van muziek drager')
    print('{} - mp3'.format(C_MUSIC_CARRIER_MP3))
    print('{} - streaming'.format(C_MUSIC_CARRIER_STREAMING))
    print('{} - cd'.format(C_MUSIC_CARRIER_CD))
    print('{} - vinyl'.format(C_MUSIC_CARRIER_VINYL))
    print('{} - casette'.format(C_MUSIC_CARRIER_CASSETTE))

def print_genre_choices():
    """Print the list of available genres
    """
    print('De lijst van mogelijke genres"')
    cnt = 0
    for x in genres:
        print('{} - {}'.format(cnt, x))
        cnt +=1

def get_song(music_type: int) -> Music:
    """
        ask the user for input and creates a song
    Returns:
        Music: returns a song
    """
    artist = get_input_item('Geef uitvoerder: ')
    title = get_input_item('Geef title: ')
    genre_type = get_input_item('Geef genre (cijfer): ', 1)
    duration = get_input_item('Duur in seconden (0 is ongekend): ')
    
    return create_song(music_type, artist, title, genre_type, duration)

def create_songlist() -> list:
    # wihle
    print_carriers()
    print('-'*20)
    print_genre_choices()

    music = []
    inp = ''
    while inp != C_STOPCHAR:
        print('')
        inp = get_input_item('kies een type van muziekdrager, (n) om te stoppen: ', 1)
        if inp == C_STOPCHAR:
            continue
        music.append(get_song(inp))

    return music
    