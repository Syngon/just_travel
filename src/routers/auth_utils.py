from src.infra.sqlalchemy.repositories.user_repository import UserRepository
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from starlette import status
from src.infra.sqlalchemy.config.database import get_db
from src.infra.providers import token_provider
from jose import JWTError


oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')


def get_logged_in_user(token: str = Depends(oauth2_schema),
                         session: Session = Depends(get_db)):
    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid Token')

    try:
        username = token_provider.verify_access_token(token)
    except JWTError:
        raise exception

    if not username:
        raise exception

    user = UserRepository(session).get_user_by_id(username)

    if not user:
        raise exception

    return user
