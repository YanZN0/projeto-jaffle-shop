##  Código para conseguirmos conexão com o nosso Cloud de armazenamento com o SQLAlchemy-BigQuery.

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

project_id = os.getenv("PROJECT_ID")
project_dataset = os.getenv("PROJECT_DATASET")


engine = create_engine(
    f"bigquery://{project_id}/{project_dataset}"
)  ## Fazendo a conexão ao banco pelo ID do projeto.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

print(
    "Conexão Estabelecida com Sucesso!"
)  ## Print de test caso a conexão for estabelecida.
