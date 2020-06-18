import datetime

from passlib.context import CryptContext
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token
)
from flask import current_app as app

from app import db
from app.models.VerificationCode import VerificationCode


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Integer, nullable=False, default=1)
    is_verified = db.Column(db.Integer, nullable=False, default=0)
    last_logged_in = db.Column(db.DateTime, default=datetime.datetime.now())
    created_at = db.Column(db.DateTime, default=datetime.datetime.now(), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())

    def __init__(self, email, password):
        self.email = email
        self._hash_password(password)

    def save(self):
        """ Shorthand method to update User object """
        db.session.add(self)
        db.session.commit()
