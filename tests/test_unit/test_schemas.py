from app.schemas.user import UserCreate
from pydantic import ValidationError
import pytest
from app.schemas.user import UserRead

def test_user_create_valid():
    user = UserCreate(username="jason", email="jason@example.com", password="securepass")
    assert user.username == "jason"
    assert user.email == "jason@example.com"

def test_user_create_invalid_email():
    with pytest.raises(ValidationError):
        UserCreate(username="jason", email="invalid-email", password="securepass")

def test_user_read():
    user = UserRead(id=1, username="jason", email="jason@example.com", created_at="2024-01-01T00:00:00")
    assert user.id == 1
