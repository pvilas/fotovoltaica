# fotovoltaica
Cosas varias para trabajar con fotovoltaica


## Carga de datos de endesa y energiaxxi

Hay que ir a la página de Clientes->Mi Consumo, escoger un periodo, vista por factura y guardar como hoja de cálculo, escoger formato csv y guardar el fichero.

Ahora abrirlo y quitar la cabecera y el pie de página, y guardar como datos.csv. Vamos bajando datos de diferentes periodos y los añadimos (copiar-pegar) a este fichero.

O sea, que sólo escogemos las líneas de tipo 

```csv
2022-04-21 , 1.0 , 86.0 , 0.200677395 , 0.01725825597
```

Los campos son

```Fecha  , Hora  , Consumo (Wh) , Precio (€/kWh) , Coste por hora (€)```


