import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import Base

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
db_url = "postgresql+psycopg2://myuser:mypassword@localhost:5432/mydatabase"
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import Base

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
db_url = "postgresql+psycopg2://myuser:mypassword@localhost:5432/mydatabase"
engine = create_engine(db_url, echo=False)

Session = sessionmaker(bind=engine)

from .db import CrudTable