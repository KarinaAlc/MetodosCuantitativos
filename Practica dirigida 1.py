# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 13:38:28 2025

@author: ariaf
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 13:07:58 2025

@author: ariaf
"""

"""
Práctica dirigida 1

FACULTAD DE CIENCIAS SOCIALES - PUCP
1REI45 - MÉTODOS CUANTITATIVOS EN CIENCIAS SOCIALES

1. ¿Qué es Python?

Python es un lenguaje de programación de alto nivel, fácil de leer y escribir, 
que ejecuta instrucciones línea por línea mediante un intérprete escrito en C. 
Es de código abierto, versátil y ampliamente utilizado en áreas como análisis 
de datos, estadística, automatización, inteligencia artificial y desarrollo web.


2. ¿Qué es Spyder?

Spyder (Scientific Python Development Environment) es un entorno de 
desarrollo integrado (IDE) especializado en análisis de datos y 
programación científica en Python.

Incluye:
    
- Editor de código con resaltado de sintaxis y autocompletado.
- Consola interactiva para ejecutar comandos en tiempo real.
- Explorador de variables para visualizar y gestionar datos.
- Paneles de ayuda y documentación integrada.


3. ¿Por qué usamos Spyder para programar en Python?

Aunque Python puede escribirse en cualquier editor y ejecutarse desde la línea 
de comandos, el uso de un IDE o editor avanzado, como Spyder, facilita la 
programación, especialmente en proyectos grandes.

Sus ventajas incluyen:

- Mejor legibilidad y escritura del código: resaltado de sintaxis, gestión 
automática de la indentación y visibilidad de errores comunes.
- Depuración más sencilla: mensajes de error claros, herramientas para ejecutar 
el código paso a paso, inspeccionar variables y usar puntos de interrupción.
- Gestión de proyectos complejos: organización de múltiples archivos, 
integración de librerías y módulos, y soporte para programación orientada a objetos.


4. Instalación y configuración

1) Instalar Anaconda (recomendado) desde https://www.anaconda.com
2) Esto incluye Python, Spyder y librerías científicas como NumPy, Pandas 
    y Matplotlib.
3) Abrir Spyder desde el menú de aplicaciones de Anaconda.
4) Configurar el idioma y el tema de la interfaz según preferencia.

5. Primeros pasos en Python con Spyder
En el Editor, escribir el siguiente código y guardarlo con extensión .py:
"""
# Ejemplo más utilizado en en Python

print("Hola, mundo")

#Presionar F5 o el botón ▶️ para ejecutar el script.
#Verificar el resultado en la Consola de IPython.

"""
5. Conceptos básicos para programar en Python

5.1. Configurar el directorio de trabajo

Python funciona como un entorno temporal de trabajo, lo que significa que el
 usuario va creando variables, cargando datos y ejecutando código en memoria. 

Sin embargo, si estos datos o resultados no se guardan en archivos, se perderán 
al cerrar la sesión. Por ello, es importante configurar una carpeta 
predeterminada en nuestro ordenador, donde Python buscará y guardará archivos 
por defecto.

Para ver el directorio de trabajo actual, escribimos el siguiente código en la 
consola de Python o en una celda:
"""
import os

# Ver directorio de trabajo actual
os.getcwd()

# Cambiar directorio de trabajo
## os.chdir("C:/ruta/a/otra/carpeta")

"""
En Spyder, también podemos hacerlo desde el menú:
1. Console > Current Working Directory (barra superior de Spyder, junto al 
                                        ícono de carpeta)
2. Elegimos la carpeta deseada y esta será el nuevo directorio predeterminado 
para la sesión.

3. Para verificar el cambio, volvemos a ejecutar:
    """
## os.getcwd()

"""
5. Librerías esenciales para estadística
En Python, el análisis estadístico se apoya en librerías como:

    - NumPy → manejo de arreglos y cálculos matemáticos.
    - Pandas → manejo de datos en tablas (DataFrames).
    - Matplotlib y Seaborn → visualización de datos.
    - Statsmodels y Scikit-learn → modelado estadístico y machine learning.
    """
import pandas as pd
import numpy as np

print("-" * 50) #Solo para separar las secciones, es un recurso de estilo

# Crear un DataFrame simple
data_libros = pd.DataFrame({
    'Edad': [23, 25, 30, 22],
    'Libros_leidos': [10, 15, 7, 20]})
print("-" * 50) 

#Puedes visualizar el nuevo objeto, "data", creado en el Explorador

print(data_libros.describe()) #Puedes visualizar esta matriz en el Terminal de IPython
print("-" * 50) 
"""
6.  Sintaxis en Python

