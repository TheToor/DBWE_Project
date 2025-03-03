from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped
from app.db.db import db

class SchoolRating(db.Model):
    __tablename__ = "school_rating"

    id: Mapped[int] = Column(Integer, primary_key=True)
    rating: Mapped[int] = Column(Float)
    comment: Mapped[str] = Column(String(256))
    
    user_id: Mapped[int] = Column(Integer, ForeignKey('user.id'))
    school_id: Mapped[int] = Column(Integer, ForeignKey('school.id'))

    user = db.relationship("User", backref='school_ratings')
    school = db.relationship("School", backref='ratings')