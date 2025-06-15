from fastapi import APIRouter,status,Response,Depends,HTTPException # type:ignore
from typing import List
from sqlalchemy.orm import Session
from passlib.context import CryptContext #type:ignore
from  Blog.oauth2 import get_current_user
from Blog import schema,database,models

router = APIRouter(
    prefix='/blogs',
    tags=['Blogs']
)

get_db = database.get_db


# Hashing the password

pwd_cxt = CryptContext(schemes=["bcrypt"],deprecated="auto")


# Get all the data from the database 
@router.get('/',status_code=status.HTTP_200_OK,response_model=List[schema.ShowBlogs])
def get_blog(response:Response,db:Session = Depends(get_db),current_user:schema.User=Depends(get_current_user)):
    blogs = db.query(models.Blog).all()
    if not blogs:
        response.status_code = status.HTTP_404_NOT_FOUND  
    return blogs

# Creating the new data and inserting into database 
@router.post("/",status_code=status.HTTP_201_CREATED)
def create(request:schema.Blog,db:Session = Depends(get_db),current_user:schema.User=Depends(get_current_user)):
    new_blog = models.Blog(title=request.title,body=request.body)
    db.add(new_blog)    
    db.commit()
    db.refresh(new_blog)
    return new_blog

# Get the particular data from the database using id
# response_model will fetch the data fields from the ShowBlogs class and show in response
@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=schema.ShowBlogs) 
def get_blog_by_id(response:Response,id:int,db:Session = Depends(get_db),current_user:schema.User=Depends(get_current_user)):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        # response.status_code = status.HTTP_404_NOT_FOUND 
        # return 'Data Not Available' 
        # OR
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Data Not Available")
    
    return blogs

# Deleting the particular record
@router.delete('/',status_code=status.HTTP_204_NO_CONTENT)
def delete_data(id:int,db:Session = Depends(get_db),current_user:schema.User=Depends(get_current_user)):
    data = db.query(models.Blog).filter(models.Blog.id == id)
    if not data.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Data Not Available")
   
    data.delete(synchronize_session=False)
    db.commit()
    return 'Record Deleted'
    

# Update the data from the database 
@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update_data(id:int,request:schema.Blog,db:Session = Depends(get_db),current_user:schema.User=Depends(get_current_user)):
    data = db.query(models.Blog).filter(models.Blog.id == id)
    if not data.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Data Not Available")
   
    data.update(request.dict())
    db.commit()
    return 'Record Updated '


