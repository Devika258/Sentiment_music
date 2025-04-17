from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str  # plaintext on input, hashed in storage
