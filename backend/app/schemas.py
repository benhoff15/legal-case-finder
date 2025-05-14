from pydantic import BaseModel
from typing import Optional

class CaseBase(BaseModel):
    title: str
    case_summary: Optional[str] = None
    full_text: Optional[str] = None
    charges: Optional[str] = None
    defendant_age: Optional[int] = None
    defendant_race: Optional[str] = None
    state: Optional[str] = None
    year: Optional[int] = None
    court_type: Optional[str] = None
    keywords: Optional[str] = None

class CaseCreate(CaseBase):
    pass

class Case(CaseBase):
    id: int

    class Config:
        orm_mode = True
