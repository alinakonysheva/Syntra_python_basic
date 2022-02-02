from main import db
from sqlalchemy import Column, Integer, String, Text


class Movie(db.Model):
    __tablename__ = 'T_MOVIE'

    id = Column('PK_ID', Integer, primary_key=True)
    title = Column('F_TITLE', String(200), nullable=False)
    year = Column('F_YEAR', Integer, nullable=False)
    description = Column('F_TEXT', Text)

    def __str__(self):
        return '{} - {} ({})'.format(self.id, self.title, self.year)