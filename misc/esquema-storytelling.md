# Esquema storytelling

PRESENTACIÓN: 
- Quiénes somos: hemos hecho este proyecto, aquí tenéis nuestro enlace al Tableau y este es el link a nuestro repo.
- vamos a hablar del lado más humano de la energía (enlazar con lo siguiente).

## Introducción – La energía, compañera de nuestra evolución

Porque la energía está con nosotros desde que los primeros homínidos que aprendieron a dominar el fuego, la energía ha estado en el centro de nuestra evolución. No solo ha sido un recurso para sobrevivir: ha sido el motor del progreso. Cocinar, protegernos del frío, desarrollar herramientas… y siglos más tarde, dar luz a nuestras ciudades y alimentar nuestras industrias.

A lo largo de la historia, cada avance humano ha estado ligado a una nueva forma de generar energía.

Una anécdota curiosa ilustra bien esta relación:
A finales del siglo XIX, las grandes ciudades como Londres o Nueva York enfrentaban una crisis inesperada —el estiércol de caballo. El auge del transporte con carruajes trajo consigo toneladas de desechos diarios. Se decía que en pocos años las calles quedarían sepultadas en estiércol. ¿La solución? El automóvil, impulsado por un motor de combustión interna. Un invento pensado para resolver un problema… que, irónicamente, nos llevó a otro aún mayor: la dependencia de los combustibles fósiles y el impacto climático.

Hoy nos encontramos en una encrucijada similar por los combustibles fósiles, cómo han contribuido al efecto invernadero y al cambio climático.


## Links de interés para la presentación:
https://www.svgrepo.com/
https://slidesgo.com/es/


## Dashboard 0 introductorio:
- Exponer la historia introductoria expuesta al principio de este documento.
- Para que podáis seguir mejor nuestra exposición, nos gustaría comentaros las unidades con las que estamos trabajando. Hemos puesto un vídeo aquí por si queréis profundizar. 
- GWp: potencia máxima teórica que una fuente de energía puede generar bajo condiciones ideales.
- Por último, os preguntaréis, qué hace a la energía renovable: que ésta se produzca a un ritmo más alto del que se consume. Podríamos por ejemlo pensar que la madera es renovable, pero se necesita muhca madera para quemar y eerar energá Por eso la madera no es renovable.



## Dashboard 2: Energy consumption world
-  Desde que tenemos datos en los 90, ha ido aumentando el consumo de energía y hay proyección de que se siga aumentando en el futuro. Ejemplo claro, antes no podíamos estudiar a distancia de esta manera y el hecho de que nosotras estemos aquí en el Zoom, está consumiendo una energía que antes no era planteable.

La necesidad de energía sigue creciendo, pero ahora buscamos tecnologías sostenibles que nos permitan mantener este ritmo de consumo sin hipotecar el planeta. Y como comentado anteriormente, cada solución trae consigo nuevos desafíos.

Por ejemplo, la generación de energía solar o eólica depende de factores naturales —el sol, el viento— y su disponibilidad es limitada a ciertos momentos del día. De ahí la importancia de las baterías para el almacenamiento energético, que a su vez requieren materiales y procesos que también pueden impactar el medioambiente.

Este dashboard busca contar esa historia, visualizando el estado actual y la evolución de las energías renovables en el mundo.

`Explicar la visualización`. 
- Aunque en la actualidad, el % de energía renovable consumida sea más alto que antes, la mayoría de energías que se consumen vienen de fuentes de energía no renobables. 

- La energía tb te puede servir para estudiar la historia de la humanidad, por ejemplo, si nos fijamos en las bajadas de consumo en 2009 y 2020. Posibles causas de la disminución (`a analizar en el futuro`):

