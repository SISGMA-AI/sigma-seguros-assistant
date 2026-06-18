def detectar_intencion(mensaje):
    texto = mensaje.lower()

    if "cotizar" in texto or "seguro auto" in texto or "asegurar" in texto:
        return "cotizar_auto"

    if "siniestro" in texto or "choqué" in texto or "accidente" in texto:
        return "siniestro"

    if "renovar" in texto or "vence" in texto:
        return "renovacion_poliza"

    return "consulta_general"
