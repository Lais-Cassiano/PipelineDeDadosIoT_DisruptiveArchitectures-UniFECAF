import streamlit as st
import pandas as pd
import plotly.express as px
from database import connect_to_database


# Função para buscar os dados de uma view do PostgreSQL
def get_data_from_database(view_name):
    engine = connect_to_database()

    # Consulta os dados da view e transforma em dataframe
    query = f"SELECT * FROM {view_name}"

    data = pd.read_sql(query, engine)

    engine.dispose()

    return data


def main():
    st.title("Dashboard de Temperaturas - IoT")

    st.write(
        "Visualização dos dados de temperatura "
        "armazenados no PostgreSQL."
    )

    # Busca os dados da primeira view (temperatura média por localização)
    df_temperature = get_data_from_database(
        "avg_temperature_location"
    )

    st.subheader("Temperatura média por localização")

    # Cria um gráfico de barras com as médias
    fig_temperature = px.bar(
        df_temperature,
        x="location_type",
        y="avg_temperature",
        labels={
            "location_type": "Localização",
            "avg_temperature": "Temperatura média (°C)"
        }
    )

    # Exibe o gráfico no dashboard
    st.plotly_chart(fig_temperature, use_container_width=True)


    
    # Busca os dados da segunda view (registros por hora)
    df_hourly = get_data_from_database("readings_per_hour")

    st.subheader("Leituras por Hora")

    # Cria o gráfico de linhas
    fig_hourly = px.line(
        df_hourly,
        x="hour",
        y="total_readings",
        labels={
            "hour": "Hora do dia",
            "total_readings": "Quantidade de registros"
        },
        markers=True
    )

    # Exibe o gráfico no dashboard
    st.plotly_chart(fig_hourly, use_container_width=True)



    
    # Busca os dados da terceira view (temperaturas mínimas e máximas de cada dia)
    df_daily = get_data_from_database(
        "daily_temperature_extremes"
    )

    st.subheader("Temperaturas Máximas e Mínimas por Dia")

    # Cria o gráfico de linhas
    fig_daily = px.line(
        df_daily,
        x="reading_date",
        y=["max_temperature", "min_temperature"],
        labels={
            "reading_date": "Data",
            "value": "Temperatura (°C)",
            "variable": "Tipo de temperatura"
        }
    )

    fig_daily.for_each_trace(
        lambda trace: trace.update(
            name={
                "max_temperature": "Temperatura máxima",
                "min_temperature": "Temperatura mínima"
            }.get(trace.name, trace.name)
        )
    )

    # Exibe o gráfico no dashboard
    st.plotly_chart(fig_daily, use_container_width=True)



if __name__ == "__main__":
    main()
