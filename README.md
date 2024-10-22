# Simulador_ruleta_europea
# Juego de Ruleta en Python

Este es un proyecto simple de un juego de ruleta en Python. El juego permite a los jugadores realizar apuestas y simula el giro de la ruleta europea (números del 0 al 36). Además, incluye una representación gráfica de la ruleta utilizando Matplotlib.

## Archivos del proyecto

1. **ruleta.py**: Archivo principal donde se implementa la lógica del juego de ruleta, incluidas las apuestas y las reglas.
2. **config.py**: Define la configuración de la ruleta, como la asociación de los números con sus colores (rojo, negro y verde).
3. **graficas.py**: Contiene la función para mostrar una representación gráfica de la ruleta, con animaciones utilizando Matplotlib.

## Características

- Simulación de una ruleta europea con números del 0 al 36.
- Diferentes tipos de apuestas: número exacto, color, par/impar, docena y columna.
- Visualización gráfica de la ruleta usando Matplotlib, con animación del giro.
- Control de saldo del jugador con posibilidad de realizar múltiples apuestas hasta que el saldo se agote.

## Requisitos

Este proyecto requiere Python 3.x y las siguientes librerías:

- `matplotlib`
- `numpy`

Puedes instalar las dependencias ejecutando:

```bash
pip install matplotlib numpy

Para iniciar el juego, simplemente ejecuta el archivo ruleta.py:

bash
Copy code
python ruleta.py
Ejemplo de uso
El jugador comienza con un saldo de $100.
Se ofrecen cinco tipos de apuestas: número exacto, color, par/impar, docena y columna.
El jugador ingresa su apuesta y el monto a apostar.
La ruleta gira y muestra el número y color ganador.
Si la apuesta del jugador es ganadora, el saldo aumenta; de lo contrario, disminuye.
Personalización
Puedes modificar el archivo config.py para cambiar los colores de los números de la ruleta.
La función mostrar_ruleta_animada en graficas.py permite visualizar una animación de la ruleta girando.
