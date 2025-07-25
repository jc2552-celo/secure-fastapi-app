from app.utils.hashing import get_password_hash, verify_password

def test_password_hashing():
    raw_password = "securepassword123"
    hashed = get_password_hash(raw_password)
    
    assert hashed != raw_password
    assert verify_password(raw_password, hashed)
