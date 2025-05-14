from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Case(Base):
    __tablename__ = "cases"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    case_summary = Column(Text)
    full_text = Column(Text)
    charges = Column(String, index=True)
    defendant_age = Column(Integer)
    defendant_race = Column(String)
    state = Column(String, index=True)
    year = Column(Integer, index=True)
    court_type = Column(String)
    keywords = Column(String)
