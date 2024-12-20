from sqlalchemy import Column, Integer, String

from db import Base


class TermModel(Base):
    __tablename__ = "terms"
    id = Column(Integer, primary_key=True, index=True)
    term = Column(String, unique=True, index=True, nullable=False)
    definition = Column(String)
