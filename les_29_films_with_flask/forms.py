from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField


class MovieForm(FlaskForm):
    title = StringField('Title', name='movie_title')
    year = IntegerField('Year', name='movie_year')
    description = TextAreaField('Description', name='movie_description')
    submit = SubmitField('Bewaren')

