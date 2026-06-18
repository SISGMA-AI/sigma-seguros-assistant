import json

def cargar_workflow(intencion):
    archivo = f"workflows/{intencion}.json"

    with open(archivo, "r", encoding="utf-8") as file:
        return json.load(file)

def obtener_siguiente_paso(workflow, datos_cliente):
    for paso in workflow["pasos"]:
        campo = paso.get("campo")

        if campo and campo not in datos_cliente:
            return paso

    return {
        "tipo": "accion",
        "accion": "derivar_productor"
    }
