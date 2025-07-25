from app.utils.hashing import get_password_hash, verify_password

def test_password_hashing():
    password = "securepass123"
    hashed = get_password_hash(password)
    assert verify_password(password, hashed)
    assert not verify_password("wrongpass", hashed)

