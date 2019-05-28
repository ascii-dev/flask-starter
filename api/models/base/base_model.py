"""Module for base model"""

from datetime import datetime as dt

from ..database import db


class BaseModel(db.Model):  # pragma: no cover
    """Class for base model attributes and method"""

    __abstract__ = True

    id = db.Column(db.String(36), primary_key=True)
    created_at = db.Column(db.DateTime, default=dt.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=dt.utcnow)

    def save(self):
        """
        Saves a model instance
        :return: model instance
        """
        db.session.add(self)
        db.session.commit()

    def update(self, **kwargs):
        """
        Updates a mode instance
        :return: updated model instance
        """
        for field, value in kwargs.items():
            setattr(self, field, value)
            db.session.commit()

    def delete(self):
        """
        Deletes a database instance
        :return: None
        """
        db.session.delete(self)
        db.session.commit()
