# 🧪 Proyecto Peng-Robinson Solver - Verano Delfín 2026

> **¡Bienvenidas!** > Este repositorio es un entorno de pruebas diseñado específicamente para aprender y practicar el flujo de trabajo colaborativo usando **Git** y **GitHub**. A lo largo de este proyecto, aprenderán a clonar repositorios, hacer *commits* y abrir *Pull Requests* de forma segura, todo mientras trabajamos con un modelo termodinámico real en Python.

Este proyecto implementa un solucionador (*solver*) basado en la ecuación de estado de Peng-Robinson. Permite calcular una variable de estado faltante (Presión, Volumen molar o Temperatura) de un fluido, siempre que se conozcan las otras dos.

---

## 📖 Marco Teórico: Ecuación de Estado de Peng-Robinson

*[Espacio en blanco: Las estudiantes deben reemplazar este texto con su investigación sobre la ecuación de Peng-Robinson, sus parámetros $a$ y $b$, y su relevancia en termodinámica].*











---

## ⚙️ Arquitectura del Proyecto

El código está estructurado siguiendo principios de "Arquitectura Limpia", separando los datos, la lógica matemática y el flujo de ejecución en tres archivos distintos:

### 1. `problem.py` (Definición de Datos)
Contiene la clase `ProblemaFluido`. Funciona exclusivamente como una estructura de datos para definir el estado inicial del sistema. 
* **Atributos:** Recibe el nombre del fluido (como un *string* compatible con la base de datos CoolProp), la Presión ($P$), el Volumen molar ($V$) y la Temperatura ($T$).
* **Lógica:** No realiza ningún cálculo. Se encarga únicamente de almacenar qué variables conocemos y cuál es la incógnita (la que entra como `None`).

### 2. `solver.py` (Motor Matemático)
Aquí reside toda la termodinámica y los métodos numéricos.
* **`obtener_propiedades_gas(fluido)`:** Se conecta con la librería `CoolProp` para extraer las constantes críticas del fluido: Temperatura crítica ($T_c$), Presión crítica ($P_c$) y el factor acéntrico ($\omega$).
* **`calcular_a_b(...)`:** Calcula los parámetros de atracción y repulsión del modelo de Peng-Robinson.
* **Cálculos específicos:** Contiene funciones dedicadas (`calcular_P_manual`, `calcular_V_manual`, `calcular_T_manual`) que aplican álgebra o métodos de optimización (como el cálculo de raíces de polinomios con `numpy` o el método de Brent con `scipy.optimize`) para encontrar la variable faltante.

### 3. `main.py` (Controlador Central)
Es el orquestador del programa.
* Toma un objeto `ProblemaFluido`.
* Analiza las variables para detectar automáticamente cuál es la incógnita (la variable declarada como `None`).
* Se comunica con `solver.py` para obtener las propiedades críticas y ejecutar la función de cálculo correspondiente.
* Imprime los resultados en la terminal con sus respectivas unidades.

---

## 🚀 Requisitos e Instalación

Para ejecutar este código en sus computadoras, necesitarán tener Python instalado y configurar un entorno virtual.

### Dependencias necesarias:
El motor matemático (`solver.py`) depende de las siguientes librerías científicas:
* `numpy` (Para manejo de arreglos y cálculo de raíces polinómicas).
* `scipy` (Para algoritmos de optimización matemática).
* `CoolProp` (Base de datos termodinámica de fluidos).

### Instrucciones de configuración:

1. **Clonar el repositorio:**
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd peng_robinson_solver