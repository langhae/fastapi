from sqlalchemy.orm import Session

from . import models, schemas
from .faces_test_6 import classify_age, classify_gender, url_to_image

# def get_faceimage_by_uri(db: Session, face_image: str):
#     return db.query(models.FaceImages).filter(models.FaceImages.face_image == face_image).first()


def create_infos(db: Session, recommend: schemas.FaceImagesCreate):
    img = url_to_image(recommend.face_image)
    age_img = classify_age(img)
    gender_img = classify_gender(img)
    db_user = models.InFos(age=age_img, gender=gender_img)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    output_data = {'age': age_img, 'gender': gender_img}
    return output_data
