from typing import List
from flask_login import UserMixin
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from app.db.db import db
from app.models.SchoolTeachers import school_teachers

class User(db.Model, UserMixin):
    __tablename__ = "user"

    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str] = Column(String(256))
    email: Mapped[str] = Column(String(256), unique=True)
    password: Mapped[str] = Column(String(60))
    is_active: Mapped[bool] = Column(Boolean(), default=True)

    is_teacher: Mapped[bool] = Column(Boolean(), default=False)
    schools = relationship("School", secondary=school_teachers, back_populates="teachers")

    calculated_rating = None

    def get_id(self):
        return self.id
    
    def calculate_rating(self):
        if self.calculated_rating is not None:
            return self.calculated_rating
        
        if len(self.my_teacher_ratings) == 0:
            return "N/A"
        
        self.calculated_rating = sum([rating.rating for rating in self.my_teacher_ratings]) / len(self.my_teacher_ratings)
        return self.calculated_rating