- `2009`:  La disminución podría deberse a una menor actividad económica, como consecuencia de la crisis. Fuentes:
    - [Fuente](https://elpais.com/economia/2009/12/30/actualidad/1262161977_850215.html#:~:text=El%20consumo%20de%20energ%C3%ADa%20el%C3%A9ctrica,publicado%20por%20la%20patronal%20Unesa.)

    - [Fuente](https://www.miteco.gob.es/content/dam/miteco/es/energia/files-1/balances/Balances/LibrosEnergia/Energia_2009.pdf)

- `2020`: La disminución podría estar condicionada por las diferentes medidas tomadas para contener la pandemia COVID-19.
    
    - [Fuente](https://www.ree.es/sites/default/files/publication/2022/05/downloadable/inf_sis_elec_ree_2020_0.pdf)



## Dashboard 3: mapa energía renovable 10 países

- Los países que tenemos representados en este Dashboard son aquellos que más energía renovable producen en el mundo. Nos apoyamos: (i) en la fuente de Kaggle del dataset, y (ii) se corrobora en la siguiente [Fuente] (https://www.ren21.net/reports/global-status-report/#).

- empezamos la total y abrimos el mapa:
    -  si sumas todos los tipos, China estaría en la cabeza (la que más produce). 


- cerrar el mapa: 
    - Si filtramos por tipo de energía: vemos que en eólica... en solar....
    - `Explicar cada energía según vayamos avanzando con el filtro`
    - explicar que estos filtros se puede mirar tb con el mapa.

- `tipos de energía`: 
    - hidráulica: energía generada al aprovechar el movimiento del agua. Este movimiento hace girar una turbina que, a su vez, energía eléctrica a través de un generador.
    - solar: Comentar que hay dos tecnologías, termosolar y fotovoltaica. La primera aprovecha el calor y la segunda la luz (resumiendo mucho)
    - viento: funciona de manera similar a la hidráulica, el viento mueve las aspas del molino que están conectadas a un rotor. El rotor está conectado a un generador eléctrico que convierte la energía mecánica en energía eléctrica.  
    - otras: biomasa, geotérmica, mareomotriz que no profundizaremos en este proyecto porque nos vamos a centrar en eólica y solar (hilamos con el siguiente).



## Dashboard 4: Profundizando en Eólica y Solar

- `¿Por qué nos hemos centrado eólica y solar?:` porque son las dos fuentes renovables con mayor proyección (las que más se han potenciado en los últimos años). 

**Objetivo**: En este Dashboard os vamos a mostrar cómo los países han evolucionado en estas dos energías.

- `Factor de capacidad`: El factor de capacidad es una medida que relaciona la energía real producida con la capacidad de generación máxima. Este factor es un indicador importante de la eficiencia y el rendimiento de la tecnología instalada.


- `Visualización`: gráfica de factor de capacidad de energía eólica y solar por país.

- Aquí podemos ver el factor de capacidad tanto para la eólica como para la solar: `abrir visualizaciones`. Dependerá mucho de las condiciones climatológicas y de las necesidades de cada país. Porque se puede tener mucha capacidad instalada pero poca `aprovechada`.

--> sólo China y España

    - `Solar`: Resaltamos los siguientes países:
        - Italia (analizar qué paso en 2007-- > caída de aprovechamiento, podría explorarse en más profundidad si en next steps). Mejoró a partir de 2008 y se mantiene, para estar en la vanguardia de energía solar. En eólica están bastante altos y se han mantenido.
        [Fuente](https://news.soliclima.com/noticias/energia-solar/la-energia-solar-en-italia) 
        - Corea del Sur (`analizar 2000 y 2001`). Tienen datos muy fuertes de solar. Han apostado fuerte por solar. En Viento tb están muy bien.
        - China: la mostramos para demostrar que España aprovecha lo mismo o incluso más que China (en lo solar). España está incluso más cerca que Corea del Sur.
        - España 

    - `Wind `:  Resaltamos:
        - España está en el top World. España ya había instalada energía eólica. Primer parque eólico en marcha en 1984.  
        - Nota: el orden de 2021 de capacidad de viento: China, USA, Alemania, Germany, India, Spain, UK, Brazil.


## Dashboards 4 y 5: Curiosidades:

1. `Wind & Solar`: Líderes en las sombras. Países con el mayor porcentaje de electricidad producido proveniente de eólica o solar

Storyhook: “¿Es posible ser pequeño y estar a la vanguardia renovable?”

- `Solar (% electricity)`: Países interesantes: Islas Cook, Namibia, Palestine, Yemen, El Salvador, Spain, USA, China.

Algunos países, como las Islas Cook (Polinesia dependiente de Nueva Zelanda, son 15 islas, pueden tener más facilidades), Namibia o Palestina, sorprenden por el alto porcentaje de electricidad solar en su mix energético, aunque su volumen total de electricidad producida sea bajo.

- `Namibia`:  Namibia tiene un enorme potencial para la producción de energía solar, ya que es el país más seco del continente africano, con un promedio de 10 horas diarias y 300 días de sol al año. Los datos del último censo indican que aproximadamente el 12% de los namibios utilizan soluciones fuera de la red, principalmente sistemas solares, para satisfacer sus necesidades de electricidad.
    [Fuente] (https://www.icex.es/es/quienes-somos/sala-de-prensa/sala-de-prensa/detalle.namibia-planta-solar.news056202003)
    [Fuente] (https://www.namibian.com.na/solar-energy-usage-lagging-in-sun-rich-namibia/#:~:text=Despite%20being%20ranked%20as%20having,300%20days%20of%20sunshine%20annually.)



- `Wind (% electricity)`: Países interesantes: Falkland Islands, Denmark, Lithuania, Urugay, Ireland, Spain, China, USA. Los países curiosos probablemente sean tan potentes debido a factores climatológicos y geográficos.

    - `Islas Malvinas (Falkland)`: quieren llegar al 100% de fuente renovables en 2045. Fueron colonia inglesa y ahora forman parte de Argentina. Se encuentran al sur, muy cerca de Patagonia, al lado del Tierra del Fuego (Argentina).
    [Fuente] (https://www.falklands.gov.fk/policy/downloads?task=download.send&id=215:fi-energy-strategy&catid=11)

    - `Dinamarca`: quieren llegar al 100% de fuente renovables en 2030 y tener el 60% de la energía generada ques sea eólica. Ahora mismo están en un 50%, parece que pueden conseguirlo si siguen así.
    [Fuente] (https://www.construction21.org/articles/h/denmark.html#:~:text=By%202030%2C%20Denmark%20plans%20to,energy%20generated%20by%20wind%20power.&text=While%20wind%20power%20plays%20an,solar%20energy%20and%20geothermal%20energy.)



2. `PIB vs Renovables`:

- Explicar medidas y termómetro:
    - Mencionar que utilizamos PIB per capita y no pib global. Hacer hincapié en que el total de lo producido (la riqueza) por un país se divide entre el total de habitantes. Por eso China tiene un PIB per cápita tan pequeño (por debajo de España).
    
    - Hemos puesto los percentiles como referencia: claramente la riqueza no está bien repartida. La riqueza se concentra en el percentil 75. 

    - Orden termómetro: Los países que hemos puesto como referencia
        - menos PIB per capita: Yemen
        - más PIB per capita: Mónaco, Licheinstein, Luxemburgo
        - España: por encima del percentil 75
        - China entre el percentil 75 y 50%. Lo hemos seleccionado para tener una referencia porque tiene muchos habitantes.
    
    - Visualización: Explicar la gráfica de correlación. Dejar claro que el año no tiene que corresponder con el mayor PIB, porque estamos viendo una correlación entre PIB y % energía producida.

- `¿qué queremos contar con este Dashboard?` ¿Es la transición energética también una cuestión económica?”

Casos llamativos: 
- Por lo general, según aumenta PIB, aumenta también la producción con fuente de energía eólica y solar. Casos muy claros:
    - India, China, USA, Germany, Italia (generalmente)
    - China y USA : aunque haya aumentado el % de renovables, realmente no tiene efectos relevantes a nivel absoluto, porque el porcentaje sobre el total de electricidad producida es muy poca, como podéis ver == CASO de USA VS ESPAÑA

- Ejemplo claro de `país con alto PIB pero bajo % de mix energético en eólica y solar`:
    - USA

- Uno con `bajo PIB y un alto % de electricidad solar/eólica`:
    - Marruecos: está dentro del percentil 10%. Tiene un 12% de viento y un 4% solar (probablemente solar se podría aprovechar más).

- España: vemos que está super bien, porque tiene en solar en torno al 10% y en viento sobrepasa los 20% (muy por encima del resto).

- No siguen la tendencia: 
    - Grecia: independiendemente de su PIB, ha seguido invirtiendo. Su pib ha bajado mucho en los últimos años. 


`Cierre reflexivo`
- Los datos nos muestran que aunque el PIB ayuda mucho no es el único factor o no es el factor clave de esta transición que estamos estudiando.

- Los últimos años la tecnología fotocoltaica se ha hecho mucho más efiicente y accesible y en cualquier caso parece que sí es determinante es que tiene que haber un compromiso firme de los gobernantes para que esta transición se produzca.



## Next steps:
1. En el “energy consumption word” ver correlation de la energía con:
    - 2020: coronavirus
    - 2009: crisis 2008

2. Añadir factores demográficos(relación de estas medidas con la superficie de cada país).

3. ¿en qué se consume principalmente la energía renovable vs no renovable? 

4. Estudiar la caída de Italia en el aprovechamiento de energía en 2007
