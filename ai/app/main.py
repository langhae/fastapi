from fastapi.responses import JSONResponse
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine
from .env import POST_URI

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post(f"/{POST_URI}", response_model=schemas.FaceImages)
def create_faceimage(faceimages: schemas.FaceImagesCreate, db: Session = Depends(get_db)):
    db_user = crud.create_infos(db=db, recommend=faceimages)
    
    return JSONResponse(content=db_user)



