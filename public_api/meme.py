from typing import List

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

import database
import models
import schemas

app = FastAPI()


# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/memes", response_model=List[schemas.Meme])
def get_memes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    memes = db.query(models.Meme).offset(skip).limit(limit).all()
    return memes


@app.get("/memes/{meme_id}", response_model=schemas.Meme)
def get_meme(meme_id: int, db: Session = Depends(get_db)):
    meme = db.query(models.Meme).filter(models.Meme.id == meme_id).first()
    # raise (meme)
    if meme is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return meme


@app.post("/memes", response_model=schemas.Meme)
def create_meme(meme: schemas.MemeCreate, db: Session = Depends(get_db)):
    db_meme = models.Meme(**meme.dict())
    db.add(db_meme)
    db.commit()
    db.refresh(db_meme)
    return db_meme


@app.put("/memes/{meme_id}", response_model=schemas.Meme)
def update_meme(meme_id: int, meme: schemas.MemeUpdate, db: Session = Depends(get_db)):
    db_meme = db.query(models.Meme).filter(models.Meme.id == meme_id).first()
    if db_meme is None:
        raise HTTPException(status_code=404, detail="Meme not found")
    for var, value in vars(meme).items():
        setattr(db_meme, var, value) if value else None
    db.commit()
    db.refresh(db_meme)
    return db_meme


@app.delete("/memes/{meme_id}", response_model=schemas.Meme)
def delete_meme(meme_id: int, db: Session = Depends(get_db)):
    meme = db.query(models.Meme).filter(models.Meme.id == meme_id).first()
    if meme is None:
        raise HTTPException(status_code=404, detail="Meme not found")
    db.delete(meme)
    db.commit()
    return meme
