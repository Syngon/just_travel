from datetime import datetime, timedelta
from jose import jwt

# CONFIG
SECRET_KEY = '1g42uig412uigui24g1ui4oj12h3o21jh'
ALGORITHM = 'HS256'
EXPIRES_IN_MIN = 30


def create_access_token(data_input: dict):
    data = data_input.copy()
    expire = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MIN)

    data.update({'expire_in': expire})

    token_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return token_jwt


def verify_access_token(token: str):
    data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return data.get('sub')
