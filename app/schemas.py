from pydantic import BaseModel, EmailStr

class WarriorCreate(BaseModel):
    name: str
    skill: str

class WarriorOut(WarriorCreate):
    id: int

    model_config = {
        "from_attributes": True
    }
# 👤 Input for registration
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# 👤 Output after registration
class UserOut(BaseModel):
    id: int
    email: EmailStr

    model_config = {
        "from_attributes": True
    }
#  Token Response
class Token(BaseModel):
    access_token: str
    token_type: str
