# fotovoltaica

Con el cuaderno es posible calcular, en media horaria, los consumos y la producción de una instalación fotovoltaica.

Los consumos se obtienen de las páginas de endesa o energiaxxi. Las producciones, de la base de datos de radiación de EU-PVGIS.


## Carga de datos de consumo de endesa y energiaxxi

Hay que ir a la página de Clientes->Mi Consumo, escoger un periodo, vista por factura y guardar como hoja de cálculo, escoger formato csv y guardar el fichero.

Ahora abrirlo y quitar la cabecera y el pie de página, y guardar como datos.csv. Vamos bajando datos de diferentes periodos y los añadimos (copiar-pegar) a este fichero.

O sea, que sólo escogemos las líneas de tipo 

```csv
2022-04-21 , 1.0 , 86.0 , 0.200677395 , 0.01725825597
```

Los campos corresponden a 

```Fecha  , Hora  , Consumo (Wh) , Precio (€/kWh) , Coste por hora (€)```

Una vez tenemos el periodo del que deseamos hacer la simulación, copiamos esos datos en el portapapeles y los copiamos en el cuanderno, en el apartado *Datos*, conservando las tres comillas del inicio y del final. No incluir las cabeceras.

## Parámetros de la instalación

Una vez tenemos cargados los datos de consumo, parametrizamos la instalación con los siguientes datos:

- lat: Latitude of the location
- lon: Longitude of the location
- name: Name of the panel location on the object
- tilt: Tilt of the solar panels (0 is flat, 90 is standing straight)
- azimuth: Direction the panels, 0 is South, negative from south to east, - positive from south to west
- panels: Number of panels on the location
- peakpower: Peakpower per panel (in kW)

La longitud y latitud se puede sacar del google maps. Hay que poner todos los decimales.

La fecha de inicio y final la toma del mínimo y máximo de los datos de consumo.

> Atención: La base de datos pvgis sólo llega hasta 2020. Hemos tomado los datos de radiación de este año como base para la comparación con el consumo de cualquier año.

## Cálculo y obtención de la gráfica

Una vez tenemos los datos introducidos, hacemos `run all` (Cmd/Ctrl+F9) para generar la gráfica que lucirá algo como

![Ejemplo de gráfica de cosumo y producción]()
