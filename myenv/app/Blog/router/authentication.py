from datetime import timedelta
from fastapi import APIRouter, status, Depends, HTTPException # type: ignore
from fastapi.security import OAuth2PasswordRequestForm # type: ignore
from sqlalchemy.orm import Session
from Blog import jwt_token, models, database
from Blog.hashing import Hash

get_db = database.get_db

router = APIRouter(tags=['Login'])

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user_data = db.query(models.User).filter(models.User.name == request.username).first()
    
    if not user_data or not Hash.verify(user_data.password, request.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    access_token = jwt_token.create_access_token(
        data={"sub": user_data.email},  # or user_data.id if you prefer
        expires_delta=timedelta(minutes=30)
    )

    return {"access_token": access_token, "token_type": "bearer"}
