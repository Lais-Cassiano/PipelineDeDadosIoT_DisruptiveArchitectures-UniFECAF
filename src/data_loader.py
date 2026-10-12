import pandas as pd

def load_csv_data(file_path="data/IOT-temp.csv"):
    # Leitura do arquivo usando pandas
    data = pd.read_csv(file_path)

    return data
