from pathlib import Path


PASTA_PROJETO = Path(__file__).resolve().parents[2]

PASTA_DADOS = PASTA_PROJETO / "dados"

# coloque abaixo o caminho para os arquivos de dados de seu projeto
DADOS_2005_2014 = PASTA_DADOS / "canada_2005_2014.csv"
DADOS_2015_2019 = PASTA_DADOS / "canada_2015_2019.csv"
DADOS_2020 = PASTA_DADOS / "canada_2020.csv"
DADOS_2021 = PASTA_DADOS / "canada_2021.csv"
DADOS_2022 = PASTA_DADOS / "canada_2022.csv"
DADOS_2023 = PASTA_DADOS / "canada_2023.csv"
DADOS_2024 = PASTA_DADOS / "canada_2024.csv"
DADOS_CONSOLIDADOS = PASTA_DADOS / "canada_consolidados.parquet"
DADOS_TRATADOS = PASTA_DADOS / "canada_tratados.parquet"

# coloque abaixo o caminho para os arquivos de modelos de seu projeto
PASTA_MODELOS = PASTA_PROJETO / "modelos"
MODELO_FINAL = PASTA_MODELOS / "ridge.joblib"

# coloque abaixo outros caminhos que você julgar necessário
PASTA_RELATORIOS = PASTA_PROJETO / "relatorios"
PASTA_IMAGENS = PASTA_RELATORIOS / "imagens"
