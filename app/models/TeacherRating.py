from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped
from app.db.db import db

class TeacherRating(db.Model):
    __tablename__ = "teacher_rating"

    id: Mapped[int] = Column(Integer, primary_key=True)
    rating: Mapped[int] = Column(Float)
    comment: Mapped[str] = Column(String(256))
    
    user_id: Mapped[int] = Column(Integer, ForeignKey('user.id'))
    teacher_id: Mapped[int] = Column(Integer, ForeignKey('user.id'))
    school_id: Mapped[int] = Column(Integer, ForeignKey('school.id'))

    user = db.relationship("User", backref='teacher_ratings', foreign_keys=[user_id])
    teacher = db.relationship("User", backref='my_teacher_ratings', foreign_keys=[teacher_id])
    school = db.relationship("School", backref='teacher_ratings', foreign_keys=[school_id])