from sqlalchemy import Column, ForeignKey, Integer, String,JSON

import sys
sys.path.insert(0, '/home/maxim/Desktop/Fast_Api_lern')

from app.database import Base

class Hotels(Base):
    __tablename__='hotels'
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False)
    location = Column(String, nullable = False)
    services = Column(JSON)
    room_quantity = Column(Integer, nullable = False)
    image_id  = Column(Integer)

class Rooms(Base):
    __tablename__='rooms'
    id = Column(Integer, primary_key = True, nullable=False)
    
    hotel_id = Column(ForeignKey("hotels.id"), nullable=False)
    name = Column(String,nullable=False)
    description = Column(String, nullable=True)
    price = Column(Integer, nullable=False)
    services = Column(JSON,nullable=True)
    quantity = Column(Integer,nullable=False)
    image_id = Column(Integer)


'''
INSERT INTO hotels (name, location, services, room_quantity, image_id) VALUES
('Cosmos','Республика Алтай', '["Wi-Fi", "Парковка"]',1,1)

INSERT INTO rooms (hotel_id, name, price, quantity, services, image_id) VALUES
(1, 'Улучшенный с террасой и видом на озеро', 24500, 5, '["Бесплатный Wi-Fi","Кондиционер"]', 2)
'''