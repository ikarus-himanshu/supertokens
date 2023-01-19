from pydantic import BaseModel
class changepassword(BaseModel):
    oldPassword:str
    newPassword:str