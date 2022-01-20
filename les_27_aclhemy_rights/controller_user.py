from user import User
from database import session


class ContrillerUser():
    @staticmethod
    def add_user(email, fullname):
        u = User()
        u.email = email
        u.fullname = fullname

        session.add(u)
        session.commit()

    def unique_email(self, email):
        email = email.strip().lower()
        result = session.query(User).filter(User.email == email).all()
        return self.email.lower()

