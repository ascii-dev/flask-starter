"""Module for base model"""

from datetime import datetime as dt

from ..database import db


class BaseModel(db.Model):
    """Class for base model attributes and method"""

    __abstract__ = True

    id = db.Column(db.String(36), primary_key=True)
    created_at = db.Column(db.DateTime, default=dt.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=dt.utcnow)
