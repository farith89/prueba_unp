# Creacion y activacion de el entorno virtual.
python -m venv venv
.\venv\Scripts\Activate.ps1

# Creacion de archivo.txt para instalar librerias necesarias en el proyecto.
requirements.txt

spacy==3.7.5
pandas==2.2.2
spacy-transformers==1.3.9
scikit-learn==1.7.0

instalar requirements.txt
pip install -r requirements.txt
python -m spacy download es_core_news_lg

# Creacion del Scripts para preparar los datos.

[text](preparar_datos.py)


python preparar_datos.py   

# Creacion de archivo de configuracion para spacy


python -m spacy init config --lang es --pipeline textcat --optimize efficiency --force config.cfg

# Configuracion que importa

#########################################

[paths]
train = "./corpus/train.spacy"
dev = "./corpus/dev.spacy"
vectors = "es_core_news_lg"

[nlp]
lang = "es"
pipeline = ["textcat"]

[components]
[components.textcat]
factory = "textcat"

[components.textcat.model]
@architectures = "spacy.TextCatEnsemble.v2"

#############################################

# Llena la configuracion que no nos importa por defecto

python -m spacy init fill-config config.cfg config.cfg

python -m spacy train config.cfg --output ./output

# Creacion del Scripts para preparar los datos

[text](inferencia.py)

python inferencia_datos.py   



# Comparto las metricas de mi modelo

 "performance":{
    "cats_score":0.7166666667,
    "cats_score_desc":"macro F",
    "cats_micro_p":0.8,
    "cats_micro_r":0.8,
    "cats_micro_f":0.8,
    "cats_macro_p":0.7222222222,
    "cats_macro_r":0.7777777778,
    "cats_macro_f":0.7166666667,
    "cats_macro_auc":1.0,
    "cats_f_per_type":{
      "Petici\ufffdn":{
        "p":1.0,
        "r":1.0,
        "f":1.0
      },
      "Reclamo":{
        "p":1.0,
        "r":1.0,
        "f":1.0
      },
      "Denuncia":{
        "p":1.0,
        "r":1.0,
        "f":1.0
      },
      "Solicitud":{
        "p":0.0,
        "r":0.0,
        "f":0.0
      },
      "Felicitaci\ufffdn":{
        "p":1.0,
        "r":0.6666666667,
        "f":0.8
      },
      "Queja":{
        "p":0.3333333333,
        "r":1.0,
        "f":0.5
      }
    },
    "textcat_loss":0.0000001056
  }


# Subir el proyecto a git

git add .
git commit -m "Advertencia el git se sube sin el entorno virtual y archivos del modelo por su tamaño"
git push -u origin main --force
