**CIENCIA DE DATOS \- Semana 1**

OBJETIVO

El objetivo de la ciencia de datos es **mejorar la toma de decisiones** en base a grandes estructuras de datos.

ECOSISTEMA

**Recopilación de datos:**

* Datos transaccionales: órdenes de compra, recibos, etc.  
* almacenamiento en BD, primero relacionales y después no relacionales  
* Big Data: Volúmenes imposibles de procesar con métodos tradicionales  
* Map Reduce: Procesamiento de datos paralelo y distribuido

**Análisis de datos:**

* Estadística de datos: Tendencias, regresiones  
* Análisis discriminatorio: Clasificación por reconocimiento de patrones  
* Machine learning: Aprender de los datos en lugar de la programación explícita  
* Deep learning: Redes neuronales

ROLES CLAVE

* **Ingeniero de datos:** Recopilan, almacenan y estructuran la información, crean interfaces para poder visualizarlos.  
* **Analista de datos:** Visualizan, analizan y consultan la información para dar ideas y crear informes, crean gráficas y estadísticas.  
* **Científico de datos:** Exploran, pre-procesan, limpian y transforman la información, crean modelos predictivos.  
* **Business Intelligence:** Analista que descubre nuevas oportunidades de negocio.

METODOLOGÍAS: KDD, SEMMA, TDSP y CRISP-DM

CRISP-DM

1. **Business understanding:** comprender las necesidades del cliente  
2. **Data understanding:** Identificar, recopilar y analizar los conjuntos de datos  
3. **Data preparation:** Prepara los conjuntos de datos para el modelado  
4. **Modeling:** Construir y evaluar varios modelos de datos empleando diferentes técnicas  
5. **Evaluation:** Analizar qué modelo se adapta mejor al negocio  
6. **Deployment:** Generar reportes y mandar el modelo a producción.

ESTRATEGIA DE NEGOCIOS

* **Preguntas descriptivas:** ¿Cómo son las cosas?  
* **Preguntas predictivas:** ¿Cómo creemos que serán las cosas?  
* **Preguntas prescriptivas:** ¿Cómo deberían ser las cosas?

**INGENIERÍA DE DATOS \- Semana 2**

La ingeniería de datos es un conjunto de operaciones destinadas a crear interfaces y mecanismos para el flujo y acceso a la información.

**Ingenieros de datos:** Mantienen los datos de modo que permanezcan disponibles y utilizables por otros.

**Ciclo de vida:**

* Generación (¿cómo se crean los datos?)  
* Almacenamiento (elegir la arquitectura de datos adecuada según los casos de uso)  
* Ingestión (es el proceso de mover datos de un lugar a otro)  
* Transformación (convertir los datos sin procesar en consumibles para las partes interesadas)  
* Servicio (para aplicaciones de analítica y machine learning)

Y tiene el soporte de otras disciplinas que incluyen seguridad, gestión de datos, DataOps, arquitectura de datos, orquestación e ingeniería de software.

**Pandas:** Es un módulo de python para trabajar con datos. Y su principal estructura de datos son los DataFrames.

**DataFrames:** Son estructuras de datos bidimensionales. Each DataFrame carries two types of index: default indices or assigned indices.

**Default index \- loc\[\]:** Es el indice por default, se puede cambiar con la funcion **.set\_index()**

**Assigned index \- iloc\[\]:** Es el índice interno que maneja python, inmutable.

**5 PASOS PARA CONOCER EL DATASET**

It is good practice to always get to know the dataset you are about to work on.

1. Understand each attribute of the dataset.  
2. Check the shape of the dataset. How many rows and columns does the dataset have? This one is easy. For instance, just try **adult\_df.shape** and review the result.  
3. Check whether the data has any missing values.  
4. Calculate summarizing values for numerical attributes such as mean, median, and standard deviation, and compute all the possible values for categorical attributes.  
5. Visualize the attributes. For numerical attributes, use a histogram or a boxplot, and for categorical ones, use a bar chart.

**DESVENTAJA CÓDIGO VS EXCEL**

One of the disadvantages of data manipulations using programming instead of spreadsheet software such as Excel is that you cannot scroll through the data as you would in Excel.

**PROPIEDADES PARA EXPLORAR LA ESTRUCTURA DE LOS DATOS**

**.shape** is the property of any Pandas DataFrame. It tells you how many rows and columns the DataFrame has. 

**.columns** allows you to see and edit the column names in your DataFrame.

#### **.info()** This function provides information about both the shape and the columns of the DataFrame.

