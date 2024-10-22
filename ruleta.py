import random
import matplotlib.pyplot as plt
from graficas import mostrar_ruleta
from config import ruleta

# Definimos la ruleta europea (números del 0 al 36)


def girar_ruleta():
    """Simula el giro de la ruleta y devuelve el número ganador."""
    resultado = random.randint(0, 36)  # Genera un número entre 0 y 36
    color = ruleta[resultado]  # Busca el color correspondiente
    return resultado, color

def realizar_apuesta():
    """Permite al usuario elegir una apuesta: número, color o par/impar."""
    print("Tipos de apuestas:")
    print("1. Número exacto (0-36)")
    print("2. Color (rojo o negro)")
    print("3. Par o impar")
    print("4. Docena (1-12, 13-24, 25-36)")
    print("5. Columna (1ra, 2da, 3ra)")
    
    tipo_apuesta = int(input("Elige el tipo de apuesta (1, 2, 3, 4 o 5): "))
    
    if tipo_apuesta == 1:
        numero = int(input("Apuesta a un número (0-36): "))
        return 'numero', numero
    elif tipo_apuesta == 2:
        color = input("Apuesta a un color (red o black): ").lower()
        return 'color', color
    elif tipo_apuesta == 3:
        paridad = input("Apuesta a par o impar: ").lower()
        return 'paridad', paridad
    elif tipo_apuesta == 4:
        docena = int(input("Apuesta a una docena (1, 2 o 3): "))
        return 'docena', docena
    elif tipo_apuesta == 5:
        columna = int(input("Apuesta a una columna (1, 2 o 3): "))
        return 'columna', columna
    else:
        print("Apuesta no válida.")
        return None, None

def verificar_apuesta(resultado, apuesta):
    """Verifica si la apuesta del usuario es ganadora."""
    tipo_apuesta, valor = apuesta
    numero, color = resultado
    
    if tipo_apuesta == 'numero':
        return numero == valor  # Compara el número de la ruleta con la apuesta
    elif tipo_apuesta == 'color':
        return color == valor  # Compara el color
    elif tipo_apuesta == 'paridad':
        es_par = numero % 2 == 0 and numero != 0  # 0 no es par ni impar
        return (valor == 'par' and es_par) or (valor == 'impar' and not es_par)
    elif tipo_apuesta == 'docena':
        if valor == 1:
            return 1 <= numero <= 12
        elif valor == 2:
            return 13 <= numero <= 24
        elif valor == 3:
            return 25 <= numero <= 36
    elif tipo_apuesta == 'columna':
        if valor == 1:
            return numero % 3 == 1
        elif valor == 2:
            return numero % 3 == 2
        elif valor == 3:
            return numero % 3 == 0

    return False

# Juego de ruleta con sistema de banca
def juego_ruleta():
    saldo = 100  # Saldo inicial del jugador
    print(f"Bienvenido a la ruleta. Tu saldo es de ${saldo}.")

    while saldo > 0:
        print(f"Tu saldo actual es: ${saldo}.")

        # Preguntar si quiere seguir apostando
        seguir = input("¿Quieres hacer otra apuesta? (sí/no): ").lower().strip()
        if seguir == 'no':
            print("Gracias por jugar. ¡Hasta la próxima!")
            break
        elif seguir != 'si':  # Validar la entrada
            print("Entrada no válida. Por favor, responde 'sí' o 'no'.")
            continue
        
        tipo_apuesta, valor_apuesta = realizar_apuesta()
        
        if tipo_apuesta is None:
            print("Apuesta inválida. Intenta de nuevo.")
            continue
        
        try:
            apuesta = int(input("Ingresa la cantidad que deseas apostar: "))
        except ValueError:
            print("Debes ingresar un número válido.")
            continue
        
        if apuesta > saldo:
            print("No tienes suficiente saldo para esa apuesta.")
            continue
        
        resultado = girar_ruleta()
        print(f"La ruleta ha caído en {resultado[0]} ({resultado[1]}).")
        
        mostrar_ruleta(resultado)  # Mostrar el resultado gráficamente
        
        if verificar_apuesta(resultado, (tipo_apuesta, valor_apuesta)):
            print("¡Felicidades! Has ganado la apuesta.")
            saldo += apuesta
        else:
            print("Lo siento, has perdido.")
            saldo -= apuesta
        
        if saldo <= 0:
            print("Te has quedado sin saldo. ¡Fin del juego!")
            break

# Ejecutar el juego
juego_ruleta()