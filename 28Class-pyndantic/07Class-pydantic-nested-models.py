"""
In Pydantic (v2), nested models allow you to define complex,
 hierarchical data structures by using one BaseModel class as a type hint inside another. 
 Pydantic automatically validates, casts, and serializes each level of the hierarchy.
"""

from typing import List
from pydantic import BaseModel

# To nest models, define the child model first and reference it as a type annotation in the parent model: Address is child model 
class Address(BaseModel):
    house_no:str
    street:str
    postal_address:int

class User(BaseModel):
    id:str
    name:str
    address:Address

class Hacker(BaseModel):
    id:str
    name:str
    address:List[Address]

ad1 = Address(
    house_no='143a',
    street= 'viddela',
    postal_address = 515008
)

user1 = User(
    id='21O',
    name='ned',
    address= ad1
)
print(user1)
print(user1.address.street)

h1 = Hacker(
    id='31f',
    name='divl',
    address=[ad1]

)
print(h1)
print(h1.address[0].house_no)