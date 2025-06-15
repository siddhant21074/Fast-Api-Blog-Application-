from fastapi import FastAPI # type: ignore
from Blog.database import engine
from Blog import models
from Blog.router import blog,user,authentication

app = FastAPI()

models.Base.metadata.create_all(engine)
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

