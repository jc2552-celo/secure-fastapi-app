from app.core.security import get_password_hash, verify_password

def test_password_hash_and_verify():
    raw_password = "supersecret"
    hashed_password = get_password_hash(raw_password)
    assert hashed_password != raw_password
    assert verify_password(raw_password, hashed_password)
