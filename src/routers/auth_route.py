from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas.schemas import LoginSuccess, User, LoginData, SimpleUser
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositories.user_repository import UserRepository
from src.infra.providers import hash_provider, token_provider
from src.routers.auth_utils import get_logged_in_user

router = APIRouter()


@router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=User)
def signup(user: SimpleUser, session: Session = Depends(get_db)):
    # verificar se já existe um para o username
    find_user = UserRepository(session).get_user_by_name(user.username)

    if find_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists"
        )

    # criar novo usuario
    user.password = hash_provider.generate_hash(user.password)
    created_user = UserRepository(session).create(user)
    return created_user


@router.post("/token", response_model=LoginSuccess)
def login(login_data: LoginData, session: Session = Depends(get_db)):
    password = login_data.password
    username = login_data.username

    user = UserRepository(session).get_user_by_name(username)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Wrong data, please use the correct data!",
        )

    valid_password = hash_provider.verify_hash(password, user.password)
    if not valid_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Password is not valid!"
        )
    # Gerar Token JWT
    token = token_provider.create_access_token({"sub": user.username})
    del user.password

    return LoginSuccess(user=user, access_token=token)


@router.get("/me", response_model=User)
def me(user: User = Depends(get_logged_in_user)):
    return user
