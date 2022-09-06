# Fotovoltaica

Con el cuaderno Jupyter adjunto es posible calcular, en media horaria, los consumos y la producción de una instalación fotovoltaica.

Los consumos se obtienen de las páginas de endesa o energiaxxi. Las producciones, de la base de datos de radiación de EU-PVGIS.

Ver el vídeo de [youtube](https://www.youtube.com/watch?v=IwvNvcPrDFc).


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

![Ejemplo de gráfica de cosumo y producción](https://github.com/pvilas/fotovoltaica/blob/main/prod-consumo.png)

## Interpretación de la gráfica

En el ejemplo (vivienda) se observa que el consumo y la producción no coinciden.

La producción es nula en las horas nocturnas, mientras que el consumo es de unos 190Wh. A partir de las 6 de la mañana, el consumo se eleva a la vez que la producción. El primer momento en cuál la producción sobrepasa al consumo es a partir de las 08h. Desde este momento hasta las 17h, se produce mucho más de lo que se consume. La diferencia entre ambas gráficas es el excedente que eventualmente puede inyectarse en la red. Las horas de mayor consumo se encuentran precisamente a partir de las 18h, cuando la producción ya es nula otra vez.

Una posible forma de que la instalación resultara rentable sería mediante un posible cambio de hábito de consumo, trasladando en lo posible en pico de las 21h dentro del horario de producción. Este pico puede corresponder a la preparación de la cena en la vitrocerámica, lavadoras, secadora, etc. Así mismo se observan consumos de 190Wh de 01 a 06 horas que posiblemente se deban a algún electrodoméstico que está consumiendo. Sólo en el caso de que ambas medidas fueran posibles, resultaría racional realizar la instalación.

## Recursos

PVGIS Photovoltaic Geographical Information System

> European Commission. [PVGIS](https://joint-research-centre.ec.europa.eu/pvgis-photovoltaic-geographical-information-system_en)


Librería pvlib
> William F. Holmgren, Clifford W. Hansen, and Mark A. Mikofski. “pvlib python: a python package for modeling solar energy systems.” Journal of Open Source Software, 3(29), 884, (2018). https://doi.org/10.21105/joss.00884

The power project

> NASA. [https://power.larc.nasa.gov/](https://power.larc.nasa.gov/)

Solar panel power generation analysis

> Leo van der Meulen. "How much energy will you be able to generate with your solar panels? Make your own calculations to stay in control" Medium. [https://towardsdatascience.com/solar-panel-power-generation-analysis-7011cc078900](https://towardsdatascience.com/solar-panel-power-generation-analysis-7011cc078900)

Shadow Calculator

> KameoCode. "Sun position calculator on google maps.
Predict size of shadows at different times of the day for google maps location." [http://shadowcalculator.eu/](http://shadowcalculator.eu/)
