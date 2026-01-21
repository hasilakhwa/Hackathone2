from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Annotated
from jose import jwt, JWTError
from pydantic import ValidationError
from ..core.config import settings
from ..models.user import User
import os


security = HTTPBearer()


class JWTData:
    def __init__(self, user_id: int):
        self.user_id = user_id


def get_current_user_id(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],
) -> int:
    """
    Get current user ID from JWT token.

    This function validates the JWT token and extracts the user ID.
    It ensures that the user_id in the token matches the user_id in the URL path
    to prevent cross-user access.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            credentials.credentials,
            settings.BETTER_AUTH_SECRET,
            algorithms=[os.getenv("JWT_ALGORITHM", "HS256")]
        )
        user_id: int = payload.get("user_id")
        if user_id is None:
            raise credentials_exception
    except (JWTError, ValidationError):
        raise credentials_exception

    return user_id


def verify_user_id_match_path(path_user_id: int, current_user_id: int = Depends(get_current_user_id)) -> int:
    """
    Verify that the user_id in the path matches the user_id in the JWT token.

    This function ensures that users can only access their own resources.
    """
    if path_user_id != current_user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: Cannot access another user's resources"
        )
    return current_user_id