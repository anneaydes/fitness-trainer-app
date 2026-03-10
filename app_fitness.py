"""
Proyecto: Sistema de Rutina, Dieta y Progreso Fitness

Este programa registra personas con:
- nombre
- sexo
- edad
- peso en libras
- estatura en pies

Luego calcula el IMC y recomienda:
- rutina de gimnasio
- dieta
- déficit o superávit calórico
- progreso mensual estimado

También muestra una tabla de datos y una gráfica del peso.
"""

import pandas as pd
import matplotlib.pyplot as plt


nombres = []
sexos = []
edades = []
pesos_lb = []
estaturas_ft = []
imc_lista = []


def convertir_peso(peso_lb):
    """Convierte libras a kilogramos"""
    return peso_lb * 0.453592


def convertir_estatura(estatura_ft):
    """Convierte pies a metros"""
    return estatura_ft * 0.3048


def calcular_imc(peso_lb, estatura_ft):
    """Calcula el índice de masa corporal"""

    peso_kg = convertir_peso(peso_lb)
    estatura_m = convertir_estatura(estatura_ft)

    imc = peso_kg / (estatura_m ** 2)

    return imc


def analizar_edad(edad):
    """Da recomendaciones según la edad"""

    print("\n--- Análisis por edad ---")

    if edad < 18:

        print("Entrenamiento moderado y supervisado.")

    elif edad <= 40:

        print("Puedes realizar entrenamiento completo.")

    else:

        print("Se recomienda entrenamiento moderado y más descanso.")


def recomendar_rutina(imc):
    """Recomienda rutina según IMC"""

    print("\n--- Rutina semanal ---")

    if imc < 18.5:

        print("Objetivo: Subir masa muscular")
        print("Lunes: Piernas")
        print("Martes: Pecho")
        print("Miércoles: Descanso")
        print("Jueves: Espalda")
        print("Viernes: Hombros")

    elif imc < 25:

        print("Objetivo: Mantener condición física")
        print("Lunes: Pecho")
        print("Martes: Piernas")
        print("Miércoles: Cardio")
        print("Jueves: Espalda")
        print("Viernes: Hombros")

    else:

        print("Objetivo: Bajar peso")
        print("Lunes: Cardio")
        print("Martes: Piernas")
        print("Miércoles: Cardio")
        print("Jueves: Espalda")
        print("Viernes: Cardio")


def recomendar_dieta(imc):
    """Recomienda dieta según IMC"""

    print("\n--- Dieta recomendada ---")

    if imc < 18.5:

        print("Consumir más calorías saludables.")
        print("Ejemplo: avena, arroz, pollo, aguacate.")

    elif imc < 25:

        print("Dieta balanceada.")
        print("Proteína, vegetales y carbohidratos integrales.")

    else:

        print("Reducir calorías.")
        print("Más vegetales y proteínas magras.")


def recomendacion_calorica(imc):
    """Define déficit o superávit"""

    if imc < 18.5:

        print("\nDebe hacer SUPERÁVIT CALÓRICO")
        return "superavit"

    elif imc < 25:

        print("\nDebe mantener calorías")
        return "mantener"

    else:

        print("\nDebe hacer DÉFICIT CALÓRICO")
        return "deficit"


def progreso_mensual(peso, tipo):
    """Simula progreso mensual"""

    print("\n--- Progreso estimado en 1 mes ---")

    if tipo == "deficit":

        nuevo_peso = peso - 4
        print("Podrías bajar hasta:", nuevo_peso, "lb")

    elif tipo == "superavit":

        nuevo_peso = peso + 3
        print("Podrías subir hasta:", nuevo_peso, "lb")

    else:

        print("Tu peso probablemente se mantenga en:", peso, "lb")


def registrar_persona():
    """Registra una nueva persona"""

    nombre = input("Nombre: ")

    sexo = input("Sexo (M/F): ")

    edad = int(input("Edad: "))

    peso = float(input("Peso en libras: "))

    estatura = float(input("Estatura en pies: "))

    imc = calcular_imc(peso, estatura)

    nombres.append(nombre)
    sexos.append(sexo)
    edades.append(edad)
    pesos_lb.append(peso)
    estaturas_ft.append(estatura)
    imc_lista.append(imc)

    print("\nIMC:", round(imc, 2))

    analizar_edad(edad)

    recomendar_rutina(imc)

    recomendar_dieta(imc)

    tipo = recomendacion_calorica(imc)

    progreso_mensual(peso, tipo)


def mostrar_datos():
    """Muestra datos en tabla"""

    if len(nombres) == 0:

        print("No hay datos registrados")
        return

    datos = pd.DataFrame({

        "Nombre": nombres,
        "Sexo": sexos,
        "Edad": edades,
        "Peso (lb)": pesos_lb,
        "Estatura (ft)": estaturas_ft,
        "IMC": imc_lista

    })

    print("\nDatos registrados")

    print(datos)


def grafica_peso():
    """Crea gráfica de peso con color según sexo"""

    if len(nombres) == 0:

        print("No hay datos para graficar")
        return

    colores = []

    for sexo in sexos:

        if sexo.upper() == "F":

            colores.append("pink")

        else:

            colores.append("blue")

    plt.bar(nombres, pesos_lb, color=colores)

    plt.title("Peso de los usuarios")

    plt.xlabel("Personas")

    plt.ylabel("Peso en libras")

    plt.show()


while True:

    print("\n----- MENÚ -----")
    print("1 Registrar persona")
    print("2 Mostrar datos")
    print("3 Ver gráfica")
    print("4 Salir")

    opcion = input("Seleccione opción: ")

    if opcion == "1":

        registrar_persona()

    elif opcion == "2":

        mostrar_datos()

    elif opcion == "3":

        grafica_peso()

    elif opcion == "4":

        print("Programa finalizado")
        break

    else:

        print("Opción incorrecta")