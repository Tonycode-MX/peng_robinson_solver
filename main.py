# main.py
from problem import ProblemaFluido
import solver

def procesar_y_resolver(problema: ProblemaFluido):
    """
    Aquí se hace el trabajo sucio. Revisa cuál variable es None,
    pide las constantes críticas a solver y ejecuta la fórmula correspondiente.
    """
    print(f"\n[Main] Procesando estado para el fluido: {problema.fluido}...")
    
    # 1. Obtener los datos críticos desde el solver usando el string del problema
    Tc, Pc, omega = solver.obtener_propiedades_gas(problema.fluido)
    if Tc is None:
        print("[Main] Cancelando operación debido a error en el nombre del fluido.")
        return

    print(f"[Main] Constantes críticas -> Tc: {Tc:.2f} K | Pc: {Pc/1e5:.2f} bar")

    # 2. IDENTIFICAR LA INCÓGNITA (La variable que es None)
    
    # CASO A: Presión es la incógnita
    if problema.P is None and problema.V is not None and problema.T is not None:
        print("[Main] Detectado: Buscando Presión (P)...")
        # El cálculo manual se hace en el Sistema Internacional (m3/mol y K)
        problema.P = solver.calcular_P_manual(problema.V, problema.T, Tc, Pc, omega)
        print(f"== RESULTADO == Presión Calculada: {problema.P / 1e5:.4f} bar")

    # CASO B: Volumen es la incógnita
    elif problema.V is None and problema.P is not None and problema.T is not None:
        print("[Main] Detectado: Buscando Volumen Molar (V)...")
        # Pasamos la presión al SI antes de calcular
        problema.V = solver.calcular_V_manual(problema.P, problema.T, Tc, Pc, omega)
        print(f"== RESULTADO == Volumen Molar Calculado: {problema.V * 1e6:.2f} cm3/mol")

    # CASO C: Temperatura es la incógnita
    elif problema.T is None and problema.P is not None and problema.V is not None:
        print("[Main] Detectado: Buscando Temperatura (T)...")
        problema.T = solver.calcular_T_manual(problema.P, problema.V, Tc, Pc, omega)
        print(f"== RESULTADO == Temperatura Calculada: {problema.T:.2f} K")
        
    else:
        print("[Main] Error: Asegúrate de enviar exactamente DOS variables con datos y una como None.")


# --- EJEMPLO DE USO / PRUEBAS DEL ECOSYSTEMA ---
if _name_ == "_main_":
    print("=== PROBANDO ARQUITECTURA LIMPIA ===")
    
    # Ejemplo 1: Queremos calcular el Volumen Molar del Propano (V = None)
    # Definimos las condiciones de entrada: P = 10 bar (10e5 Pa), T = 350 K
    estado_propano = ProblemaFluido(fluido="Propane", P=10e5, V=None, T=350.0)
    
    # Le pasamos el objeto al "trabajo sucio" del main
    procesar_y_resolver(estado_propano)
    
    
    # Ejemplo 2: Queremos calcular la Presión del Metano (P = None)
    # Definimos V = 600 cm3/mol (0.0006 m3/mol) y T = 240 K
    estado_metano = ProblemaFluido(fluido="Methane", P=None, V=0.0006, T=240.0)
    
    procesar_y_resolver(estado_metano)

