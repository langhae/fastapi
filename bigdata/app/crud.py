from sqlalchemy.orm import Session

from . import models, schemas
from .find_priority_category import result_population

# def get_faceimage_by_uri(db: Session, face_image: str):
#     return db.query(models.FaceImages).filter(models.FaceImages.face_image == face_image).scalar()


# def create_recommend(db: Session, recommend: schemas.InFosCreate):
#     db_user = models.InFos(age=recommend.age, gender=recommend.gender)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


def create_recommend_list(db: Session, infos: schemas.InFosCreate):
    recommend_url_list = result_population(infos.age, infos.gender)
    db_user = models.RecommendList(
        category1=recommend_url_list[0],
        category2=recommend_url_list[1],
        category3=recommend_url_list[2],
        category4=recommend_url_list[3],
        category5=recommend_url_list[4],
        category6=recommend_url_list[5])
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    content = dict()
    content['url_list'] = recommend_url_list
    return content