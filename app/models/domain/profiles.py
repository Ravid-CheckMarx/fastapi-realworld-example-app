from typing import Optional

from app.models.domain.rwmodel import RWModel


class Profile(RWModel):
    username: str
    bio: str = ""
    image: Optional[str] = None
    following: bool = False
    creditcard: str = "1234123412341234"