En Python, la sintaxis es el conjunto de reglas que determinan cómo debe 
escribirse el código, es decir, la manera en la que hablaremos con Python. 

6.1. Palabras reservadas
Python tiene palabras reservadas que son reconocidas por el programa y están
diseñadas para gatillar funciones específicas y que por ende no deberían ser
usadas para la creación de variables, estas son:

• and
• as
• assert
• break
• class
• continue
• def
• del
• elif
• else
• except
• False
• finally
• for
• from
• global
• if
• import
• in
• is
• lambda
• None
• nonlocal
• not
• or
• pass
• raise
• return
• True
• try
• while
• with
• yield

 6.2. Variables
    Una variable es un nombre que hace referencia a un valor almacenado en 
    memoria.Se crean con una sentencia de asignación: nombre = valor. El tipo 
    de la variable depende del valor asignado (int, str, etc.). Es necesario 
    inicializarlas antes de usarlas, o se producirá un NameError.
    
    6.2.1. Tipos de datos
    Se refiere a la naturaleza de los datos que usamos para comunicarnos con 
    Python y que pueden ser reconocidos por el programa:
        - int (Entero): Números sin parte decimal. Ej.: 17
        - str (Cadena): Texto entre comillas simples o dobles. Ej.: "Qué tal!"
        - float (Punto flotante): Números con parte decimal. Ej.: 3.14 o pi
        - bool (Booleano): Valores lógicos True o False.
        - list (Lista): Secuencia mutable de elementos. Ej.: [1, 2, 3]
        - dict (Diccionario): Pares clave-valor. 
            Ej.: {"nombre": "Ana", "edad": 25}
        - tuple (Tupla): Secuencia inmutable. Ej.: (1, 2, 3)
        - NoneType: Representa ausencia de valor. Ej.: None

    
6.2. Sensibilidad a mayúsculas y minúsculas: 
    'Variable' y 'variable' son nombres distintos.
    
6.3. Indentación obligatoria: 
    Se usan espacios (recomendado 4) o tabulaciones para definir bloques.

6.4. Comentarios:
   - Una línea: usando "#".
   - Varias líneas: usando comillas triples 
6.5. Nombres de variables:
   - Deben empezar con letra o guion bajo.
   - Pueden contener letras, números y guion bajo, pero no espacios.
   - Evitar palabras reservadas (if, for, while, etc.).

6.6. Sentencias:
   - Generalmente una por línea, pero pueden separarse con ';' o unirse con '\'.

6.7. Cadenas de texto:
   - Se definen con comillas simples (' '), dobles (" ") o triples para varias 
   líneas.

6.8. Bloques de código:
   - No se usan llaves '{}' como en otros lenguajes, sino indentación.

6.9. Uso de paréntesis:
   - Para llamadas a funciones, agrupar operaciones o definir tuplas.
   
Para visualizar las diversas partes que componen la sintaxis, veamos este ejemplo:
"""
########## Ejemplo 1 ############
# 1. Instalamos pandas (solo es necesario hacerlo una vez en el entorno)
# Se ejecuta en la terminal o consola:
# pip install pandas openpyxl

import pandas as pd  # Importamos la librería pandas

# 2. Cargamos el archivo Excel en un "DataFrame" (objeto de pandas para manejar bases de datos)
    #Asegúrate de gestionar todos los archivos descargables en carpetas identificables

data1 = pd.read_excel("DemocracyIndex_2024.xlsx") 
print("-" * 50) 

# 3. Verificamos el tipo de objeto con la función "type()"
print("Verificamos el tipo de objeto") 
print(type(data1))
print(data1.head()) #Para asegurarnos que cargo bien pedimos las 10 primeras filas
print("-" * 50) 
# Resultado esperado: <class 'pandas.core.frame.DataFrame'>

# 4. Acceder a una variable (columna) específica del DataFrame
print("Acceder a una variable específica") 
Tipo_regimen = data1["Regime_type"] #La columna que veremos es del tipo de régimen
print("-" * 50) 

# 5. Verificar el tipo de la variable
print("Verificar el tipo de la variable") 
print(type("Regime_type"))
print("-" * 50) 
# Resultado esperado: <class 'str'> donde str significa string o cadena


"""
7. Análisis descriptivo en Python

