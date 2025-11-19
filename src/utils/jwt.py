#tokeny tut delaesh

from datetime import datetime, timedelta
from jose import jwt, JWTError

def create_access_token(user_id: int) -> str:
    expire = datetime.utcnow() + timedelta(
        minutes=settings.access_token_expires_minutes
    )
    to_encode = {"sub": str(user_id), "exp": expire, "token_type": "access"}
    encoded_jwt = jwt.encode(
        to_encode, settings.secret_key, algorithm=settings.algorithm
    )
    return encoded_jwt


def create_refresh_token(user_id: int) -> str:
    expire = datetime.utcnow() + timedelta(days=settings.refresh_token_expires_days)
    to_encode = {"sub": str(user_id), "exp": expire, "token_type": "refresh"}
    encoded_jwt = jwt.encode(
        to_encode, settings.secret_key, algorithm=settings.algorithm
    )
    return encoded_jwt


def decode_token(token: str, expected_token_type: str):
    try:
        payload = jwt.decode(
            token, settings.secret_key, algorithms=[settings.algorithm]
        )
        token_type = payload.get("token_type")
        
        if token_type != expected_token_type:
            raise JWTError(f"Invalid token type: expected {expected_token_type}, got {token_type}")
        
        return payload.get("sub")
    except JWTError:
        return None