
import os
import sys
from os.path import dirname,abspath 
sys.path.insert(0,dirname(dirname(abspath(__file__))))
sys.path.insert(0, '/home/maxim/Desktop/Fast_Api_lern')
print(234923)
from app.database import Base, DATABASE_URL

from app.hotels.models import Hotels 


a = [1,2,3]
print((*a,))
print (tuple(a))