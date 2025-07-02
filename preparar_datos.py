import pandas as pd
from sklearn.model_selection import train_test_split
import spacy
from spacy.tokens import DocBin


# Cargar el dataset etiquetado
try:
    df = pd.read_csv("pqr_mensajes_etiquetados.csv", sep=';')
except FileNotFoundError:
    print("Error: pqr_mensajes_etiquetados.csv no encontrado .")
    exit()

# Dividir el dataset en entrenamiento y validación 80/20
train_df, val_df = train_test_split(df, test_size=0.2, random_state=42, stratify=df['categoria']) 

# Cargar un modelo de spaCy base. Usamos 'es_core_news_lg' para aprovechar sus vectores
nlp = spacy.load("es_core_news_lg")

# Crear el directorio corpus si no existe
def crear_docs(data, output_file):
    doc_bin = DocBin()
    for _, row in data.iterrows():
        doc = nlp.make_doc(row['text'])
        doc.cats = {categoria: 0 for categoria in df['categoria'].unique()}
        doc.cats[row['categoria']] = 1
        doc_bin.add(doc)
    doc_bin.to_disk(output_file)
    print(f"✔️ Creado archivo de datos en: {output_file}")

# Crear archivos .spacy para entrenamiento y validación
crear_docs(train_df, "./corpus/train.spacy")
crear_docs(val_df, "./corpus/dev.spacy")