from sqlalchemy import Column, Computed, Date, Integer, String,JSON,ForeignKey

import sys
sys.path.insert(0, '/home/maxim/Desktop/Fast_Api_lern')

from app.database import Base

class Users(Base):
    __tablename__='users'
    id = Column(Integer, primary_key = True, nullable=False)
    email = Column(String,nullable=False)
    hashed_password = Column(String, nullable=False)