from database import Base, sessionLocal, Engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends , HTTPException
from fastapi.responses import JSONResponse 
from pydantic import BaseModel

app = FastAPI()


class User(Base): #Model
    __tablename__ ="users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(60))
    password = Column(String(30), unique=True)

Base.metadata.create_all(bind = Engine)

class userSchema(BaseModel): #Schema 
    name:str
    email:str
    class config:
        orm_model = True

class userCreateSchema(userSchema):
    password:str
    


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

# create decorative for POST
@app.post("/users")
async def send_user(users:userCreateSchema, db:Session = Depends(get_db)):
    data = User( name = users.name, email = users.email, password = users.password)
    db.add(data)
    db.commit()
    return "done"
# create decorative for GET
@app.get("/user", description="getting user data", response_model=list[userSchema])
async def get_user(db:Session = Depends(get_db)):
    return db.query(User).all()



# @app.put("/users/{user_id}", response_model=userSchema)
# def update_user(user_id:int, user: userSchema, db:Session = Depends(get_db)):

#     try:
#         u=db.query(User).filter(User.id == user_id).first()
#         if u:
#             u.name = user.name
#             u.email = user.email
#             db.add(u)
#             db.commit()
#             return u
#         else:
#             raise HTTPException(status_code=404, detail="User not found")

#     except Exception as e:
#         return HTTPException(status_code=500, detail=str(e))



    
@app.delete("/user/{user_id}", response_class=JSONResponse)
def delete_user(user_id:int, db:Session = Depends(get_db)):
    try:
        u = db.query(User).filter(User.id == user_id).first()
        db.delete(u)
        db.commit()
        return {f"user of id {user_id} has been deleted"}
    except:
        return HTTPException(status_code=404, detail= "User not found")
