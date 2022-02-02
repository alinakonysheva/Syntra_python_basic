from flask import Flask, render_template, flash, redirect, url_for, abort, request
from consts import MESSAGES_OK, MESSAGES_ERROR, MESSAGES_WARNING
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from config import USER_NAME, PASSWORD, HOST, PORT, DB_NAME
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'lsdkfjsdlfkjsldkfj'
app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql+mysqlconnector://{USER_NAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'

db = SQLAlchemy(app)


class Music(db.Model):
    __tablename__ = 'T_MUSIC'

    id = Column('PK_ID', Integer, primary_key=True, index=True)
    title = Column('F_TITLE', String(255), nullable=False)
    artist = Column('F_ARTIST', String(255), nullable=False)
    year = Column('F_YEAR', Integer, nullable=False)

    def __str__(self):
        return '{} - {} - {} ({})'.format(self.id, self.artist, self.title, self.year)


class MusicForm(FlaskForm):
    title = StringField('Title', name='music_title')
    year = IntegerField('Year', name='music_year', render_kw={'class': 'form-control'})
    artist = StringField('Artist', name='music_artist', render_kw={'class': 'form-control'})
    genre = SelectField('Genre', name='music_genre',
                        choices=[('1', 'Happy Hardcore'), ('2', 'Trance'), ('3', 'Hardrock')])
    submit = SubmitField('Bewaren')


@app.route('/')
def do_home():
    return render_template('index_base.html')


@app.route('/music/<string:search>')
@app.route('/music', defaults={'search': ''})
def do_music_list(search):
    qry = db.session.query(Music)
    searchtext = search.strip().lower()
    if searchtext != '':
        if searchtext.isdigit():
            qry = qry.filter((Music.year == int(searchtext)) | (Music.id == int(searchtext)))
        else:
            searchtext = '%{}%'.format(searchtext)
            qry = qry.filter(Music.artist.ilike(searchtext) | Music.title.ilike(searchtext))

    music = qry.all()
    return render_template('music_list.html', music=music, searchtext=searchtext)


@app.route('/search', methods=['POST'])
def do_search():
    if request:
        search = request.form.get('search_music', '')

        if len(search) < 3 and not search.isdigit():
            flash('Zoek opdracht was te kort, gelieve minstens 3 karakters in te geven', MESSAGES_WARNING)
            return redirect(request.referrer)
        else:
            return redirect(url_for('do_music_list', search=search))
    else:
        return redirect(url_for('do_music_list'))


@app.errorhandler(404)
def do_not_found(error):
    return render_template('errors.html', code=404)


@app.errorhandler(403)
def do_not_authorised(error):
    return render_template('errors.html', code=403)


@app.errorhandler(500)
def do_server_error(error):
    return render_template('errors.html', code=500)


@app.route('/song/<int:song_id>', methods=['GET', 'POST'])
@app.route('/song/', defaults={'song_id': 0}, methods=['GET', 'POST'])
def do_song(song_id):
    try:
        form = MusicForm()

        if song_id == 0:
            song = Music()
        else:
            song = db.session.query(Music).get(song_id)

        if form.validate_on_submit():
            song.title = form.title.data
            song.year = form.year.data
            song.artist = form.artist.data
            db.session.add(song)
            db.session.commit()

            if song_id == 0:
                msg = 'Niew record bewaard'
            else:
                msg = 'Wijzigingen opgeslagen'

            flash(msg, MESSAGES_OK)

            return redirect(url_for('do_song', song_id=song.id))

        if song is None:
            flash('"{}" niet gevonden'.format(song_id), MESSAGES_ERROR)
            return redirect(url_for('do_music_list'))
        else:
            form.artist.data = song.artist
            form.title.data = song.title
            form.year.data = song.year
            form.genre.data = '2'

            return render_template('music_detail.html', song=song, form=form)
    except Exception as e:
        msg = 'Fout bij het opslagen'
        flash(msg, MESSAGES_ERROR)
        print('user.id - m')

    abort(404)


@app.route('/song-nowtf/<int:song_id>', methods=['GET', 'POST'])
@app.route('/song-nowtf/', defaults={'song_id': 0}, methods=['GET', 'POST'])
def do_song_nowtf(song_id):
    try:
        song = db.session.query(Music).get(song_id)

        if song_id == 0:
            song = Music()
        else:
            song = db.session.query(Music).get(song_id)

        if request.method == 'POST':
            song.artist = request.form.get('artistname', '')
            song.title = request.form.get('songtitle', '')
            song.year = request.form.get('songyear', '')
            db.session.add(song)
            db.session.commit()

            if song_id == 0:
                msg = 'Niew record bewaard'
            else:
                msg = 'Wijzigingen opgeslagen'

            flash(msg, MESSAGES_OK)
            return redirect(url_for('do_song_nowtf', song_id=song.id))

        if song is None:
            flash('"{}" niet gevonden'.format(song_id), MESSAGES_ERROR)
            return redirect(url_for('do_music_list'))
        else:
            return render_template('music_detail_nowtf.html', song=song)
    except Exception as e:
        msg = 'Fout bij het opslagen'
        flash(msg, MESSAGES_ERROR)
        print('user.id - m')

    abort(404)
