import json

ruta = "/media/MV-Linux/MaquinasVirtuais/a25davidvm/Despregamento/datos.har"

def gardar_json_pretty(dicionario, nome_ficheiro):
    # filtrado = {clave: valor for clave, valor in dicionario.items() if valor == "content-type"}
    with open(nome_ficheiro, 'w') as ficheiro:
        # Usamos json.dumps para converter o dicionario a unha cadea de texto JSON ben formateada
        json.dump(dicionario, ficheiro, indent=4, ensure_ascii=False)

def ler_har(path):
    with open(path, 'r', encoding='utf-8') as ficheiro:
        datos = json.load(ficheiro)
    return datos

diccionario = ler_har(ruta)

entries = diccionario.get("log").get("entries")

for value in entries:
    for response in value.get("response"):
        for header in response.get("headers"):
            if(header.get("name") == "content-type"):
                if(header.get("value") == "application/json; charset=UTF-8"):
                    print(header.get("name").index())
                
filtered_datos = diccionario.get("mimeType","application/json*")

# print(filtered_datos)