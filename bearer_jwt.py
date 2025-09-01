from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException
from user_jwt import validate_token

class BearerJWT(HTTPBearer):
    
    async def __call__(self,request: Request):
        auth = await super().__call__(request)
        data =  validate_token(auth.credentials)
        if data["email"] != "ya@123" :
            raise HTTPException(status_code=403, credentials= "Email Incorrect")
       
