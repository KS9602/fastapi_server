from fastapi import FastAPI, Depends, Request
from requests import Request
from starlette.status import HTTP_201_CREATED

import tables
from schemas import PartyUserSchema, CreatePartyUser, Req
from database import get_db
from sqlalchemy.orm import Session
from tables import PartyUser
from router import router

app = FastAPI()
app.include_router(router)

@app.get('/all_users',response_model=list[PartyUserSchema])
def all_users(db: Session = Depends(get_db)):
    users = db.query(PartyUser).all()
    return users

@app.get('/get_user/{id}')
def get_user(id: str, db: Session = Depends(get_db)):
    user = db.query(PartyUser).where(PartyUser.id == id).first()
    return user

@app.post('/get_user_payload')
def add_user(request: PartyUserSchema,db: Session = Depends(get_db)):
    return db.query(PartyUser).where(PartyUser.id == request.id).first()


@app.post('/add_user',status_code=HTTP_201_CREATED)
def create_user(request: CreatePartyUser, db: Session = Depends(get_db)):
    fake_hashed_password = request.password + "notreallyhashed"
    db_user = PartyUser(username=request.username, password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {'db_user':"created"}
