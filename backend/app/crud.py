from sqlalchemy.orm import Session
from sqlalchemy import or_
import models
import schemas

def get_case(db: Session, case_id: int):
    return db.query(models.Case).filter(models.Case.id == case_id).first()

def get_cases(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Case).offset(skip).limit(limit).all()

def create_case(db: Session, case: schemas.CaseCreate):
    db_case = models.Case(**case.dict())
    db.add(db_case)
    db.commit()
    db.refresh(db_case)
    return db_case

def search_cases(db: Session, **filters):
    query = db.query(models.Case)

    # Extract and remove full_text_search from filters if present
    full_text_search = filters.pop("full_text_search", None)

    # Apply structured filters
    for attr, value in filters.items():
        if value is not None:
            query = query.filter(getattr(models.Case, attr) == value)

    # Apply keyword/full text search
    if full_text_search:
        search_pattern = f"%{full_text_search}%"
        query = query.filter(
            or_(
                models.Case.case_summary.ilike(search_pattern),
                models.Case.full_text.ilike(search_pattern),
                models.Case.keywords.ilike(search_pattern),
                models.Case.title.ilike(search_pattern),
            )
        )

    return query.all()

