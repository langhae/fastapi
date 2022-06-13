from pydantic import BaseModel


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


class FaceImagesBase(BaseModel):
    kiosk_id: int
    face_image: str


class FaceImagesCreate(FaceImagesBase):
    pass


class FaceImages(FaceImagesBase):
    id: int

    class Config:
        orm_mode = True

