# 🧪 Proyecto Peng-Robinson Solver - Verano Delfín 2026

> **¡Bienvenidas!** > Este repositorio es un entorno de pruebas diseñado específicamente para aprender y practicar el flujo de trabajo colaborativo usando **Git** y **GitHub**. A lo largo de este proyecto, aprenderán a clonar repositorios, hacer *commits* y abrir *Pull Requests* de forma segura, todo mientras trabajamos con un modelo termodinámico real en Python.

Este proyecto implementa un solucionador (*solver*) basado en la ecuación de estado de Peng-Robinson. Permite calcular una variable de estado faltante (Presión, Volumen molar o Temperatura) de un fluido, siempre que se conozcan las otras dos.

---

## 📖 Marco Teórico: Ecuación de Estado de Peng-Robinson

# [cite_start]ECUACIÓN DE ESTADO PENG-ROBINSON [cite: 1]

[cite_start]La Ecuación de Estado Peng Robinson es esencialmente un modelo matemático utilizado para el cálculo y la predicción del comportamiento de componentes puros y mezclas en estado gaseoso, líquido y fluido supercrítico[cite: 2]. [cite_start]Esta Ecuación de Estado es una forma cúbica, similar a las ecuaciones anteriores de Van der Waals y Redlich-Kwong, con la mejora añadida de un término adicional para describir mejor el comportamiento de los fluidos no ideales[cite: 3]. [cite_start]Su eficacia, especialmente para los sistemas formados por hidrocarburos, ha contribuido a su uso generalizado en la industria y el mundo académico[cite: 4].

## [cite_start]Forma General [cite: 5]

[cite_start]La forma general de la ecuación de Peng-Robinson en función de la presión ($P$), la temperatura ($T$) y el volumen molar ($v$) es[cite: 5]:

[cite_start]$$P = \frac{RT}{v-b} - \frac{a(T)}{v(v+b)+b(v-b)}$$ [cite: 6]

[cite_start]**Donde:** [cite: 7]
* [cite_start]**$R$**: Constante universal de los gases[cite: 8].
* [cite_start]**$b$**: Parámetro de covolumen (representa el volumen que ocupan las moléculas)[cite: 9].
* [cite_start]**$a(T)$**: Parámetro de atracción molecular, que cambia según la temperatura[cite: 10].

---

## [cite_start]Parámetro de Covolumen ($b$) [cite: 11]

[cite_start]Este valor representa el volumen molecular efectivo y se calcula a partir de las propiedades críticas de la sustancia (temperatura crítica $T_c$ y presión crítica $P_c$)[cite: 11]:

[cite_start]$$b = 0.07780 \frac{R T_c}{P_c}$$ [cite: 12]

---

## [cite_start]Parámetro de Atracción ($a(T)$) [cite: 13]

[cite_start]Peng-Robinson introdujo una dependencia térmica más completa para considerar cómo se atraen las moléculas entre sí[cite: 13]:

[cite_start]$$a(T) = a(T_c) \alpha(T_r, \omega)$$ [cite: 14]

[cite_start]**Donde:** [cite: 15]
* [cite_start]$$a(T_c) = 0.45724 \frac{R^2 T_c^2}{P_c}$$ [cite: 16]
* [cite_start]$$\alpha(T_r, \omega) = \left[1 + k\left(1 - \sqrt{T_r}\right)\right]^2$$ [cite: 17]
* [cite_start]$$T_r = \frac{T}{T_c}$$ (Temperatura reducida)[cite: 18].
* [cite_start]$$k = 0.37464 + 1.54226\omega - 0.26992\omega^2$$ [cite: 19]
* [cite_start]**$\omega$ (Omega)**: Es el factor acéntrico de Pitzer, que mide qué tan "esférica" o compleja es la molécula[cite: 20].

---

## [cite_start]Factor de Compresibilidad ($Z$) [cite: 21]

[cite_start]Para resolver la ecuación en función del volumen, se suele expresar como una ecuación cúbica[cite: 21]:

[cite_start]$$Z^3 - (1-B)Z^2 + (A-3B^2-2B)Z - (AB-B^2-B^3) = 0$$ [cite: 22]

[cite_start]Donde los parámetros $A$ y $B$ dependen de la presión y la temperatura[cite: 23]:
* [cite_start]$$A = \frac{a(T) P}{R^2 T^2}$$ [cite: 24]
* [cite_start]$$B = \frac{b P}{R T}$$ [cite: 25]

---

## [cite_start]Equilibrio Líquido-Vapor (ELV) [cite: 26]

[cite_start]La PR-EOS es fundamental para modelar cómo se distribuyen las sustancias entre el líquido y el vapor[cite: 26]. [cite_start]Esto se logra mediante el concepto de fugacidad[cite: 27]. [cite_start]Al igualar la fugacidad de cada componente en la fase líquida ($L$) y en la fase vapor ($V$) ($f_i^L = f_i^V$) podemos determinar las condiciones exactas de equilibrio[cite: 27].

[cite_start]En general, la ecuación de Peng-Robinson destaca por su gran precisión al calcular densidades de líquidos y su excelente desempeño en sistemas de hidrocarburos[cite: 28]. [cite_start]Aunque no es la opción ideal para sustancias muy polares (como el agua), sigue siendo el estándar en la industria para realizar simulaciones termodinámicas complejas de manera confiable[cite: 29].


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