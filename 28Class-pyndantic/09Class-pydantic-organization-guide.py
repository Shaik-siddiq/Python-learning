"""
Pydantic Model Organization Guide
A clean pattern for structuring nested schemas in minimal lines of code:

Leaf models first (innermost components defined at the top).

Build upward (each model depends only on already-defined classes).

Use clear naming (self-descriptive nouns).

Group related models (keep domain-bounded models together).
"""
# Example: E-Commerce Order

from pydantic import BaseModel, PositiveInt, NonNegativeFloat

# ==========================================
# 1. Leaf Models (Base building blocks)
# ==========================================
class GeoLocation(BaseModel):
    lat: float
    lng: float

class OrderItem(BaseModel):
    sku: str
    quantity: PositiveInt
    unit_price: NonNegativeFloat

# ==========================================
# 2. Intermediate Models (Composing leaves)
# ==========================================
class ShippingAddress(BaseModel):
    street: str
    city: str
    postal_code: str
    location: GeoLocation | None = None

# ==========================================
# 3. Root / Aggregate Model (Top-level schema)
# ==========================================
class Order(BaseModel):
    order_id: str
    customer_id: str
    shipping: ShippingAddress
    items: list[OrderItem]

data = {
    "order_id": "ORD-101",
    "customer_id": "CUST-9",
    "shipping": {
        "street": "123 Main St",
        "city": "Bengaluru",
        "postal_code": "560001",
        "location": {"lat": 12.9716, "lng": 77.5946},
    },
    "items": [
        {"sku": "KEY-01", "quantity": 1, "unit_price": 49.99},
        {"sku": "MOU-02", "quantity": 2, "unit_price": 19.50},
    ],
}

order = Order.model_validate(data)

# Accessing deeply nested fields naturally
print(order.shipping.city)           # Bengaluru
print(order.shipping.location.lat)   # 12.9716
print(order.items[0].sku)            # KEY-01