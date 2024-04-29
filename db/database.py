from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine

SQLALCHEMY_BASE_URL = 'sqlite:///./rental.db'

engine = create_engine(
    SQLALCHEMY_BASE_URL, connect_args={"check_same_thread": False}, isolation_level='SERIALIZABLE'
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
        db.commit()  
    except Exception as e:
        db.rollback()  
        raise e
    finally:
        db.close()  