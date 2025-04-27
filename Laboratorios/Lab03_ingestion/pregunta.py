"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""

import pandas as pd
from datetime import datetime
import re


def clean_data():
    def format_date(fecha_str):
        try:
            fecha = datetime.strptime(fecha_str, "%Y/%m/%d")
        except:
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        return fecha

    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    df.drop(df.columns[0], axis=1, inplace=True)
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    df = df.apply(lambda x: x.str.lower() if x.dtype == "object" else x)
    df["idea_negocio"] = df["idea_negocio"].str.replace(r"[ -_]+", " ", regex=True)
    df["barrio"] = df["barrio"].map(lambda x: re.sub(r"-", " ", str(x)))
    df["barrio"] = df["barrio"].map(lambda x: re.sub(r"\s", "_", str(x)))
    # df["barrio"] = df["barrio"].str.replace(r"[_]", " ", regex=True)
    # df["barrio"] = df["barrio"].str.replace("nari¿o", "nariño")
    # df["barrio"] = df["barrio"].str.replace("bel¿n", "belen")
    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)
    df["monto_del_credito"] = df["monto_del_credito"].str.replace(
        r"[ $,]+", "", regex=True
    )
    df["monto_del_credito"] = df["monto_del_credito"].str.replace(
        r"(\.00)", "", regex=True
    )
    df["monto_del_credito"] = df["monto_del_credito"].astype(float)
    df["línea_credito"] = df["línea_credito"].str.replace(r"[-_. ]+", " ", regex=True)
    df["fecha_de_beneficio"] = df["fecha_de_beneficio"].apply(format_date)
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    df.drop_duplicates(inplace=True)

    return df
