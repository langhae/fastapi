from fastapi.responses import JSONResponse
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

import requests, json
from .env import POST_URI, POST_AI_URI, POST_BIGDATA_URI


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
    # query face_image
    db_faceimage = crud.get_faceimage_by_uri(db, face_image=faceimages.face_image)

    if db_faceimage:
        raise HTTPException(status_code=400, detail="faceimage already registered")
    else:
        crud.create_faceimage(db=db, faceimages=faceimages)
        data = {"kiosk_id": faceimages.kiosk_id, "face_image": faceimages.face_image}
        data2 = json.dumps(data)
        response = requests.post(f'{POST_AI_URI}', data=data2)
        response2 = requests.post(f"{POST_BIGDATA_URI}", json=response.json())

        return JSONResponse(content=response2.json())


@app.get("/")
async def request_pass():
    pass