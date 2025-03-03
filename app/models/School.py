from dataclasses import dataclass
from typing import List
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from app.db.db import db
from app.models.SchoolTeachers import school_teachers

@dataclass
class School(db.Model):
    __tablename__ = "school"

    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str] = Column(String(256))
    address: Mapped[str] = Column(String(256))
    phone: Mapped[str] = Column(String(256))
    email: Mapped[str] = Column(String(256))
    website: Mapped[str] = Column(String(256))

    calculated_rating = None

    teachers = relationship("User", secondary=school_teachers, back_populates="schools")
    
    def calculate_rating(self):
        if self.calculated_rating is not None:
            return self.calculated_rating
        
        if len(self.ratings) == 0:
            return "N/A"
        
        self.calculated_rating = sum([rating.rating for rating in self.ratings]) / len(self.ratings)
        return self.calculate_rating