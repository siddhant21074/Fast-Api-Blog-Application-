from fastapi import APIRouter,status,Response,Depends,HTTPException # type:ignore
from typing import List
from sqlalchemy.orm import Session
from Blog import schema,database,models
from  Blog.hashing import  Hash
router = APIRouter(
    prefix='/users',
    tags=['Users']
)
# Hashing the password



get_db = database.get_db
@router.post('/',response_model=schema.ShowUser)
def user(request:schema.User,db:Session = Depends(get_db)):
    hashed_password = Hash.hashing(request.password)
    new_user = models.User(name=request.name,email=request.email,password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get('/',status_code=status.HTTP_200_OK,response_model=List[schema.ShowUser])
def get_users(response:Response,db:Session = Depends(get_db)):
    users = db.query(models.User).all()
    if not users:
        response.status_code = status.HTTP_404_NOT_FOUND  
    return users
