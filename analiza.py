# pasar los csv de endesa o energiaXXI a la base de datos
# atención: quitar las cabeceras de los csv antes de usar este script,
# para las lineas en blanco no hay problema

import pandas as pd
import numpy as np

print('Iniciando análisis de datos')
# Fecha  , Hora  , Consumo (Wh) , Precio (€/kWh) , Coste por hora (€)
df = pd.read_csv('datos.csv', 
                 names=["fecha", "hora", "consumo", "precio", "coste-hora"],
                 dtype={"fecha": object, "hora": "Int64", "consumo": "Int64", "precio": np.float64, "coste-hora": np.float64},
                 parse_dates=["fecha"],) 
#df.columns=["fecha", "hora", "consumo", "precio", "coste-hora"]
#df.dtype={"fecha": object, "hora": "Int64", "consumo": "Int64", "precio": np.float64, "coste-hora": np.float64}
print(f'Datos cargados: {df.shape[0]} filas, {df.shape[1]} columnas')
print(df.info())

print(df.head()) 