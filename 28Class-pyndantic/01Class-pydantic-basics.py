"""
Pydantic is a data validation and settings management library for Python. 
It enforces type hints at runtime, validates incoming data, coerces compatible types, 
and produces user-friendly error messages when data does not conform to the schema you define.

Why Use Pydantic?
Python is dynamically typed: standard type hints (x: int) are merely hints for linters and IDEs, not runtime guarantees. 
Pydantic bridges this gap by acting as a runtime type contract.

Automatic Type Coercion: If a field is typed as int and you pass "42", Pydantic parses it into 42 automatically.

Detailed Error Messages: When data fails validation, Pydantic pinpoints the exact field, the invalid value, and why it failed.

High Performance: Core validation logic is written in Rust (pydantic-core), making it significantly faster than purely Python-based validation tools.

Seamless Serialization: Easily convert models to and from Python dictionaries, JSON strings, and database outputs using .model_dump() and .model_dump_json().

Deep Ecosystem Integration: Frameworks like FastAPI, LangChain, and SQLModel rely on Pydantic as their primary data modeling foundation.
"""

"""
Where to Use It
Web APIs & Frameworks:

FastAPI: Request body parsing, query parameter validation, and response schema enforcement.

Configuration Management (pydantic-settings):

Reading and validating environment variables, .env files, or secrets at application startup.

LLM & AI Pipelines (e.g., LangChain, Instructor):

Enforcing structured outputs (JSON schema) from Large Language Models.

ETL & Data Ingestion Pipelines:

Cleaning and validating untrusted records coming from CSVs, external webhooks, or third-party APIs.

Microservice Communication:

Validating message payloads on message brokers like Kafka, RabbitMQ, or AWS SQS.
"""

"""
When to Use It (and When Not To)

[
  {
    "scenario": "API boundaries & Webhooks",
    "recommendation": "Use Pydantic",
    "reason": "External data cannot be trusted; automatic validation and error reporting are critical."
  },
  {
    "scenario": "Reading environment variables",
    "recommendation": "Use Pydantic",
    "reason": "Fails fast on boot if required credentials or configs are missing or malformed."
  },
  {
    "scenario": "Structured LLM outputs",
    "recommendation": "Use Pydantic",
    "reason": "Keeps non-deterministic text outputs pinned to a strict, parseable schema."
  },
  {
    "scenario": "Internal data structures (in-memory)",
    "recommendation": "Use dataclasses or namedtuple",
    "reason": "If the data is already validated, standard library dataclasses have lower memory overhead and require no external dependencies."
  },
  {
    "scenario": "Heavy array/matrix computation",
    "recommendation": "Use NumPy / Pandas / Polars",
    "reason": "Pydantic validates row-by-row and object-by-object; it is not designed for vectorized mathematical workloads."
  }
]

"""
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool

input_data = {'id':'shit', 'name':'siddiq', 'is_active':True }

user = User(**input_data) # ** is used to unpack the dictionary
print(user)

"""
output
pydantic_core._pydantic_core.ValidationError: 1 validation error for User
id
  Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='shit', input_type=str]
    For further information visit https://errors.pydantic.dev/2.14/v/int_parsing
"""