from pydantic import BaseModel, computed_field

"""
{
  "decorator_concepts": {
    "decorator": {
      "definition": "A callable in Python that takes another function or method as an argument, 
      extends or alters its behavior without modifying its source code directly, and returns a new callable or descriptor object.",
      "syntax": "@decorator_name",
      "mechanism": "Syntactic sugar for `func = decorator_name(func)` evaluated at definition time."
    },
    "property": {
      "definition": "A built-in Python decorator that converts an instance method into a read-only getter attribute, 
      enabling access via dot notation (`obj.attribute`) without function call parentheses `()`.",
      "origin": "Standard library (Python built-in)",
      "primary_role": "Encapsulates calculated logic behind standard attribute access syntax.",
      "pydantic_behavior": "Invisible to Pydantic serialization methods (`.model_dump()`, `.model_dump_json()`) and omitted from generated JSON schemas."
    },
    "computed_field": {
      "definition": "A Pydantic v2 decorator that wraps a property or cached property, registering the computed output as an official, 
      read-only field in the model's schema and serialization output.",
      "origin": "pydantic module",
      "primary_role": "Bridges Python dynamic properties with Pydantic serialization, OpenAPI generation, and type introspection.",
      "pydantic_behavior": "Included in `.model_dump()`, serialized in `.model_dump_json()`, and declared with types in `.model_json_schema()`."
    }
  }
}
"""

class Product(BaseModel):
    price:float
    quantity:int

    @computed_field
    @property
    def totalIncome(self)->float:
        return self.price * self.quantity

p1 = Product(price="22.4", quantity=9)
print(p1.totalIncome) # 201.6