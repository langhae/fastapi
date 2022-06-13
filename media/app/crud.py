from sqlalchemy.orm import Session

from . import models, schemas


def get_faceimage_by_uri(db: Session, face_image: str):
    return db.query(models.FaceImages).filter(models.FaceImages.face_image == face_image).first()

# def get_id_by_face_image(db: Session, face_image: str):
#     return db.query(models.FaceImages).filter(models.FaceImages.face_image == face_image).scalar()

def create_faceimage(db: Session, faceimages: schemas.FaceImagesCreate):
    db_user = models.FaceImages(kiosk_id=faceimages.kiosk_id, face_image=faceimages.face_image)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user




