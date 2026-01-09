from jose import jwt
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get SECRET_KEY from environment
SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
ALGORITHM = "HS256"


def create_dummy_token(user_id: str, expires_delta: timedelta = None):
    """Create a dummy JWT token for testing."""
    if expires_delta is None:
        expires_delta = timedelta(minutes=30)

    expire = datetime.now() + expires_delta
    to_encode = {"sub": user_id, "exp": expire.timestamp()}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def test_token_verification():
    """Test the token creation and verification process."""
    print("Testing JWT token creation and verification...")

    # Create a dummy token
    user_id = "test_user_123"
    token = create_dummy_token(user_id)
    print(f"Created token for user {user_id}: {token[:30]}...")

    # Verify the token by decoding it (simulating what auth.py does)
    try:
        from jose import jwt as jose_jwt
        payload = jose_jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        decoded_user_id = payload.get("sub")

        if decoded_user_id == user_id:
            print(f"SUCCESS: Token verification successful! User ID: {decoded_user_id}")
        else:
            print(f"ERROR: Token verification failed! Expected: {user_id}, Got: {decoded_user_id}")
            return False

    except jose_jwt.JWTError as e:
        print(f"ERROR: JWT Error during verification: {e}")
        return False

    # Test with an invalid token
    try:
        invalid_token = "invalid.token.here"
        jose_jwt.decode(invalid_token, SECRET_KEY, algorithms=[ALGORITHM])
        print("ERROR: Invalid token should have failed verification!")
        return False
    except jose_jwt.JWTError:
        print("SUCCESS: Invalid token correctly rejected")

    # Test with wrong secret
    try:
        wrong_secret = "wrong_secret"
        jose_jwt.decode(token, wrong_secret, algorithms=[ALGORITHM])
        print("ERROR: Token should have failed with wrong secret!")
        return False
    except jose_jwt.JWTError:
        print("SUCCESS: Token correctly rejected with wrong secret")

    print("All authentication tests passed! SUCCESS")
    return True


if __name__ == "__main__":
    test_token_verification()