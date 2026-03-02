#This file shows how to use Pydantic
#Pydantic is a data validation Library in python, it helps to get:
#IDE type hints, Data validation, JSON serialization
#after installation of the library Pydantic
#creaing a Pydantic model
#installed pydantic
# and now doing the import of the class BaseModel from the library Pydantic
from pydantic import BaseModel
class User(BaseModel):
    name : str
    email : str
    account_id : int
#creating an instance of the model by "unpacking dictionary"
user = User(
    name = "Manar",
    email = "manardg09@gmail.com",
    account_id = 12345
)
print(user)
#another way to create an instance
user_data = {
    'name': 'Manar',
    'email': 'manardg09@gmail.com'
    'account_id': 12345
}
user = User(**user_data)
print(user)
#or
print(user.name)
print(user.email)
print(user.account_id)
#validating data with pydantic
from pydantic import BaseModel
#creating a user with account_id that is not type int ==> validation error
class User(BaseModel):
    name: str
    email: str
    account_id: int
user = User(name = 'Ali', email = 'ali@gmailcom', account_id = 'hello')
print(user)
from pydantic import BaseModel, EmailStr
#validating through the class EmailStr ==> validation error
class User(BaseModel):
    name: str
    email: EmailStr
    account_id: int
user = User(name = 'Ali', email = 'ali', account_id = 1234)
print(user)
#custom field validation
#when we want to enforce a condition
@field_validator("account_id")
def validate_account_id(cls, value):
    if value <= 0:
        raise ValueError(f"account_id must be positive: {value}")
    return value
user = User(name = 'Ali', email = 'ali', account_id = -12)
print(user) #validation error appears
#JSON serialization: pydantic provides built-in support for JSON serialization,
#makes it easy to convert pydantic models to a JSON form
user_json_str = user.model_dump_json()
# this will return a JSON string representation of the model's data
print(user_json_str)
#execution gonna be like this:
{"name": "Ali, "email": "ali@gmail.com", "account_id": 1234}
#in case we just want a plain python dict objct instead
#use model_dum method
user_json_obj = user.model_dump()
#if we want to convert it back to Pydantic we use the meyhod parse_raw()
json_str = {"name": "Ali, "email": "ali@gmail.com", "account_id": 1234}
user = user.parse_raw(json_str)*
#pydantic vs dataclasses
#dataclass is an inbuilt model that lets us create class fields
from dataclasses import dataclass
#its very similar to Pydantic but we use it intead of extending BaseModel we use dataclass decorator intstead
@dataclass
class User:
    name: str
    email: str
    account_id: int


