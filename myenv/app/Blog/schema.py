# Here the Pydantic models are called Schema in fast api 

from pydantic import BaseModel
 
class Blog(BaseModel):
    title:str
    body:str
    # id:int

# We are defining this ShowBlogs class to get only the required fiels in the response. This will show only the initialized values i.e title and body if we uncomment the id then it will be also shown

class ShowBlogs(Blog): # Here we are inheriting the Blog class 
    class Config():  # This help to prevent the 'internal server error' 
        orm_mode=True
          
class User(BaseModel):
    name:str
    email:str
    password:str
    
class ShowUser(BaseModel):
    name:str
    email:str
    
class Login(BaseModel):
    username:str
    password:str
    
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None