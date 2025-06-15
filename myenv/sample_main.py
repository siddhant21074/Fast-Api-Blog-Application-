# from fastapi import FastAPI
# from pydantic import BaseModel
# import uvicorn

# app = FastAPI()

# @app.get("/")
# def home():
#     return {'Home page'}

# @app.get('/index/{id}/{val}')

# def index(id : int,fix:int=10,val:bool = False):
    
#     if val == True:
#         return {"id":id}
    
#     else:
#         return "none"
    
    
# class Blog(BaseModel):
#     title : str
#     blog_body : str
#     blog_bool : bool 
    
# @app.post("/blog")
# def blog(request: Blog):
#     return {"blog":{f'blog is created with {request.title}'}}



# # if __name__ == "__main__":
# #     uvicorn.run(app,host="127.0.0.1",port=9090)