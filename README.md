def saludar(nombre, edad):
    print(f"hola, {nombre} tienes {edad} años.")


saludar("ronald", 33)
saludar("Isabel", 32)


def saludar_con_saludo(nombre, edad, saludo="hola"):
    print(f"{saludo}, {nombre} tienes {edad} años.")


saludar_con_saludo("ronald", 33)
saludar_con_saludo("Isabel", 32, "hola")
