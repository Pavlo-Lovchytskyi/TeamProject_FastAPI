from pydantic import BaseModel
from pydantic import BaseModel, EmailStr, Field
from datetime import date, datetime


class CommentRequest(BaseModel):
    description: str


class CommentResponce(BaseModel):
    id: int
    user_id: int
    description: str

class Admin(BaseModel):
    id: int
    role: str


class ShareRequest(BaseModel):
    description: str = Field(min_length=2, max_length=50)


class ShareResponce(BaseModel):
    id: int
    image: str
    qrcode: str
    description: str = Field(min_length=2, max_length=50)
    comment: str
    tags: list
    created_at: datetime
    updated_at: datetime


class UserModel(BaseModel):
    username: str = Field(min_length=5, max_length=16)
    email: str
    password: str = Field(min_length=6, max_length=10)



class UserDb(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime
    avatar: str

    class Config:
        from_attributes = True


class UserResponse(BaseModel):
    user: UserDb
    detail: str = "User successfully created"


class TokenModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class RequestEmail(BaseModel):
    email: EmailStr
    

class TagRequest(BaseModel):
    name: str


class TagResponce(BaseModel):
    id: int
    share_id: int
