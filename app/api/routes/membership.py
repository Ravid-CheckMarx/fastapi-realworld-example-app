from fastapi import APIRouter, Body, Depends, HTTPException
from pydantic import BaseModel
from starlette.status import HTTP_400_BAD_REQUEST

from app.api.dependencies.authentication import get_current_user_authorizer
from app.api.dependencies.database import get_repository
from app.core.config import get_app_settings
from app.core.settings.app import AppSettings
from app.db.repositories.users import UsersRepository
from app.models.domain.users import User
from app.models.schemas.users import UserInResponse, UserInUpdate, UserWithToken
from app.resources import strings
from app.services import jwt
from app.services.authentication import check_email_is_taken, check_username_is_taken

router = APIRouter()


class Member(BaseModel):
    number: str
    cvc: str
    expiry: str
    name: str


@router.post("")
async def member(
        member: Member,
        user: User = Depends(get_current_user_authorizer()),

):
    print(member)
    if (
    member.number == '4426111122223333' and
    member.cvc == '555' and
    member.name == 'Team Rocket' and
    member.expiry == '0922'
    ):
        return "flag{2_much_1nf0_Xp0seD}"
    else:
        return "Card declined, try again!"
