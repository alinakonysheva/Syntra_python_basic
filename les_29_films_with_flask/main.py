from flask import Flask, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from config import DB_USER, DB_PORT, DB_NAME, DB_PASS, DB_HOST

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
    DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME
)
app.config['SECRET_KEY'] = 'MijnGeheim!!'

db = SQLAlchemy(app)

'''
def do_create():
    from movie import Movie
    db.drop_all()
    db.create_all()
'''


@app.route("/")
def do_home():
    # do_create()
    return render_template('home.html')


@app.route('/movies', methods=['GET'])
def do_movie_list():
    try:
        from movie import Movie
        movies = db.session.query(Movie).all()
        return render_template('movie_list.html', movies=movies)
    except Exception as e:
        print('fout: {}'.format(e))
    
    abort(404)


@app.route('/movie/<int:movieid>', methods=['GET', 'POST'])
@app.route('/movie/', defaults={'movieid': 0}, methods=['GET', 'POST'])
def do_movie_detail(movieid):
    try:
        from movie import Movie
        from forms import MovieForm

        movie_form = MovieForm()

        if movieid == 0:
            movie = Movie()
        else:
            movie = db.session.query(Movie).get(movieid)
        
        if movie is not None:
            if movie_form.validate_on_submit():
                movie.title = movie_form.title.data
                movie.year = int(movie_form.year.data) 
                movie.description = movie_form.description.data
                db.session.add(movie)
                db.session.commit() 
            
            movie_form.title.data = movie.title
            movie_form.year.data = movie.year
            movie_form.description.data = movie.description
            
            return render_template('movie_detail.html', form=movie_form, movie=movie)



    except Exception as e:
        print('do_movie_detail: {}'.format(e))

    abort(404)