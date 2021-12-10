import os
import unittest
from unittest import TestCase, main as testmain
from song import Song, SongList
from files import create_json_file, read_json_file

C_ARTIST = 'Charlie laagherrie & mentale theo'
C_TITLE = 'Wonderfull days'
C_ALBUM = 'Charlottenburg'
C_YEAR = 1995
C_FILENAME = 'test_songs.json'
C_JSON = '''{
            "title": "Live at london",
            "artist": "Charlie lownoise & menthal theo",
            "year": 1996,
            "album": "Live in london remasterd",
            "played": 0
        }'''

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song.createWithProperties(C_TITLE, C_ARTIST, C_YEAR, C_ALBUM)

    def test_title(self):
        self.assertEqual(self.song.title, C_TITLE)

    def test_artist(self):
        self.assertEqual(self.song.artist, C_ARTIST)
        
    def test_album(self):
        self.assertEqual(self.song.album, C_ALBUM)
        
    def test_year(self):
        self.assertEqual(self.song.year, C_YEAR)

    def test__str__(self):
        self.assertTrue(str(C_YEAR) in str(self.song))
        self.assertTrue(C_ARTIST in str(self.song))
        self.assertTrue(C_ALBUM in str(self.song))
        self.assertTrue(C_TITLE in str(self.song))

        newsong = Song()
        self.assertNotIn(str(C_YEAR), str(newsong))
        self.assertNotIn(C_ARTIST, str(newsong))
        self.assertNotIn(C_ALBUM, str(newsong))
        self.assertNotIn(C_TITLE, str(newsong))
        self.assertIn('unknown', str(newsong))

    def test_json(self):
        self.song.as_json = C_JSON
        self.assertIn('lownoise', str(self.song))

    def test_play(self):
        self.assertEqual(self.song.played, 0)
        self.song.play()
        self.assertEqual(self.song.played, 1)        




class TestSongList(TestCase):
    def test_items(self):
        self.songs = SongList(C_FILENAME)
        self.songs.items.append(Song.createWithProperties(C_TITLE, C_ARTIST, C_YEAR, C_ALBUM))
        self.songs.save()        
        
        self.assertTrue(os.path.exists(self.songs.filename))
        content = read_json_file(self.songs.filename)
        self.assertIn(str(C_YEAR), content)
        self.assertIn(C_ARTIST, content)
        self.assertIn(C_ALBUM, content)
        self.assertIn(C_TITLE, content)


        self.songs = SongList(C_FILENAME)
        self.songs.load()

        self.assertEqual(len(self.songs.items), 1)
        self.assertEqual(self.songs.items[0].title, C_TITLE)
        self.assertEqual(self.songs.items[0].artist, C_ARTIST)
        self.assertEqual(self.songs.items[0].year, C_YEAR)
        self.assertEqual(self.songs.items[0].album, C_ALBUM)
        
        

if __name__ == '__main__':
    testmain()   