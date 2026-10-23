from pydantic import BaseModel, field_validator, model_validator, ValidationError

"""
@field_validator — validates a single field in isolation (e.g., verifying userName format/length).
"""
class User(BaseModel):
    userName:str
    @field_validator('userName')
    def validate_username(cls, val):
        if len(val) < 3:
            raise ValueError(f"The {val} should be greater than 3 charechters")
        return val

"""
@model_validator — validates multiple fields together across the whole model (e.g., checking if password matches confrim_password).
"""
class SignUpData(BaseModel):
    password: str
    confrim_password:str 
    @model_validator(mode='after')
    def pass_match(self):
        if self.password != self.confrim_password:
            raise ValueError('😑 Please try again')
        return self

# Valid User
u1 = User(userName="Siddiq")
print("✅ Success:", u1.userName)

# Invalid User (too short)
try:
    User(userName='AI')
except ValidationError as e:
    print(f"❌ Expected error as {e.errors()[0]["msg"]}")

# Valid Sign-up (Passwords match)
s1 = SignUpData(password="secret123", confrim_password="secret123")
print("✅ Passwords match! Account created.")

try:
    SignUpData(password="sh123", confrim_password = "ab125")
except ValidationError as e:
    print(f"🤦🏻 match the passwords {e.errors()[0]['msg']}")
