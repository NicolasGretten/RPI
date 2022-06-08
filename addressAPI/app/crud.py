from sqlalchemy.orm import Session

from . import models, schemas


def get_address(db: Session, address_id: int):
    return db.query(models.Address).filter(models.Address.id == address_id).first()


def get_addresses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Address).offset(skip).limit(limit).all()


def create_address(db: Session, address: schemas.AddressBase):
    db_address = models.Address(city=address.city, zip_code=address.zip_code, adress_line_1=address.adress_line_1)
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address
