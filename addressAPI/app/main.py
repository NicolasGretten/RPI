from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas, database


models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/addresses/", response_model=schemas.Address)
def create_user(address: schemas.AddressBase, db: Session = Depends(get_db)):
    return crud.create_address(db=db, address=address)


@app.get("/addresses/", response_model=list[schemas.Address])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_addresses(db, skip=skip, limit=limit)
    return users


@app.get("/addresses/{address_id}", response_model=schemas.Address)
def read_user(address_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_address(db, address_id=address_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return db_user
