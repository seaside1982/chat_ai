from dataclasses import dataclass

@dataclass
class UserInfo:
    user_id: str
    age: int
    gender: str
    zipcode: str
    email: str
    phone_number: str
    device: str
    os: str