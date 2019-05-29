from sqlalchemy.event import listens_for
from werkzeug.security import generate_password_hash
from .database import db
from ..utilities.enums import UserRoleEnum
from .base.base_model import BaseModel


class User(BaseModel):
    """Class for user's model"""

    __tablename__ = 'users'

    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    role = db.Column(db.Enum(UserRoleEnum), nullable=False, default='user')
    passport_photograph = db.Column(db.String)

    def __repr__(self):
        return f'<User {self.first_name} {self.last_name}>'


@listens_for(User, 'before_insert')
def hash_password(mapper, connect, target):
    """
    Hash the password before saving it into the DB
    :param mapper:
    :param connect:
    :param target:
    :return: None
    """
    target.password = generate_password_hash(
        target.password, method='pbkdf2:sha256')
