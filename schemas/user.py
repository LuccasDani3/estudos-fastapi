from pydantic import BaseModel, EmailStr, Field, field_validator

class UserCreate(BaseModel):
    name: str = Field(min_length=3)
    email: EmailStr
    age: int

    @field_validator("age")
    @classmethod
    def validate_age(cls, age: int):
        if age <= 18:
            raise ValueError("O usuário deve ser maior de idade")
        return age