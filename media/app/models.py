from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class FaceImages(Base):
    __tablename__ = "faceimages"

    id = Column(Integer, primary_key=True, index=True)
    kiosk_id = Column(Integer, index=True)
    face_image = Column(String(200), unique=True, index=True)



class InFos(Base):
    __tablename__ = "infos"

    id = Column(Integer, primary_key=True, index=True)
    gender = Column(Integer, index=True)
    age = Column(Integer, index=True)
    owner_id = Column(Integer, ForeignKey("faceimages.id"))

   


class RecommendList(Base):
    __tablename__ = "recommends_list"

    id = Column(Integer, primary_key=True, index=True)
    category1 = Column(String(200), index=True)
    category2 = Column(String(200), index=True)
    category3 = Column(String(200), index=True)
    category4 = Column(String(200), index=True)
    category5 = Column(String(200), index=True)
    category6 = Column(String(200), index=True)
    owner_id = Column(Integer, ForeignKey("recommends.id"))