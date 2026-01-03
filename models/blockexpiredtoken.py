from db import db

class BlockedTokenModel(db.Model):
    __tablename__ = "blocked_tokens"

    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False, unique=True)