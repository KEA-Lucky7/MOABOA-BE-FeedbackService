import sys

from starlette.config import Config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# env = sys.argv[1] if len(sys.argv) > 1 else 'dev'
config = Config('.env')

SQLALCHEMY_DATABASE_URL = config('DATABASE_URI', cast=str)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()