from intent_classifier import detectar_intencion
from dialog_manager import cargar_workflow, obtener_siguiente_paso

mensaje_cliente = "Hola, quiero cotizar un seguro para mi auto"

intencion = detectar_intencion(mensaje_cliente)
workflow = cargar_workflow(intencion)

datos_cliente = {}

siguiente_paso = obtener_siguiente_paso(workflow, datos_cliente)

print({
    "mensaje_cliente": mensaje_cliente,
    "intencion_detectada": intencion,
    "siguiente_paso": siguiente_paso
})
