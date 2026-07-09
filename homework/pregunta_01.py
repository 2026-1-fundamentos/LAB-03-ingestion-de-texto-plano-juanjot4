"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""



import pandas as pd
file = pd.read_fwf("files/input/clusters_report.txt", widths=[9, 16, 16, 80], names=["Cluster", "Cantidad de palabras clave", "Porcentaje de palabras clave", "Principales palabras clave"], skiprows=4)

def pregunta_01():

    lista = []
    cluster = None

    for _, row in file.iterrows():

        if pd.notna(row[ "Cluster" ]):
            if cluster:
                lista.append(cluster)

            cluster = {
                "Cluster": int( row[ "Cluster" ] ),

                "Cantidad de palabras clave": int( row[ "Cantidad de palabras clave" ] ),

                "Porcentaje de palabras clave": float( row[ "Porcentaje de palabras clave" ].replace('%', '').replace(',', '.') ),

                "Principales palabras clave": row[ "Principales palabras clave" ]
            }
        
        else:
            cluster[ "Principales palabras clave" ]  += " "  +  row[ "Principales palabras clave" ].strip()

    if cluster:
        lista.append(cluster)
        
    data = pd.DataFrame(lista)

    data.columns = data.columns.map(lambda x: x.lower(). replace(" ", "_"))

    data["principales_palabras_clave"] = (
        data["principales_palabras_clave"].str.replace(r'\s+', ' ', regex=True).str.strip().str.replace(r'\s*,\s*', ', ').str.replace(".", "")
        )

    return data


    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
