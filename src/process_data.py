import pandas as pd
from data_loader import load_csv_data
from database import connect_to_database


def process_data():
    # Carrega os dados do arquivo CSV
    data = load_csv_data()

    # Renomeia as colunas para corresponder à tabela do banco
    data = data.rename(
        columns={
            "room_id/id": "room_id",
            "out/in": "location_type"
        }
    )

    # Converte as datas para o formato do PostgreSQL
    data["noted_date"] = pd.to_datetime(
        data["noted_date"],
        format="%d-%m-%Y %H:%M"
    )

    engine = connect_to_database()

    # Insere os registros na tabela existente
    data.to_sql(
        name="temperature_readings",
        con=engine,
        if_exists="append",
        index=False
    )

    engine.dispose()

    print(f"Quantidade de registros importados: {len(data)}")


if __name__ == "__main__":
    process_data()
