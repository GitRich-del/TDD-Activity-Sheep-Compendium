from pydantic import BaseModel, Field


class Sheep(BaseModel):
    id: int = Field(..., gt=0)
    name: str = Field(..., min_length=1)
    breed: str = Field(..., min_length=1)
    sex: str = Field(..., min_length=1)
