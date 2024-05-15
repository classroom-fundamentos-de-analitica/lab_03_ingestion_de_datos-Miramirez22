"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re


def ingest_data():

    data = []
    with open('clusters_report.txt', 'r') as f:
        for line in f: #Organizar el nombre de las columnas correctamente
            line = line.strip()
            if re.match(r'^\d+', line):
                parts = re.split(r'\s{2,}', line)
                cluster = parts[0]
                num_keywords = parts[1]
                percent_keywords = parts[2]
                keywords = parts[3] if len(parts) > 3 else ''
                data.append([cluster, num_keywords, percent_keywords, keywords])
            elif data:
                data[-1][3] += ' ' + line

    df = pd.DataFrame(data, columns=['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])

    df['principales_palabras_clave'] = df['principales_palabras_clave'].apply(lambda x: ', '.join(re.split(r'\s{2,}|,', x)))

    return df


ingest_data()