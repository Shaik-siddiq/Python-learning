from pydantic import BaseModel
from typing import List, Dict, Optional

class Product(BaseModel):
    id:int
    name:str
    price:float
    in_stock:bool
    is_listing:bool=True  # In Pydantic (and standard Python), this is called a Field with a Default Value (or simply an optional field / default argument).
"""
Key Takeaway: Any field without a default value is considered required. 
Assigning a default value makes the field optional at instantiation time.
"""

prod_1 = Product(id=12, name='phone', price=22.34, in_stock=True, is_listing=False)
prod_2 = Product(id=1, name='cooler', price=12.12, in_stock=False)

print(f"{[prod_1, prod_2]}") # [Product(id=12, name='phone', price=22.34, in_stock=True, is_listing=False), Product(id=1, name='cooler', price=12.12, in_stock=False, is_listing=True)]


"""
{
  "typing_module": {
    "definition": "A standard library module providing type constructors and protocols to annotate expected types of variables, arguments, and return values.",
    "categories": {
      "collection_generics": {
        "description": "Used to annotate collections and the types of items they hold.",
        "members": [
          {
            "name": "List",
            "syntax": "List[T]",
            "purpose": "A homogeneous list of elements of type T.",
            "example": "items: List[str] = ['item1', 'item2']"
          },
          {
            "name": "Dict",
            "syntax": "Dict[KeyT, ValueT]",
            "purpose": "A mapping with keys of KeyT and values of ValueT.",
            "example": "stock: Dict[str, int] = {'phone': 10}"
          },
          {
            "name": "Set",
            "syntax": "Set[T]",
            "purpose": "An unordered collection of unique elements of type T.",
            "example": "unique_ids: Set[int] = {1, 2, 3}"
          },
          {
            "name": "Tuple",
            "syntax": "Tuple[T1, T2, ...]",
            "purpose": "A fixed-size heterogeneous sequence, or Tuple[T, ...] for variable length.",
            "example": "coordinate: Tuple[float, float] = (12.5, 77.2)"
          }
        ]
      },
      "choice_and_presence_types": {
        "description": "Used when a value can be multiple types or might be absent.",
        "members": [
          {
            "name": "Optional",
            "syntax": "Optional[T]",
            "purpose": "Shorthand for Union[T, None]. Field can be T or None.",
            "example": "image_url: Optional[str] = None"
          },
          {
            "name": "Union",
            "syntax": "Union[T1, T2]",
            "purpose": "Value can match any one of the specified types.",
            "example": "identifier: Union[int, str] = 'EMP-101'"
          },
          {
            "name": "Literal",
            "syntax": "Literal[val1, val2]",
            "purpose": "Restricts value to exact literal primitive values (enums/constants).",
            "example": "status: Literal['pending', 'completed', 'failed'] = 'pending'"
          }
        ]
      },
      "general_and_fallback_types": {
        "description": "Used when values are unconstrained, dynamic, or return nothing.",
        "members": [
          {
            "name": "Any",
            "syntax": "Any",
            "purpose": "Disables type checking; accepts any data type without validation.",
            "example": "payload: Any = {'anything': 123}"
          },
          {
            "name": "None",
            "syntax": "None",
            "purpose": "Represents the absence of a value (e.g., function returns nothing).",
            "example": "def log(msg: str) -> None: print(msg)"
          }
        ]
      },
      "functions_and_callables": {
        "description": "Used to annotate functions passed as arguments or returned values.",
        "members": [
          {
            "name": "Callable",
            "syntax": "Callable[[Arg1T, Arg2T], ReturnT]",
            "purpose": "Represents a function/callable object with specific argument and return types.",
            "example": "validator: Callable[[int], bool] = lambda x: x > 0"
          }
        ]
      },
      "structural_typing_and_models": {
        "description": "Advanced typing tools to define schemas and duck-typed interfaces.",
        "members": [
          {
            "name": "TypedDict",
            "syntax": "class Schema(TypedDict): ...",
            "purpose": "Type-hints standard dictionary keys and their value types.",
            "example": "class UserDict(TypedDict): name: str; age: int"
          },
          {
            "name": "TypeVar",
            "syntax": "T = TypeVar('T')",
            "purpose": "Generic type parameter for building reusable generic classes/functions.",
            "example": "def identity(item: T) -> T: return item"
          },
          {
            "name": "Protocol",
            "syntax": "class Named(Protocol): ...",
            "purpose": "Defines structural subtyping (duck typing interfaces).",
            "example": "class Printable(Protocol): def render(self) -> str: ..."
          }
        ]
      }
    }
  }
}
"""

class Cart(BaseModel):
    id:int
    items:List[str]
    quantities:Dict[str, int]
    images_url:Optional[str] = None

cart_data={
    "id":12,
    "items":["Laptop", "Mouse", "KeyBoard"],
    "quantities":{"laptop":2, "mouse":4, "keyboard":9},
    "images_url":"https://image1"
}

c1 = Cart(id=cart_data["id"], items=cart_data["items"], quantities=cart_data["quantities"], images_url=cart_data["images_url"])
c2 = Cart(**cart_data) # spread operation only works inside the functions, class. 

print([c1, c2]) # [Cart(id=12, items=['Laptop', 'Mouse', 'KeyBoard'], quantities={'laptop': 2, 'mouse': 4, 'keyboard': 9}, images_url='https://image1'), Cart(id=12, items=['Laptop', 'Mouse', 'KeyBoard'], quantities={'laptop': 2, 'mouse': 4, 'keyboard': 9}, images_url='https://image1')]
