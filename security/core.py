from passlib.context import CryptContext

passw_context = CryptContext(schemes=['bcrypt'],deprecated='auto')

def define_password_hash(password: str) -> str:
    return passw_context.hash(password)

def verify_password_hash(str_password: str, hashed_password: str) -> bool:
    return passw_context.verify(str_password,hashed_password)