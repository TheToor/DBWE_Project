from sqlalchemy import Column, ForeignKey, Integer, Table
from app.db.db import db

school_teachers = Table('teachers_schools',
    db.Model.metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=False),
    Column('school_id', Integer, ForeignKey('school.id'), primary_key=False)
)