Nuestra pregunta de investigación para hoy: 
    ¿Cuál es el estado de la democracia en el mundo?

El índice de democracia (Democracy Index) es un índice que mide la calidad de 
la democracia en el mundo. Mide diversas categorías como libertades civiles, 
cultura política, pluralismo electoral, etc. A partir de estas variables, 
se obtiene un puntaje promedio, el cual determina el puesto del país a nivel 
mundial, así como el tipo de régimen que tiene cada uno.

En esta ocasión, usaremos la base de datos del informe de 2024, publicado por 
The Economist Inteligence Unit (EIU). 


Ahora, toca responder la pregunta de investigación.

¡A trabajar!
"""

# Primero, revisaremos qué columnas conforma nuestro dataframe
print("Títulos de las columnas") #Podemos agregar un título a cada operación
print(data1.columns.values)
print("-" * 50) #Solo para separar las secciones, es un recurso de estilo

# Segundo, veremos qué tipo de datos se encuentran en estas columnas
print("Tipos de datos")
print(data1.dtypes)
print("-" * 50)

# Tercero, pediremos estadísticas descriptivas de las columnas numéricas
print("Estadísticas descriptivas valores numéricos")
print(data1.describe())
print("-" * 50)

########## Otras funciones útiles ###########

# Mostrar información general: tipos de datos, número de valores no nulos, memoria usada
print("Info general:")
print(data1.info())
print("-" * 50)

# Mostrar estadísticas también para columnas categóricas (tipo object)
print("Estadísticas descriptiivas no num.")
print(data1.describe(include='object'))
print("-" * 50)

# Contar valores faltantes por columna
print("Cantidad de valores nulos por columna")
print(data1.isna().sum())
print("-" * 50)


"""
7.1. ¿Cuál es la distribución de países por régimen?

Antes de comenzar a realizar nuestro análisis, debemos identificar la 
estructura de las variables y verificar que estén bien configuradas. Es decir 
que la escala de la variable coincida con el objeto en Python.

Por ejemplo, debemos asegurarnos que una variable categórica no esté configurada 
como numérica en Python, y viceversa.

Variable “Regime_type”:

Queremos saber el tipo de régimen de cada país observado. Para ello, realizamos 
el análisis de la variable.

Lo que queremos crear es una tabla de frecuencias. Necesitamos que cuente los 
casos (en esta data cada caso es un país) según cada categoría. En otras 
palabras, cuántos países hay por cada régimen.
"""

# Agrupar por la columna 'Regime_type' y contar el número de filas en cada grupo
frecuencia = data1.groupby("Regime_type").size().reset_index(name="Freq")

# Mostrar el resultado
print(frecuencia)
print("-" * 50)

"""
Se observa que, de los países analizados en el índice de la democracia, 
53 países son considerados como Autoritarismo, 27 como Regímenes híbridos, 
43 como Democracia imperfecta y solo 24 como Democracia Plena.
"""


"""
Creemos un gráfico de barras para visualizar mejor los países por tipo de régimen.

Ya creamos anteriormente la tabla de frecuencias, pero esta no fue agregada al 
environment. Para hacerlo necesitamos guardarla con un nombre. Necesitamos que 
tenga uno para poder referirnos a ella al hacer el gráfico. Para ello le agregamos 
al código anterior un “=” y antes del asignado irá el nombre del 
objeto nuevo “para_grafico”.
"""

# Crear tabla de frecuencias
para_grafico = data1.groupby("Regime_type").size().reset_index(name="Freq")

# Mostrar resultado
print(para_grafico)

"""
Es necesario llamar al paquete solo una vez y se podrá usar en las líneas que 
vayan después del llamado.
"""

import seaborn as sns
import matplotlib.pyplot as plt

# Gráfico de barras
sns.barplot(data=para_grafico, x="Regime_type", y="Freq", hue="Regime_type")


"""
Lo que estamos haciendo con este código es usar el comando seaborn que es el 
que permite hacer gráfico y le indicamos que usaremos la base de datos para_grafico. 
De ella, en el eje X del gráfico irá la variable Regime_type, en el eje Y 
la frecuencia (Freq) y el relleno será Regime_type. Esto último es para que cada 
barra tenga un color según su valor.

