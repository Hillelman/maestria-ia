# Procesamiento de Lenguaje Natural

Curso impartido por el Dr. Luis Eduardo Falcón Morales durante el trimestre Abri-Mayo-Junio 2025

## Conceptos básicos

**Corpus lingüístico**
Con el fin de tener un conjunto de documentos estandarizado que pudieran ser usados para llevar a cabo los análisis y pruebas con datos de texto, la comunidad científica fue creando lo que se llaman “corpus lingüísticos”. Así, un corpus lingüístico es un conjunto de documentos de texto que pueden abarcar diferentes temáticas como notas periodísticas, novelas de diversos autores, documentos oficiales, etc. El poder trabajar con un conjunto de documentos estándar ayudará a los investigadores a comparar las técnicas y modelos de inteligencia artificial que se vayan proponiendo. Actualmente, existe una gran cantidad de ellos, agrupados ya no solo por temáticas de los documentos de texto, sino también con base a las técnicas y métodos de inteligencia artificial que se desean validar, como por ejemplo corpus lingüísticos para entrenar modelos que sean capaces de responder preguntas en un chatbot, o bien para generar un resumen de un documento, o bien para distinguir y clasificar un documento por el tipo de temática sobre la cual se está hablando, o bien para traducir un documento de un idioma a otro, etc.

**Inteligencia Artificial (IA)**
Es cualquier método que permita a una computadora simular el comportamiento humano.

**Machine Learning (ML)**
Área de la IA que aplica técnica diversas para que las computadoras mejoren su desempeño con base a la experiencia

**Deep Learning (DL)**
Área de ML que implementa modelos de redes neuronales profundas. Incluye el área de visión y NLP.

**Generative IA**
Área de DL que genera datos de manera probabilística con base al conocimiento de la distribución de los datos.

**Large Language Model (LLM)**
Área de la IA generativa enfocada a la generación de texto.

**Diccionario de vocabulario**
Un “diccionario” nos permitirá relacionar las palabras o tokens de un documento de texto mediante el formato “clave:valor” (“key:value” en inglés). Esta correspondencia nos permitirá asociar de manera única cada token de un documento de texto con un ID en un arreglo matricial, cuya información numérica estará asociada a la participación de cada token en dichos documentos. Dichas matrices serán a su vez la fuente de información para alimentar los modelos de aprendizaje automático o machine learning.

**Modelado de tópicos (Topic Modeling)**
Un tópico es una combinación de palabras con una distribución de probabilidad.
Un documento es una combinación de tópicos con otra distribución de probabilidad.
