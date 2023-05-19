from fastapi import FastAPI, Query, Depends
from typing import Optional 
from datetime import date
from pydantic import BaseModel

import sys

from app.bookings.router import router as router_bookings


app = FastAPI()

app.include_router(router_bookings)


class HotelSearchArgs:
    def __init__(self,location, date_from, date_to, stars, has_spa) -> None:
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.stars = stars
        self.has_spa = has_spa


class SHotel(BaseModel):
    address:str
    name:str
    stars:int


@app.get("/hotels/")
def get_hotels(
    search_args: HotelSearchArgs = Depends()
):  
    pass
    #return search_args

class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post("/bookings")#, response_model= SHotel)
def add_booking(
    booking:SBooking
    ) -> str:
    pass

 