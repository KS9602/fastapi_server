from pydantic import BaseModel
from typing import Optional


class Req(BaseModel):
    id: int

class PartyUserBase(BaseModel):
    username: str
    email: Optional[str]


class CreatePartyUser(PartyUserBase):
    username: str
    password: str
    email: Optional[str] = None

class PartyUserSchema(PartyUserBase):
    id: int


# TODO ArjanCodes zrobil dla kazdej operacji oddzielny BaseModel, nic nie bylo dziedziczone po sobie
# TODO wydaje sie to sensowniejsze niz to dziedziczenie ktore aby przeszkadza, jak chce dwie dane zuplenie inne to w rejestracji
# TODO to moge to zrobic