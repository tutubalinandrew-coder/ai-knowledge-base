from pydantic import BaseModel
from pydantic import ConfigDict



class UserCreate(BaseModel):
    telegram_id: int
    username: str | None

class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    telegram_id: int
    username: str | None
