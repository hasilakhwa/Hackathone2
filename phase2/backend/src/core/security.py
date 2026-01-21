from datetime import datetime, timedelta
from typing import Optional
import jwt
from fastapi import HTTPException, status, Depends
from jwt.exceptions import InvalidTokenError
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from .config import settings

load_dotenv()

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: Optional[int] = None


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.BETTER_AUTH_SECRET, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, settings.BETTER_AUTH_SECRET, algorithms=[ALGORITHM])
        user_id: int = payload.get("user_id")
        if user_id is None:
            raise credentials_exception
        token_data = TokenData(user_id=user_id)
    except InvalidTokenError:
        raise credentials_exception
    return token_data


from fastapi import Request

def get_authorization_header(request: Request = None):
    """
    Extract the Authorization header value.
    This is a dependency that FastAPI will inject automatically.
    """
    if request is None:
        # This is a workaround to handle the dependency injection properly
        return None
    authorization = request.headers.get("Authorization")
    return authorization


def get_token_from_header(authorization: str = Depends(get_authorization_header)):
    if authorization is None or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = authorization[7:]  # Remove "Bearer " prefix
    return token


def get_current_user_from_token(token: str = Depends(get_token_from_header)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_data = verify_token(token, credentials_exception)
    # In a real application, you would fetch the user from the database
    # For now, we'll just return the user_id from the token
    return token_data.user_id