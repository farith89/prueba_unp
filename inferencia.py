import spacy


try:
    nlp_model = spacy.load("./output/model-best")
except IOError:
    print("Error: No se encontró el modelo entrenado")
    exit()

def predecir_categoria(texto):
    
    doc = nlp_model(texto)

    categoria_predicha = max(doc.cats, key=doc.cats.get)
    return categoria_predicha


textos_de_prueba = [
    "Estoy muy feliz con la atención.",
    "Denuncio que temo por mi vida.",
    "La página web no funciona y no puedo radicar mis documentos.",
    "quiero hacer una denuncia por acoso.",]

print("Clasificación PQRSD")
for texto in textos_de_prueba:
    categoria = predecir_categoria(texto)
    print(f"Texto: '{texto}'\n  -> Categoría: {categoria}\n")