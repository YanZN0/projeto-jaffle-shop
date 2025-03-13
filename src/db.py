##  Código para conseguirmos conexão com o nosso Cloud de armazenamento com o SQLAlchemy-BigQuery.


from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

project_id = "{{ env_var('PROJECT_ID') }}"


engine = create_engine(
    f"bigquery://{project_id}"
)  ## Fazendo a conexão ao banco pelo ID do projeto.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

print(
    "Conexão Estabelecida com Sucesso!"
)  ## Print de test caso a conexão for estabelecida.
