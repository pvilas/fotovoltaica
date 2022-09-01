# pasar los csv de endesa o energiaXXI a la base de datos
# atención: quitar las cabeceras de los csv antes de usar este script,
# para las lineas en blanco no hay problema

import pandas as pd
import numpy as np
import tablib

# periodos de facturación
periodes_facturacio={
    "Punta": { "tramos": [(10, 14), (18, 22)], "consumo": 0, "num_horas": 0, "precio": 0},
    "Llano": { "tramos": [(8, 10), (14, 18), (22, 24)], "consumo": 0, "num_horas": 0, "precio": 0},
    "Valle": { "tramos": [(0, 8)], "consumo": 0,  "num_horas": 0, "precio": 0}
}


print('Iniciando análisis de datos')
# Fecha  , Hora  , Consumo (Wh) , Precio (€/kWh) , Coste por hora (€)
df = pd.read_csv('datos.csv', 
                 names=["fecha", "hora", "consumo", "precio", "coste-hora"],
                 dtype={"fecha": object, "hora": "Int64", "consumo": "Int64", "precio": np.float64, "coste-hora": np.float64},
                 parse_dates=["fecha"],) 
#df.columns=["fecha", "hora", "consumo", "precio", "coste-hora"]
#df.dtype={"fecha": object, "hora": "Int64", "consumo": "Int64", "precio": np.float64, "coste-hora": np.float64}
print(f'Datos cargados: {df.shape[0]} filas, {df.shape[1]} columnas')
# print(df.info())

# print(df.head()) 

desde=df.fecha.min()
fins=df.fecha.max()
dias=df.fecha.nunique()
fileres=df.shape[0]

print(f'\nConsumos desde {desde:%Y-%m-%d} hasta {fins:%Y-%m-%d} ({dias}) días.')
#print("-"*80)


hores=df.groupby(["hora"]).sum() # suma de consums per hora
preus=df.groupby(["hora"]).mean() # mitja de preus per hora


total_consumo=hores.consumo.sum()
total_coste=hores["coste-hora"].sum()


# feim uns slices segons els periodes de facturació
for period in periodes_facturacio.keys():
    for tramo in periodes_facturacio[period]["tramos"]:
        inicio_tramo=tramo[0]
        fin_tramo=tramo[1]-1
        num_horas=fin_tramo-inicio_tramo+1 # nombre d'hores del tram
        # print(f"{period} {tramo} indice ({inicio_tramo}:{fin_tramo}) num_horas: {num_horas}")
        tr=hores[inicio_tramo:fin_tramo+1]
        # print(f'{tr}')
        # acumulam el consum del tram
        periodes_facturacio[period]["consumo"]=periodes_facturacio[period]["consumo"]+tr.consumo.sum()
        tp=preus[inicio_tramo:fin_tramo+1] # preus del tram
        periodes_facturacio[period]["precio"]=periodes_facturacio[period]["precio"]+tp.precio.sum()
        periodes_facturacio[period]["num_horas"]=periodes_facturacio[period]["num_horas"]+num_horas
        # print(f'Total tramo {tramo}: {tr.consumo.sum()}')
        # print('\n')

# print(f"Períodos de facturación: {periodes_facturacio}\n")


# preparam dades per pantalla
data=tablib.Dataset(headers=["Tarifa", "Consumo (kWh)", "Proporción (%)", "Precio medio (€/kWh)"])

for period in periodes_facturacio.keys():
    data.append([period,
                f"{periodes_facturacio[period]['consumo']/1000:.0f}",
                f"{periodes_facturacio[period]['consumo']*100/total_consumo:.0f}",
                f"{periodes_facturacio[period]['precio']/periodes_facturacio[period]['num_horas']:.4f}"
    ])
print(data)
print(f'\nTotal consumo periodo: {total_consumo/1000} kWh')
