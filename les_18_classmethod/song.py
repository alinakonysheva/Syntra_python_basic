from json import dumps, loads
from files import create_json_file, read_json_file
from inputs import get_input_item


class Song:
    __title = ''
    __artist = ''
    __album = ''
    __year = 0
    __played = 0

    def __init__(self):
        pass

    def __str__(self):

        def empty_as_unknown(prop):
            """internal __str__ helper function 

            Args:
                prop (str): property to test for empty

            Returns:
                str: unknown for empty string, otherwise prop value
            """
            if (type(prop) == str) and prop.strip() == '':
                return 'unknown'
            else:
                return prop

        return '{title} - {artist} - {year} - {album} ({played})'.format(
            title=empty_as_unknown(self.title),
            artist=empty_as_unknown(self.artist),
            album=empty_as_unknown(self.album),
            year=empty_as_unknown(self.year),
            played=self.played
        )

    @classmethod
    def createWithProperties(cls, title, artist, year, album=''):
        song = cls()
        song.__title = title
        song.__artist = artist
        song.__year = year
        song.__album = album
        return song

    @classmethod
    def fromDict(cls, value):
        song = cls()
        song.as_dict = value
        return song

    @property
    def title(self):
        return self.__title

    @property
    def artist(self):
        return self.__artist

    @property
    def year(self):
        return self.__year

    @property
    def album(self):
        return self.__album

    @property
    def as_dict(self):
        return dict(
            title=self.title,
            artist=self.artist,
            year=self.year,
            album=self.album,
            played=self.played
        )

    @as_dict.setter
    def as_dict(self, value):
        self.__title = value["title"]
        self.__artist = value["artist"]
        self.__year = value["year"]
        self.__album = value["album"]
        self.__played = value["played"]

    @property
    def as_json(self):
        return dumps(self.as_dict)

    @as_json.setter
    def as_json(self, value):
        ddict = loads(value)
        self.as_dict = ddict

    @property
    def played(self):
        return self.__played

    def play(self):
        """increase the playcount
        """
        self.__played += 1


class SongList:
    __filename = 'songs.json'

    def __init__(self, filename=''):
        self.__items = []
        if filename != '':
            self.__filename = filename

    @property
    def items(self):
        return self.__items

    @property
    def filename(self):
        return self.__filename

    @property
    def as_dict(self):
        mylist = []

        for song in self.items:
            mylist.append(song.as_dict)

        output = {}
        output['data'] = mylist

        return output

    @as_dict.setter
    def as_dict(self, value):
        mylist = value["data"]
        for item in mylist:
            song = Song.fromDict(item)
            self.items.append(song)

    @property
    def as_json(self):
        return dumps(self.as_dict)

    @as_json.setter
    def as_json(self, value):
        if value != '':
            d = loads(value)
            self.as_dict = d

    def save(self):
        """save the list
        """
        create_json_file(self.as_json, self.__filename)

    def load(self):
        """load the contents of this list
        """
        filecontents = read_json_file(self.__filename)
        if filecontents != '':
            self.as_json = filecontents

    def add_song(self, song):
        """add an object song to the interl list

        Args:
            song (Song): a song object
        """
        if song is not None:
            self.__items.append(song)

    def add_song_by_properties(self, title, artist, year, album):
        """add a song by its properites

        Args:
            title ([str]): title
            artist ([str]): artist
            year ([int]): year
            album ([str]): album
        """
        song = Song.createWithProperties(title, artist, year, album)
        self.__items.append(song)

    def remove_song(self, nr):
        """remove a song y id

        Args:
            nr (int): index in the list
        """
        if (nr > -1) and (nr < len(self.__items)):
            del self.__items[nr]

    def get_most_played(self):
        """get the most played song

        Returns:
            Song: a song from the list
        """
        most_played = None
        for x in self.__items:
            if most_played is None:
                most_played = x
            else:
                if x.played > most_played.played:
                    most_played = x
            # most_played = x if most_played is None or x.played > most_played

        return most_played


def create_song(artist, title, album, year):
    return Song.createWithProperties(title, artist, year, album)


def create_songlist():
    """create a list of songs and load existing songs

    Returns:
        SongList: object
    """
    songs = SongList()
    songs.load()
    return songs


def print_songlist(songs):
    """print all songs, display 

    Args:
        songs (SongList): a songlist object (does not need to contain items)
    """
    print('-' * 30)
    print('song lijst')
    if songs is not None and len(songs.items) > 0:
        counter = 0
        for song in songs.items:
            counter += 1
            print('{cnt} - {song}'.format(cnt=counter, song=song))
    else:
        print('geen songs gevonden')


def get_input_song():
    print('-' * 30)
    print('song toevoegen')
    artist = get_input_item('geef de artiest: ')
    title = get_input_item('title: ')
    year = get_input_item('geef het jaar: ', 1)
    album = get_input_item('geef het album: ')

    return create_song(artist, title, album, year)


def add_song(songs):
    """add song, display 

    Args:
        songs (SongList): a songlist object (does not need to contain items)
    """
    if songs is not None:
        song = get_input_song()
        songs.add_song(song)


def remove_song(songs):
    if songs is not None:
        print('-' * 30)
        print('song wissen')
        print_songlist(songs)
        nr = get_input_item('geef uw song nummer in om te wissen: ', 1)
        songs.remove_song(nr - 1)


def play_song(songs):
    if songs is not None:
        print('-' * 30)
        print('song afspelen')
        print_songlist(songs)
        nr = get_input_item('geef uw song nummer in om af te spelen: ', 1)
        songs.items[nr - 1].play()


def most_played(songs):
    if songs is not None:
        print(songs.get_most_played())
