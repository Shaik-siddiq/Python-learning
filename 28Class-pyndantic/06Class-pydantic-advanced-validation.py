from pydantic import BaseModel, field_validator, model_validator
import datetime
class validating(BaseModel):
    first_name:str
    last_name:str

    @field_validator('first_name', 'last_name')
    def uppercaseOnly(cls, v)->str:
        if not v.istitle():
            raise ValueError(f"should be capitalize the name")
        return v

class Price(BaseModel):
    p:str

    @field_validator('p', mode='before')
    def parse_price(cls, p1):
        if isinstance(p1, str):
            return float(p1.replace('$', ''))
        return p1 

class DateRageValidate(BaseModel):
    startDate:datetime
    endDate:datetime

    @model_validator(mode='after')
    def validator_date(cls, d):
        if d.startDate >= d.endDate:
            raise ValueError("start Date should be less than end date")

"""
{
  "validation_and_parsing_methods": {
    "string_casing_and_inspection": {
      "category": "String Character & Case Checks",
      "methods": [
        {
          "name": "str.isalpha()",
          "purpose": "Checks if string contains only alphabetic characters (no digits, spaces, or symbols).",
          "use_case": "Validating first/last names contain letters only."
        },
        {
          "name": "str.isdigit() / str.isnumeric()",
          "purpose": "Checks if string contains only numeric digit characters.",
          "use_case": "Validating PIN codes, OTPs, or credit card digits before conversion."
        },
        {
          "name": "str.isalnum()",
          "purpose": "Checks if string contains only letters and numbers.",
          "use_case": "Validating alphanumeric usernames or promo codes."
        },
        {
          "name": "str.isupper() / str.islower()",
          "purpose": "Checks if all cased characters are uppercase or lowercase.",
          "use_case": "Enforcing uppercase ISO country codes (e.g., 'US', 'IN') or lowercase slugs."
        },
        {
          "name": "str.startswith() / str.endswith()",
          "purpose": "Checks prefix or suffix patterns.",
          "use_case": "Ensuring URLs start with 'https://' or file paths end with '.png'."
        }
      ]
    },
    "string_sanitization_and_cleaning": {
      "category": "Pre-Validation Parsing & Normalization",
      "methods": [
        {
          "name": "str.strip()",
          "purpose": "Removes leading and trailing whitespace or custom characters.",
          "use_case": "Cleaning form inputs in mode='before' before length validation."
        },
        {
          "name": "str.lower() / str.upper()",
          "purpose": "Normalizes text case.",
          "use_case": "Converting incoming emails or coupon codes to standard case."
        },
        {
          "name": "str.split() / str.join()",
          "purpose": "Breaks strings by delimiters or rejoins tokens into standard format.",
          "use_case": "Parsing comma-separated tags 'python,ai,fastapi' into a list."
        },
        {
          "name": "str.replace()",
          "purpose": "Substitutes target substrings with alternatives.",
          "use_case": "Removing currency symbols, phone dashes, or commas from numeric strings."
        }
      ]
    },
    "type_and_collection_inspection": {
      "category": "Type & Structure Validation",
      "methods": [
        {
          "name": "isinstance(val, (T1, T2))",
          "purpose": "Checks if a value belongs to one or more expected Python classes.",
          "use_case": "Guarding mode='before' parsers so lists or ints don't call string methods."
        },
        {
          "name": "issubclass(cls, Base)",
          "purpose": "Checks if a class object derives from a target parent class.",
          "use_case": "Validating plugin or registry class types passed into dynamic models."
        },
        {
          "name": "callable(val)",
          "purpose": "Checks if an object can be invoked like a function.",
          "use_case": "Validating callback or handler parameters."
        },
        {
          "name": "all(iterable) / any(iterable)",
          "purpose": "Evaluates boolean conditions across an entire sequence.",
          "use_case": "Checking all scores in a list are positive (`all(x > 0 for x in scores)`)."
        },
        {
          "name": "len(collection)",
          "purpose": "Returns element or character count.",
          "use_case": "Enforcing exact lengths (e.g., verifying a token has exactly 32 chars)."
        }
      ]
    },
    "regex_and_pattern_matching": {
      "category": "Complex Pattern Rules",
      "methods": [
        {
          "name": "re.fullmatch(pattern, string)",
          "purpose": "Ensures the entire string matches a regular expression pattern from start to end.",
          "use_case": "Validating UUIDs, slug identifiers, or specific phone formats."
        },
        {
          "name": "re.search(pattern, string)",
          "purpose": "Finds a pattern match anywhere inside a string.",
          "use_case": "Checking password rules (e.g., requires at least 1 special char and 1 digit)."
        }
      ]
    },
    "date_and_time_methods": {
      "category": "Temporal Validation",
      "methods": [
        {
          "name": "datetime.date.today() / datetime.datetime.now()",
          "purpose": "Retrieves current temporal reference point.",
          "use_case": "Ensuring birth dates are in the past or expiry dates are in the future."
        },
        {
          "name": "datetime.strptime(str, format)",
          "purpose": "Parses custom non-ISO date string formats into datetime objects.",
          "use_case": "Parsing legacy date formats like 'DD/MM/YYYY' inside mode='before' validators."
        }
      ]
    }
  }
}
"""