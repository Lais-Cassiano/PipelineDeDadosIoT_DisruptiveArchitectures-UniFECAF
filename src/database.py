from sqlalchemy import create_engine, text

def connect_to_database():
    # Conexão com o Postgres
    engine = create_engine(
        "postgresql+psycopg2://postgres:test_password@localhost:5432/iot_database"
    )

    return engine


def create_table():
    # Cria a tabela com o esquema do SQLAlchemy
    engine = connect_to_database()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS temperature_readings (
        id TEXT,
        room_id TEXT,
        noted_date TIMESTAMP,
        temp REAL,
        location_type TEXT
    );
    """

    with engine.begin() as connection:
        connection.execute(text(create_table_query))

    # Libera os recursos de conexão
    engine.dispose()

    print("Tabela temperature_readings criada com sucesso!")


if __name__ == "__main__":
    create_table()