**TYPES OF COLUMNS \- NUMERICAL**

#### **.describe()** This function outputs many useful statistical metrics that are meant to summarize data for each column. These metrics include Count, Mean, Standard Deviation (std), Minimum (min), first quartile (25%), second quartile (50%) or median, third quartile (75%), and Maximum (max).

**plot.hist()** Histograms and boxplots to visualize numerical columns

**plot.bar()** muestra una gráfica de barras, pero se deben calulcular los datos primero con value\_counts()

**TYPES OF COLUMNS \- CATEGORICAL**

**.unique()** It simply returns all the possible values of the columns.

**.value\_counts()** how often each possibility happens

**.value\_counts(normalize=True)** Para mostrar el ratio en lugar del número de veces

**FUNCTIONS**

In order to apply a function we use the **apply()** function. 

Cuando aplicamos una función a todo el DataFrame, debemos pasar un segundo argumento en apply() para especificar si queremos aplicar la función en cada columna (**axis=0**) o a todas la celda (**axis=1**).

**Lambda function** is a function that is expressed in one line. So, a lot of the time, applying a lambda function may make coding easier and perhaps help our code become a bit more readable at times.

**MULTI LEVEL INDEXING**

Es el índice que discrepa debido al agrupamiento de dos o más columnas.

**unstack()** saca el índice multinivel hacia una columna, se puede aplicar varias veces para varios multiniveles.

**stack()** es el contrario, mete las columnas hacia un nivel de índice.

**SWITCH BETWEEN DATA STRUCTURE FORMS**

**.melt()** transforms from wide to long form, it requires four inputs:

* **id\_vars:** This input takes the identifying columns.  
* **value\_vars:** This input takes the columns that hold the values.  
* **var\_name:** This input takes the name you would like to give to the identifying column that will be added to the long format.  
* **value\_name:** This input takes the name you would like to give to the new value column that will be added to the long format.

**.pivot()** transforms from long to wide form, needs three inputs:

* **index:** This input takes what will be the index of the wide form.  
* **columns:** This input takes the columns of the long form that will be expanded to create the columns for the wide form.  
* **values:** This input takes the column in which the long form keeps the values.

**CARGANDO ARCHIVOS**

Se pueden cargar archivos desde múltiples formatos, siendo el más común el separado por comas (csv), pero hay muchos más (ver lista). Cuando hay datos faltantes en un archivo se usan centinelas (null, NA, etc), y hay operaciones para reemplazar esos datos faltantes.

Ejemplo para reemplazar valores faltantes:

pd.read\_csv("examples/ex5.csv", na\_values=\["NULL"\])

Ejemplo con centinelas:

sentinels \= {"message": \["foo", "NA"\], "something": \["two"\]}  
pd.read\_csv("examples/ex5.csv", na\_values=sentinels, keep\_default\_na=False)

Para desplegar solo X Líneas de un archivo bastante grande.

pd.options.display.max\_rows \= 10

Para cargar un archivo en formato JSON, se puede usar la librería json:

import json  
json.loads(obj)

Para convertir un objeto de Python a JSON:

json.dumps(pythonObj)

**SQL Y BASES DE DATOS CON PANDA \- SEMANA 3**

Para imprimir/mostrar varios DataFrames:

display('df1', 'df2')

Para combinar dos Data Frames en uno:

df3 \= pd.merge(df1, df2)

La función merge() busca las columnas que coincidan en ambos DataFrames (columnas clave). Para explicitamente especificar la columna clave podemos usar “on”:

pd.merge(df1, df2, on=’nombre\_de\_la\_columna’)

Ambos DataFrames deben de tener el mismo nombre de la columna.

Cuando los nombres de las columnas difieren entre si, usar **“left\_on**” y “**right\_on**”:

pd.merge(df1, df2, left\_on=”employee”, right\_on=”name”)

Ambas columnas se integran al nuevo Data Frame, para eliminar una columna redundante:

pd.merge(df1, df2, left\_on=”employee”, right\_on=”name”).drop(“name”, axis=1)

Para unir Data Frames por medio de su índice:

pd.merge(df1, df2, left\_index=True, right\_index=True)

Lo anterior es lo mismo que hace la función **join()**:

df1.join(df2)

Para mezclar índices y columnas, podemos combinar “left\_index” con “right\_on”, o incluso “left\_on” con “right\_index”:

pd.merge(df1, df2, left\_index=True, right\_on=”name”)

**RELACIONES EN PANDA**

