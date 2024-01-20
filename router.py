from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas import PartyUserSchema
from tables import PartyUser

router = APIRouter()

@router.get('/router',response_model=list[PartyUserSchema])
def router_get(db: Session = Depends(get_db)):
    users = db.query(PartyUser).all()
    return users
