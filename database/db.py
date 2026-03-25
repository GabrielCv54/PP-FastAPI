from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd

Base = declarative_base() # A base que serve para criação dos modelos do banco de dados

engine = create_engine('sqlite:///finance.db')


Session = sessionmaker(bind=engine)
session = Session()

'''df_user = pd.read_sql('SELECT * FROM user',engine)
df_transac = pd.read_sql('SELECT * FROM transaction',engine)'''