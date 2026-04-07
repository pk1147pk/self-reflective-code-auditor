from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

# ---------------- DATABASE CONFIG ----------------
DATABASE_URL = "sqlite:///./users.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# ---------------- USER TABLE ----------------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)   # ✅ Primary Key

    email = Column(String, unique=True)
    password = Column(String)

    # Profile fields
    name = Column(String)
    github = Column(String)
    linkedin = Column(String)
    instagram = Column(String)
    bio = Column(String)


# ---------------- ANALYSIS TABLE ----------------
class Analysis(Base):
    __tablename__ = "analysis"

    id = Column(Integer, primary_key=True, index=True)   # ✅ MUST HAVE PRIMARY KEY

    user_id = Column(Integer)
    score = Column(Integer)
    issues = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)


# ---------------- CREATE TABLES ----------------
Base.metadata.create_all(bind=engine)