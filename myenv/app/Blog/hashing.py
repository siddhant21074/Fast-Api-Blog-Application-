from passlib.context import CryptContext #type:ignore
pwd_cxt = CryptContext(schemes=["bcrypt"],deprecated="auto")   

class Hash():
    def hashing(password:str):
        hashed_password = pwd_cxt.hash(password)
        return hashed_password
    
    def verify(hashed_password,plain_password):
        return pwd_cxt.verify(plain_password,hashed_password)