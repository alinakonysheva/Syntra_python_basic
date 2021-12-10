from unittest import TestCase, main as testmain
from movie import Movie, MovieList
import os
from files import read_json_file

C_NAME = 'Grease'
C_YEAR = 1978
C_DESC = "Good girl Sandy Olsson and greaser Danny Zuko fell in love over the summer. When they unexpectedly discover they're now in the same high school, will they be able to rekindle their romance?"
C_SCORE = 9.0
C_FILENAME = 'test_movies.json'


class TestMovie(TestCase):

    def setUp(self):
        self.movie = Movie(C_NAME, C_DESC, C_YEAR, C_SCORE)

    def test_name(self):
        self.assertEqual(self.movie.name, C_NAME)
        newname = 'testmovie'
        self.movie.name = newname
        self.assertEqual(self.movie.name, newname)


    def test_score(self):
        self.assertEqual(self.movie.score, C_SCORE)
        newscore = 0.1
        self.movie.score = newscore
        self.assertEqual(self.movie.score, newscore)
        
    
    def test_description(self):
        self.assertEqual(self.movie.description, C_DESC)
        newdesc = 'test description'
        self.movie.description = newdesc
        self.assertEqual(self.movie.description, newdesc)
    

    def test_year(self):
        self.assertEqual(self.movie.year, C_YEAR)
        year = 2000
        self.movie.year = year
        self.assertEqual(self.movie.year, year)
    
    def test__str__(self):
        self.assertTrue(str(C_YEAR) in str(self.movie))
        self.assertTrue(C_NAME in str(self.movie))
        self.assertTrue(str(C_SCORE) in str(self.movie))
        self.assertTrue(C_DESC[0:15] in str(self.movie))
        self.assertTrue('...' in str(self.movie))
        



class TestMovieList(TestCase):
    def test_items(self):
        self.movies = MovieList(C_FILENAME)
        self.movies.items.append(Movie(C_NAME, C_DESC, C_YEAR, C_SCORE))
        self.movies.save()        
        
        self.assertTrue(os.path.exists(self.movies.filename))
        content = read_json_file(self.movies.filename)
        self.assertIn(str(C_YEAR), content)
        self.assertIn(C_NAME, content)
        self.assertIn(str(C_SCORE), content)
        self.assertIn(C_DESC, content)


        self.movies = MovieList(C_FILENAME)
        self.movies.load()

        self.assertEqual(len(self.movies.items), 1)
        self.assertEqual(self.movies.items[0].name, C_NAME)
        self.assertEqual(self.movies.items[0].description, C_DESC)
        self.assertEqual(self.movies.items[0].year, C_YEAR)
        self.assertEqual(self.movies.items[0].score, C_SCORE)
        

        



if __name__ == '__main__':
    testmain()   