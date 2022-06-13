from pydantic import BaseModel


class RecommendListBase(BaseModel):
    category1: str
    category2: str
    category3: str
    category4: str
    category5: str
    category6: str


class RecommendListCreate(RecommendListBase):
    pass


class RecommendList(RecommendListBase):
    id: int
    # owner_id: int

    class Config:
        orm_mode = True

class InFosBase(BaseModel):
    gender: int
    age: int


class InFosCreate(InFosBase):
    pass


class InFos(InFosBase):
    id: int
    # owner_id: int

    class Config:
        orm_mode = True