**One-To-One:** En donde ninguna de las columnas clave tiene duplicados

**Many-To-One:** En donde una de las columnas clave contiene duplicados

**Many-To-Many:** En donde ambas columnas clave contienen duplicados

**JOINS EN PANDA**

**Inner join:** Es la intersección de dos conjuntos de entradas, y se expresa usando “how”:

pd.merge(df1, df2, how=”inner”)

**Outer join:** Es la unión de dos conjuntos, que muestra todos los valores faltantes de ambos conjuntos con “NaN”:

pd.merge(df1, df2, how=”outer)

**Left join:** Es la unión de los conjuntos, que muestra todos los valores de la izquierda, y los faltantes de la derecha:

pd.merge(df1, df2, how=”left”)

**Right join:** Es la unión de los conjuntos, que muestra todos los valores de la derecha, y los faltantes de la izquierda:

pd.merge(df1, df2, how=”right”)

Para saber si existen valores faltantes en una columna del Data Frame (df):

df.isnull().any()

Para filtrar datos se puede usar la función query():

women2010 \= df.query(“year \== 2010 & gender \== ‘females’”)

**VISUALIZACIÓN Y PLOTTING \- SEMANA 4**

**MATPLOTLIB**

Para crear una nueva figura

fig \= plt.figure()

Para crear un plot se necesitan agregar subplots con “add\_subplot()”, pasando 3 parámetros para las filas, columnas y el índice, por ejemplo:

ax \= fig.add\_subplot(2,2,1)

Una forma más fácil de crear la figura y los subplots en el mismo comando

fig, ax \= plt.subplots()

Para definir los “ticks” del eje de las Xs

ticks \= ax.set\_xticks(\[0, 500, 1000\])

Para cambiar las etiquetas de los “ticks”

labels \= ax.set\_xticklabels(\["one", "two", "three"\], rotation=30, fontsize=8)

Para agregar una leyenda en el eje de las Xs

ax.set\_xlabel("Stages")

Para agregar un título

ax.set\_title("My first matplotlib plot")

Para guardar los plots en un archivo PNG/PDF/SVG con resolución de 400 DPI

fig.savefig(“figpath.png”, dpi=400)

**PREPROCESAMIENTO DE DATOS \- SEMANA 5**

**TIPOS DE DATOS**

Enteros (int), De pronto flotante (float), Objetos (object)

**ESCALAS DE MEDICIÓN**

**Cualitativas:** Representan categorías o atributos

* Nominales: No hay orden en las clases  
* Ordinales: Cada categoría es más alta o mejor que la anterior

**Cuantitativas:**

* Discretas: Suelen tomar valores enteros  
* Continuas: Puede haber valores intermedios entre dos valores

**CURTOSIS**

df.\[value\].kurt()

* Mesocúrtica: Si el valor de la curtosis es aproximadamente 0\.  
* Leptocúrtica: Si el valor de la curtosis es mayor que 0\.  
* Platicúrtica: Si el valor de la curtosis es menor que 0\.

**FALTA DE DATOS**

Cuando faltan datos, ciertos algoritmos no funcionan. Incluso para algoritmos que manejan datos faltantes, sin tratamiento, el modelo puede llevar a una conclusión inexacta.

* **MCAR:** Falta completamente al azar (Missing Completely At Random), ej. encuestas. Los resultados del análisis permanecen imparciales.  
* **MAR:** Falta al azar (Missing At Random), ej. peso en las mujeres. En la mayoría de los casos no representa un problema, así que no está sesgado.  
* **MNCAR:** Falta no al azar (Missing Not at Random), ej. salario de una persona. El manejo incorrecto de estos datos puede generar un fuerte sesgo en los resultados.

**df.info()** detecta los valores faltantes en el data frame, así como el número de filas, columnas, tipo de datos y la memoria usada.

**df.isnan().sum()** regresa una lista de los valores faltantes por cada columna del data frame.

**PRUEBA DE HIPÓTESIS**

p-value: Es la probabilidad de observar las muestras dadas bajo el supuesto de la hipótesis nula

Nivel de significancia: Es el umbral de la cantidad de casualidad (azar) que estamos dispuestos a aceptar. se fija antes de la prueba y el valor común es 0.05 (5%).

**Cómo definir una prueba de hipótesis:**

1. Definir la pregunta, determinando si hay variables relacionadas con la falta de valores en otra variable (MAR)  
2. Establecer hipótesis nula e hipótesis alternativa  
3. Reunir muestras de datos: con valores faltantes y sin valores faltantes  
4. Calcular el p-value  
5. Definir el nivel de significancia  
6. Llegar a una conclusión comparando p-value vs nivel de significancia

