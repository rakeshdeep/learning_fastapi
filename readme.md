<h1 align="center">FastAPI</h1>

## Here is a simple fastapi with `get` `post` `put` `delete` method

- This API only work in your local machine 
- only for Mysql database
- some error occuring at `put` method

**for runnig this fastapi in your system**
 - you need to have mysql in your system
 - some library and classes
    - `fastapi` , `sqlalchemy`, `pymysql`


### Here is the error code of `put`

The error part is commented in `main.py` from line 52 to 67

```
@app.put("/users/{user_id}", response_model=userSchema)
def update_user(user_id:int, user: userSchema, db:Session = Depends(get_db)):

    try:
        u=db.query(User).filter(User.id == user_id).first()
        if u:
            u.name = user.name
            u.email = user.email
            db.add(u)
            db.commit()
            return u
        else:
            raise HTTPException(status_code=404, detail="User not found")

    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))
```

### the main error showing at:
        u.name = user.name
        u.email = user.email

**There is a type error but i can't able to fix that.**