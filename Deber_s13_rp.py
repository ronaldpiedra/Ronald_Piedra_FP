def calcular_temperatura_promedio(temperaturas):
    """
    Calcula la temperatura promedio de cada ciudad durante un período de tiempo.

    :param temperaturas: Una lista de diccionarios, donde cada diccionario tiene el nombre de la ciudad
                         como clave y una lista de temperaturas semanales como valor.
    :return: Un diccionario con el nombre de la ciudad como clave y la temperatura promedio como valor.
    """
    promedios = {}

    for ciudad, datos in temperaturas.items():
        # Calcular la temperatura promedio para la ciudad
        total_temperaturas = sum(datos)
        num_semanas = len(datos)

        if num_semanas > 0:
            promedio = total_temperaturas / num_semanas
        else:
            promedio = 0

        promedios[ciudad] = promedio

    return promedios


# Ejemplo de uso
datos_temperaturas = {
    "Ciudad A": [22.5, 23.0, 21.8, 22.7],  # Temperaturas para 4 semanas
    "Ciudad B": [18.0, 19.2, 17.5, 18.6],
    "Ciudad C": [25.0, 26.5, 24.7, 25.3]
}

promedios = calcular_temperatura_promedio(datos_temperaturas)
print(promedios)