**VALORES ATÍPICOS**

Es un valor que se desvía de los otros. Su presencia puede hacer que el algoritmo no funcione correctamente. Se pueden identificar:

* Basándose en límites arbitrarios (requiere entendimiento del negocio).  
* Con la media y la desviación estándar  
* La regla de los rangos intercuartílicos IQR

**ALTA CARDINALIDAD**

Es el número de veces que una variable se repite. El problema es que las variables con alta cardinalidad tienden a dominar sobre aquellas con baja cardinalidad.

También pueden introducir ruido con poca o ninguna información, lo que hace que los modelos de aprendizaje automático sean propensos a sobre ajustarse.

**¿Cómo lidiar con la alta cardinalidad?**

Agrupación de categorías: Por ejemplo, en lugar de agrupar por país, agrupar por región.

Agrupación de categorías con poca ocurrencia en una categoría única: Por ejemplo, enfermedades con poca frecuencia, podrían agruparse en la categoría “Otras”.

**INGENIERÍA DE CARACTERISTICAS \- SEMANA 6**

En inglés Feature Engineering, es convertir observaciones sin procesar en características deseadas para un modelado más preciso.

## **Clean the Data**

Most machine learning algorithms cannot work with missing values, so you’ll need to take care of these. You have three options to fix this:

Get rid of the corresponding districts.

housing.dropna(subset=\["total\_bedrooms"\], inplace=True)

Get rid of the whole attribute.

housing.drop("total\_bedrooms", axis=1)

Set the missing values to some value (zero, the mean, the median, etc.).  
This is called imputation.

	median \= housing\["total\_bedrooms"\].median()  
housing\["total\_bedrooms"\].fillna(median, inplace=True)

**REGRESIÓN LOGÍSTICA \- SEMANA 9**

**Matriz de confusión**

La primera letra es el resultado (símbolo). La segunda letra es lo que se predijo (círculo).

Una forma común de evaluar estas cuatro cantidades juntas es usar una matriz de confusión. Los valores reales se agrupan por fila y los valores predichos se agrupan por columna.

Estas cuatro cantidades forman la base de todos los métodos de evaluación de clasificación. Las tres métricas clave: **recall, precision y accuracy** se pueden calcular desde aquí.

**Recall (Sensibilidad)** te dice qué parte de una clase determinada se identifica correctamente mediante un modelo. Es decir, establece la relación entre los datos correctamente clasificados como positivos (VP) y los datos positivos totales.

![][image1]

**Precision (Precisión)** representa la fracción de clasificaciones de una clase determinada que fueron correctas, que es la relación entre los datos positivos clasificados correctamente (VP) y el total de datos clasificados como positivos.

![][image2]

**Accuracy (Exactitud)** es la tasa general en la que un modelo clasifica correctamente los datos. Es la fracción de todas las predicciones correctas (VP \+ VN) y el total de todas las predicciones. En otras palabras, la frecuencia con la que el modelo acertó en sus predicciones en general.

![][image3]

**Ejemplo de clasificación para evaluar si una persona tiene cáncer.**

FN: Se predice que una persona NO tiene cáncer (negativo), cuando en realidad si lo tiene (negativo es falso). 

FP: Se predice que una persona SI tiene cáncer (positivo), cuando en realidad no lo tiene (positivo es falso).

VP: Se predice que una persona SI tiene cáncer (positivo), y es correcto (positivo es verdadero).

VN: Se predice que una persona NO tiene cáncer (negativo), y es correcto (negativo es verdadero).

Ya que FN es el problema más grave, nos interesa minimizarlo. Para ello se elige la métrica que evalúa los falsos negativos: **Recall.**

**Ejemplo de clasificación para evaluar si se otorga un crédito bancario**

FN: Se predice que NO pagará el préstamo (negativo), cuando en realidad si lo pagara (negativo es falso).

FP: Se predice que SI lo pagará (positivo), cuando en realidad no lo pagará (positivo es falso).

VP: Se predice que SI lo pagara (positivo), y es correcto (positivo es verdadero).

VN: Se predice que NO lo pagará (negativo), y es correcto (negativo es verdadero).

El escenario en donde nos interesa tener menos errores es el de FP, y la métrica que evalúa FP es: **Precisión.**

[image1]: <data:image/png;base64,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>

[image2]: <data:image/png;base64,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>

[image3]: <data:image/png;base64,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>