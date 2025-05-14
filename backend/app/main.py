from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
import models, schemas, crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Legal Case Finder API is running"}

@app.post("/cases/", response_model=schemas.Case)
def create_case(case: schemas.CaseCreate, db: Session = Depends(get_db)):
    return crud.create_case(db=db, case=case)

@app.get("/cases/", response_model=List[schemas.Case])
def read_cases(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_cases(db=db, skip=skip, limit=limit)

@app.get("/cases/{case_id}", response_model=schemas.Case)
def read_case(case_id: int, db: Session = Depends(get_db)):
    db_case = crud.get_case(db=db, case_id=case_id)
    if db_case is None:
        raise HTTPException(status_code=404, detail="Case not found")
    return db_case

@app.get("/search/", response_model=List[schemas.Case])
def search_cases(
    charges: Optional[str] = None,
    defendant_age: Optional[int] = None,
    defendant_race: Optional[str] = None,
    state: Optional[str] = None,
    year: Optional[int] = None,
    court_type: Optional[str] = None,
    full_text_search: Optional[str] = None,
    db: Session = Depends(get_db),
):
    filters = {
        "charges": charges,
        "defendant_age": defendant_age,
        "defendant_race": defendant_race,
        "state": state,
        "year": year,
        "court_type": court_type,
        "full_text_search": full_text_search,
    }
    return crud.search_cases(db=db, **filters)