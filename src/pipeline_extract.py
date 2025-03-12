import pandas as pd


def csv_files():
    """Função de teste, para armazenar os arquivos CSV que vamos utilizar para extração de dados."""

    csv = [
        "dados/raw_orders.csv",
        "dados/raw_products.csv",
        "dados/raw_customers.csv",
        "dados/raw_stores.csv",
        "dados/raw_supplies.csv",
        "dados/raw_items.csv",
    ]
    return csv


def leitura_dados_csv(csvs: str) -> list:
    """Função com objetivo de leitura e extração de dados de um arquivo CSV gerando resultado de visualização em Dataframe."""
    dataframes = []
    for csv in csvs:
        df = pd.read_csv(csv)
        dataframes.append(df)

    return df


def pipeline_extração_e_leitura_dados_csv(csv) -> pd.DataFrame:
    """Pipeline de extração e leitura de dados de um CSV."""
    dataframe = leitura_dados_csv(csv)
    print(dataframe)


if __name__ == "__main__":
    pipeline_extração_e_leitura_dados_csv()
