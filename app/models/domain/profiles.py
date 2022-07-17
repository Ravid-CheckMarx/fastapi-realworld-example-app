from typing import Optional

from app.models.domain.rwmodel import RWModel


class Profile(RWModel):
    admin: bool = False
    username: str
    bio: str = ""
    image: Optional[str] = None
    following: bool = False
    creditcard: str = "2222111199996666"
