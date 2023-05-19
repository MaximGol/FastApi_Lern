from fastapi import APIRouter


from app.bookings.dao import BookingDAO
from app.bookings.shemas import SBoking

router = APIRouter(
    prefix = "/bookings",
    tags = ["Бронирования"],

)

@router.get("")
async def get_bookings()-> list[SBoking]:
    return await BookingDAO.find_all()
    
        
