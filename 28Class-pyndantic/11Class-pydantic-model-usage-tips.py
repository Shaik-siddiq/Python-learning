"""
A production-ready guide demonstrating four key modeling principles:

Mirror domain relationships directly

Use Optional strictly for optional concepts (avoid treating missing data as None)

Use Discriminated Unions for polymorphic structures

Enforce cross-field business invariants using @model_validator
"""

from typing import Annotated, Literal, Union
from pydantic import BaseModel, EmailStr, Field, model_validator, ValidationError


# ---------------------------------------------------------------------------
# 1. Discriminated Unions: Polymorphic Billing Methods
# ---------------------------------------------------------------------------
class InsurancePayment(BaseModel):
    payment_type: Literal["insurance"] = "insurance"
    provider_name: str
    policy_number: str
    copay_amount: float = Field(ge=0.0)


class CreditCardPayment(BaseModel):
    payment_type: Literal["credit_card"] = "credit_card"
    card_token: str
    last_four: str = Field(min_length=4, max_length=4)


class CashPayment(BaseModel):
    payment_type: Literal["cash"] = "cash"
    receipt_reference: str


# Pydantic matches the correct schema using the `payment_type` discriminator
PaymentMethod = Annotated[
    Union[InsurancePayment, CreditCardPayment, CashPayment],
    Field(discriminator="payment_type"),
]


# ---------------------------------------------------------------------------
# 2. Domain Structure & Purposeful Optionality
# ---------------------------------------------------------------------------
class EmergencyContact(BaseModel):
    # Mandatory fields: An emergency contact must have a name and phone
    full_name: str
    phone: str
    # Optional field: Relationship description is truly optional
    relation: str | None = None


# ---------------------------------------------------------------------------
# 3. Aggregate Model with Cross-Field Business Logic
# ---------------------------------------------------------------------------
class PatientOnboardingForm(BaseModel):
    # Core domain fields (mandatory)
    email: EmailStr
    password: str = Field(min_length=8)
    confirm_password: str
    age: int = Field(ge=0, le=120)

    # Domain relationship (mirroring real-world entities)
    emergency_contact: EmergencyContact

    # Polymorphic billing integration
    billing: PaymentMethod

    # Strict optional: Only required if the patient is a minor
    guardian_consent_signature: str | None = None

    # Cross-field business rule validation
    @model_validator(mode="after")
    def validate_business_rules(self) -> "PatientOnboardingForm":
        # Rule 1: Password confirmation check
        if self.password != self.confirm_password:
            raise ValueError("Password and confirmation password do not match.")

        # Rule 2: Minors (under 18) must have guardian consent
        if self.age < 18 and not self.guardian_consent_signature:
            raise ValueError(
                "Patients under 18 require a guardian consent signature."
            )

        # Rule 3: Adult patients cannot use guardian consent
        if self.age >= 18 and self.guardian_consent_signature:
            raise ValueError(
                "Guardian consent signature is only applicable for minors."
            )

        return self

minor_data = {
    "email": "teen@example.com",
    "password": "SecurePassword123",
    "confirm_password": "SecurePassword123",
    "age": 14,
    "emergency_contact": {
        "full_name": "Jane Doe",
        "phone": "+1-555-0199",
        "relation": "Mother",
    },
    "billing": {
        "payment_type": "insurance",
        "provider_name": "BlueCross",
        "policy_number": "POL-987654",
        "copay_amount": 25.0,
    },
    "guardian_consent_signature": "Jane Doe",
}

patient = PatientOnboardingForm.model_validate(minor_data)

# Accessing polymorphic types directly
print(type(patient.billing))  # <class '__main__.InsurancePayment'>
print(patient.billing.policy_number)  # POL-987654


invalid_data = {
    "email": "adult@example.com",
    "password": "Password123",
    "confirm_password": "PasswordMismatch456",  # Password mismatch
    "age": 25,
    "emergency_contact": {
        "full_name": "John Doe",
        "phone": "+1-555-0100",
    },
    "billing": {
        "payment_type": "cash",
        "receipt_reference": "REC-4412",
    },
}

try:
    PatientOnboardingForm.model_validate(invalid_data)
except ValidationError as e:
    print(e)
    # Output: Value error, Password and confirmation password do not match.

"""
Tips
[
  {
    "Pattern": "Domain Relationships",
    "Anti-Pattern": "Flattening all fields into one huge model (patient_name, contact_name, contact_phone, etc.).",
    "Recommended Practice": "Model entities separately (EmergencyContact) and compose them into the parent."
  },
  {
    "Pattern": "Optional Usage",
    "Anti-Pattern": "Defaulting everything to None (e.g., phone: str | None = None) to avoid ingestion errors.",
    "Recommended Practice": "Make fields required by default. Only use None if the absence of a value is a valid domain state."
  },
  {
    "Pattern": "Polymorphism",
    "Anti-Pattern": "Merging all payment fields into one model with 10 optional fields.",
    "Recommended Practice": "Define individual subclasses and bind them with Annotated[Union[...], Field(discriminator=...)]."
  },
  {
    "Pattern": "Cross-Field Logic",
    "Anti-Pattern": "Validating field combinations in controllers or route handlers.",
    "Recommended Practice": "Keep domain rules within the model using @model_validator(mode=\"after\")."
  }
]
"""