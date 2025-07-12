from sqlalchemy import Column, Integer, String, Text
from db.base import Base

class Prompt(Base):
    __tablename__ = "prompts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    content = Column(Text)
