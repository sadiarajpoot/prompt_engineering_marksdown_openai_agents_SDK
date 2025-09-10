class Address(BaseModel):
    city: str
    country: str

class User(BaseModel):
    name: str
    age: int
    address: Address   # Nested model

# ✅ Valid
user = User(
    name="Sadia",
    age=22,
    address={"city": "Karachi", "country": "Pakistan"}
)
print(user)

# ❌ Invalid (address missing city)
try:
    bad_user = User(
        name="Ali",
        age=25,
        address={"country": "Pakistan"}
    )
except Exception as e:
    print("Error:", e)