Adaptemos el diseño del gráfico y agreguemos etiquetas, títulos, y tema. Esto lo
haremos con matplotlib
"""

# Mejoras estéticas
plt.title("Frecuencia por Tipo de Regimen") #Su tíyulo
plt.xlabel("Regime_type") #Etiqueta del eje X
plt.ylabel("Frecuencia") #Eqtiqueta del eje Y
plt.xticks(rotation=45)  # Girar etiquetas si son largas
plt.legend(title="Regime_type") #Etiqueta de la leyenda

plt.show() # Que nos muestre el gráfico


"""
7.2 ¿Cuáles son las medidas de tendencia central del indicador de democracia 
de los países?

Entonces, una vez configurados adecuadamente nuestros objetos, pidamos los 
estadísticos de tendencia central para nuestras variables de interés.

¿Cuál es el promedio del puntaje de todos los países analizados?

Para ello, usamos el comando mean que significa “media o promedio”. 
Recuerda que summarise siempre debe incluir el tipo de resumen o el 
estadístico que necesitamos.
"""

# Calcular la media de la columna 'Overall_score'
media = data1["Overall_score"].mean()
print("-" * 50)
# La media es: 5.226735

# Si quieres un DataFrame como salida
media_df = pd.DataFrame({"media": [media]})

print(media_df)
print("-" * 50)

# Calcular la mediana de la columna 'Overall_score'
mediana = data1["Overall_score"].median()

# Si quieres que el resultado sea un DataFrame
mediana_df = pd.DataFrame({"mediana": [mediana]})

print(mediana_df)
# La mediana es: 5.35

"""
Este resultado quiere decir que el puntaje promedio de democracia de todos los 
países analizados es de 5.23 puntos.

En segundo lugar, calculamos la mediana de los puntajes. Esta medida es más 
robusta que la media, pues resiste valores extremos.

Esto quiere decir que, hasta la mitad de países analizados tienen una puntuación 
de hasta 5.22 puntos.
"""

#Grafiquemos

#Como la variable Overall_score es numérica, esta vez pediremos un histograma.

# Histograma de la columna 'Overall_score'
plt.hist(data1["Overall_score"], bins=10, edgecolor="black")  
# bins ajusta el número de barras
plt.xlabel("Overall_score")
plt.ylabel("Frecuencia")
plt.title("Histograma de Overall Score")
plt.show()

"""
El histograma revela una distribución bimodal, con picos situados aproximadamente 
en los 2 y 6 puntos del índice de democracia.
Esto sugiere la existencia de dos grupos bien diferenciados de países:
- Democracias plenas o defectuosas, con puntajes altos.
- Regímenes híbridos o autoritarios, con puntajes bajos.

Asimismo, el gráfico muestra un sesgo negativo, evidenciado por una cola de 
datos extendida hacia la izquierda. Esto indica que un número significativo de 
países presenta valores considerablemente bajos, lo que reduce el promedio general.
"""

"""
Ejercicio 1:
Ahora tú, practica calculando el promedio por región
"""

media_reg = data1.groupby("Region")["Overall_score"].mean().reset_index(name="Media")
print(media_reg)
print("-" * 50)

"""
Ejercicio 2:
Realiza la misma operación pero usando la mediana
"""
mediana_reg = data1.groupby("Region")["Overall_score"].median().reset_index(name="Mediana")
print(mediana_reg)
print("-" * 50)

"""
Explicación paso a paso:

- groupby("Region") : agrupa el DataFrame por cada valor de la columna Región.

- ["Overall_score"] : selecciona solo la columna numérica que queremos promediar.

- .mean() o .median() :  calcula la media o mediana para cada grupo.

- .reset_index(name="Media") :  devuelve el resultado en forma de tabla ordenada 
con un nombre de columna claro.
"""

# Tabla resumen con media y mediana por región
resumen_reg = (
    data1
    .groupby("Region")["Overall_score"]
    .agg(Media="mean", Mediana="median")
    .reset_index()
)

print(resumen_reg)


"""
Ejercicio 3: Escojan una variable numérica que no hayamos utilizado y 
hallen la mediana y la media de dicha variable, por continente.
"""
 
  
