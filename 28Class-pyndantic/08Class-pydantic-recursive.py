"""
In Pydantic, a recursive (or self-referencing) model is a model that includes references to its own type within its field definitions. 
This is common when modeling hierarchical or nested data structures, such as:

Tree nodes (e.g., binary trees, organization charts)

File systems (folders containing subfolders and files)

Nested comment threads or categories with subcategories
"""

from typing import List, Optional, Union
from pydantic import BaseModel

class Comment(BaseModel):
    id:int
    content:str
    replies:Optional[List['Comment']] = None

Comment.model_rebuild()

c1 = Comment(
    id = 1,
    content='iphone',
    replies=[
        Comment(id=2, content='iphone2'),
        Comment(id=3, content='iphone3', replies=[
            Comment(id=4, content="something")
        ])
    ]
)

print(c1)

#Advanced Nested Model
#Optional Nested Model

class Address(BaseModel):
    id:int
    street:str
    pincode:Optional[int] = None

class Employee(BaseModel):
    name:str
    department:str
    address:Optional[Address] = None

class Company(BaseModel):
    c_name:str
    employee:List[Company]

# another way of writing pydantics
# Mixed Nested Models

class TextContet(BaseModel):
    type:str = 'Text'
    content: str

class ImageContent(BaseModel):
    type:str = 'Image'
    url:str
    alt_text:str

class Article(BaseModel):
    title:str
    sections:List[Union[TextContet, ImageContent]]

# Deeply Nested Model

# Level 1: Deepest layer
class Country(BaseModel):
    name:str
# Level 2: Middle Layer
class City(BaseModel):
    name: str
    country: Country

# Level 3: Top layer
class User(BaseModel):
    name: str
    city: City