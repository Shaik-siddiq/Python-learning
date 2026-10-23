from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

"""
In Pydantic (specifically V2), serialization (or dumping) is the process of converting a validated Python model instance back into raw Python data types (like dict) or standard transport formats (like JSON strings).

While validation moves data in (raw data ➔ validated model), serialization moves data out (validated model ➔ raw data / JSON).

Core Serialization Methods
Pydantic V2 provides two primary methods for exporting model data:
"""
"""
1. .model_dump() ➔ Python Dictionary
Converts the model and any nested models into standard Python dictionaries, lists, and primitives.
"""
class Address(BaseModel):
    street:str
    city:str
    zip_code:str

class User(BaseModel):
    id:int
    address:Address
    name:str
    email:str
    is_active:bool=True
    createdAt:datetime
    tags:List[str] = []

    model_config= ConfigDict(
        json_encoders ={datetime: lambda v:v.strftime('%d-%m-%Y %H:%M:$S')}
    )

user1 = User(
    id=1,
    address= Address(
        street="abc road",
        city = "somewhere",
        zip_code='001010'
    ),
    name = 'sid',
    email = 'sid@gmail.com',
    is_active = True,
    createdAt = datetime(2026, 10, 5, 9, 0),
    tags = ["premium", "channel owner"]
)
python_dict = user1.model_dump()
print('='*30)
print(user1)
print('='*30)
print(python_dict)

json_str = user1.model_dump_json()
print('='*30)
print(json_str)