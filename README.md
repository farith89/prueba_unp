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

# creacion del Scripts para preparar los datos.

[text](preparar_datos.py)


python preparar_datos.py   

# Creacion de archivo de configuracion para spacy


python -m spacy init config --lang es --pipeline textcat --optimize efficiency --force config.cfg

# configuracion que importa

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

# llena la configuracion que no nos importa por defecto

python -m spacy init fill-config config.cfg config.cfg

python -m spacy train config.cfg --output ./output

# creacion del Scripts para preparar los datos

[text](inferencia.py)

python inferencia_datos.py   