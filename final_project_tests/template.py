from sqlalchemy.ext.hybrid import hybrid_property

from database import BaseObj
from sqlalchemy import Column, String


class Template(BaseObj):
    __tablename__ = 'T_TEMPLATE'

    _name = Column('F_NAME', String(200))
    _content = Column('F_CONTENT', String(400))

    @hybrid_property
    def name(self):
        return str(self._name).lower()

    @name.setter
    def name(self, value):
        v = value.strip()
        if len(v) <= 5:
            raise ValueError('too small')
        self._name = v

    @hybrid_property
    def content(self):
        return str(self._content)

    @content.setter
    def content(self, value):
        v = value.strip()
        if len(v) >= 400:
            raise ValueError('text is too long')
        self._content = v

    @property
    def __str__(self) -> str:
        return f'{self.id} - {self._name} '
