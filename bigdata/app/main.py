from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

from .when_no_user import result_no_population
from .env import POST_URI, GET_URI

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post(f"/{POST_URI}", response_model=schemas.InFos)
def create_recommend(infos: schemas.InFosCreate, db: Session = Depends(get_db)):
    # Create age / gender
    # crud.create_recommend(db=db, recommend=recommend)

    db_user = crud.create_recommend_list(db=db, infos=infos)
    # modeling output

    return JSONResponse(content=db_user)



@app.get(f"/{GET_URI}")
async def read_recommends():
    recommend_url_list = result_no_population()

    return JSONResponse(content=recommend_url_list)

@app.get("/")
async def request_pass():
    pass
