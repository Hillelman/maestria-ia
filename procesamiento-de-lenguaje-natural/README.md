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

## Curso de IBM - AI Generativa

**Machine learning** is a branch of artificial intelligence and computer science which focuses on the use of data and algorithms to imitate the way that humans learn, gradually improving its accuracy.

- Supervised learning uses labeled datasets to train algorithms that to classify data or predict outcomes accurately.
- Unsupervised learning uses machine learning algorithms to analyze and cluster unlabeled data sets, with little to no need for human intervention .
- Semi-supervised learning uses a training dataset with both labeled and unlabeled data.

**Deep learning** is a subset of machine learning, which is essentially a neural network with three or more layers.

**Foundation models** are pre-trained language models that serve as the basis for various downstream language understanding and generation tasks.

**Large language models (LLMs)** are a type of generative AI engine designed to process and generate text. What makes these models so fascinating is that they operate by sifting through extensive datasets, leveraging this knowledge to produce fresh textual content that closely emulates the style and tone of the source material. Typical examples of LLMs include OpenAI’s GPT-4, Google’s PaLM, and Meta’s LLaMA.

There are two types of LLMs:

- Proprietary LLMs are owned and controlled by a specific company or organization, and can only be used by customers that purchase a license.
- Open-source LLMs are made available to the public for free under open-source licenses.

**Tokenization** is a crucial phase in fine-tuning the LLM. Tokenization is the process of breaking down a text document or sequence of words into smaller units called tokens. Tokens can be as short as individual characters, words, or even subwords. Tokenization helps in various language-related tasks, such as text classification and sentiment analysis. In scientific or technical domains, specialized tokenization may be needed to break down complex terms. Tokenization is a fundamental step in natural language processing (NLP) because it transforms text data into a format that can be understood by machine learning models.
Tokenization is a fundamental step in natural language processing (NLP) because it transforms text data into a format that can be understood by machine learning models.

**An embedding** is a mathematical representation of a word or sequence of words in a numerical vector space.
LLMs use embeddings to convert words into vectors that can be processed and manipulated within the model, capturing the nuances of language and its associations.

**Transformer** refers to a specific type of neural network architecture called the "transformer model", that is designed to process sequential data, such as natural language sequences.

The transformer model consists of two main parts: an encoder and a decoder.
The encoder processes the input sequence and produces a sequence of hidden states, while the decoder takes this sequence as input and produces an output sequence. By training the model on a large corpus of data, the encoder learns to encode the text in a way that captures important information and patterns, while the decoder learns to generate output text that is semantically and grammatically correct.

**An encoder** is a component or module that processes input data and converts it into a structured representation that can be understood and used by the model.

**A decoder** is a component or module responsible for processing the structured encoding generated by the encoder and producing the output sequence.

**A recurrent neural network (RNN)** is a class of neural networks that includes weighted connections within a layer (compared with traditional feed-forward networks, which connect feed only to subsequent layers).

**A convolutional neural network (CNN)** is an extension of artificial neural networks (ANN) and is predominantly used for image recognition-based tasks.

RNNs are commonly used for natural language processing and speech recognition whereas CNNs are more often utilized for classification and computer vision tasks.

Both **prompt engineering and prompt tuning** are methods for modifying or optimizing prompts in natural language processing (NLP) models to get the best output from a large language model. Prompt engineering is the process of designing prompts, while prompt tuning refers to refining and optimizing those prompts based on model feedback.
Prompt engineering is the process of crafting input text to optimize the performance of a given model and its associated parameters. The ability to design thoughtful prompts is crucial in obtaining meaningful and contextually relevant outputs from these models.

This logical order ensures that the chatbot understands the user's request (Instruction), takes into account any dietary considerations (Context), provides the necessary details for the recipe (Input Data), and formats the response in a user-friendly way (Output Indicator).

Not all four elements are required for a prompt. The specific elements included in a prompt may vary depending on the task or application.

In prompt engineering, sentiment analysis is utilized to craft prompts that elicit specific emotions from language models. By manipulating the wording and phrasing of a prompt, prompt engineers can affect the model's generated responses.

## Types of prompting

- **Zero-shot prompting** is a technique in natural language processing (NLP) where a model can generate responses without having been explicitly trained on the specific task or prompt.

- **Chain-of-thought (CoT)** prompting is an input strategy used in language models to guide the generation of responses in a coherent and connected manner, resembling a chain of thoughts.

- **Generated-knowledge prompting** improves the knowledge and reasoning capabilities of language models by supplying them with generated or simulated data as prompts, instead of relying solely on pre-existing human-curated data.

- **Retrieval-augmented generation (RAG)** is a method introduced by researchers in Meta AI specifically tailored to handle knowledge-intensive tasks.
