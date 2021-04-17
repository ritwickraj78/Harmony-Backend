from datetime import datetime

from harmony import db, app


class UserAccount(db.Model):
    __tablename__ = "user_account"

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    modified = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    public_id = db.Column(db.String(256), unique=True)
    f_name = db.Column(db.String(50))
    email = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(256))
    bio = db.Column(db.String)
    birth_date = db.Column(db.DateTime)
    job = db.Column(db.String)
    preference_id = db.Column(db.Integer, db.ForeignKey('user_preference.id', ondelete='SET NULL'))
    sexual_orientation_id = db.Column(db.Integer, db.ForeignKey('sexual_orientation.id', ondelete='SET NULL'))


class UserPreference(db.Model):
    __tablename__ = "user_preference"

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    modified = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    age_min = db.Column(db.Integer)
    age_max = db.Column(db.Integer)
    interested_gender = db.Column(db.String)


class SexualOrientation(db.Model):
    __tablename__ = "sexual_orientation"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
