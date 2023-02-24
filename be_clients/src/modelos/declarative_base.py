from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2



db_endpoint = 'database-1.cr6db6ru4ziw.us-east-1.rds.amazonaws.com'
db_name = 'clientedb'
db_user = 'postgres'
db_password = 'eyz_hqj7YCG8zdp2njb'
db_port = '5432' # Por defecto el puerto de PostgreSQL es 5432

db_uri = f"postgresql://{db_user}:{db_password}@{db_endpoint}:{db_port}/{db_name}"

engine = create_engine(db_uri)


Session = sessionmaker(bind=engine)

Base = declarative_base()
Base.metadata.create_all(bind=engine)

session = Session()




