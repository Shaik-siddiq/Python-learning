from typing import Optional
from pydantic import BaseModel, Field
import re # re means library for regex

"""
1. What is Field in Pydantic?
Field is a function provided by Pydantic used to customize and add constraints, metadata, and validation rules directly to individual model attributes.
Without Field, you can only enforce basic types (like name: str or age: int). With Field, you can enforce:
- Required vs Optional: Passing ... (the Python Ellipsis singleton) as the first argument explicitly marks the field as required (no default value).
- Length constraints for strings/lists: Limits on minimum and maximum characters.
- Numeric boundaries: Limits on numbers ($>$, $\ge$, $<$, $\le$).
- Metadata & Documentation: Documentation attributes (description, examples, title) that automatically populate OpenAPI/Swagger documentation in frameworks like FastAPI.
- Regex patterns: Pattern matching for strings (e.g., emails, phone numbers, codes).

"""
# ----------------------------------------------------
# 1. Regex Validation Functions using the `re` library
# ----------------------------------------------------
"""
    What is re?
    re is Python's built-in Regular Expressions (Regex) library. It allows you to search, match, and validate text based on specific pattern rules 
    (like verifying email formats, phone numbers, or zip codes).
    In standard Python code, you use functions like re.match() or re.search(). 
    However, inside a Pydantic Field, you don't call re functions directly—instead,
    you pass a raw regex pattern string (e.g., r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$') to the regex argument,
   and Pydantic uses regular expressions internally to validate incoming input.
"""
# Regex pattern for a standard email address
EMAIL_REGEX = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

# Regex pattern for international/standard phone numbers (10 to 15 digits, optional leading +)
PHONE_REGEX = r"^\+?[1-9]\d{9,14}$"


def validate_email(email: str) -> bool:
    """Validates an email string using Python's re library.

    Returns True if valid, False otherwise.
    """
    return bool(re.match(EMAIL_REGEX, email.strip()))


def validate_phone(phone: str) -> bool:
    """Validates a phone number string using Python's re library.

    Returns True if valid, False otherwise.
    """
    return bool(re.match(PHONE_REGEX, phone.strip()))


# ----------------------------------------------------
# 2. Pydantic Model
# ----------------------------------------------------


class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=51,
        description="Employee Name",
        examples=["Siddiq Shaik"],
    )
    department: Optional[str] = "General"
    salary: float = Field(..., ge=100_000, le=1_000_000)
    email: str = Field(..., pattern=EMAIL_REGEX)
    phone: str = Field(..., pattern=PHONE_REGEX)
    age: int = Field(..., ge=18, le=85, description="Age in Years")


# ----------------------------------------------------
# 3. Validation Tests & Employee Instance E1
# ----------------------------------------------------

test_email = "siddiq.shaik@techcorp.com"
test_phone = "+919876543210"

# Test the validation functions
print("Is email valid?:", validate_email(test_email))  # Output: True
print("Is phone valid?:", validate_phone(test_phone))  # Output: True
print("Is bad email valid?:", validate_email("bad-email@"))  # Output: False

# Store random valid employee details into E1
E1 = Employee(
    id=101,
    name="Siddiq Shaik",
    department="Engineering",
    salary=450000.0,
    email=test_email,
    phone=test_phone,
    age=28,
)

print("\nStored Employee (E1):")
print(E1.model_dump_json(indent=2))
