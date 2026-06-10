import numpy as np
import scipy.optimize as opt
import CoolProp.CoolProp as CP

# Constante universal de los gases en J/(mol*K)
R = 8.31446 


def obtener_propiedades_gas(fluido):
    """Extrae las propiedades críticas de CoolProp"""
    try:
        Tc = CP.PropsSI("Tcrit", fluido)
        Pc = CP.PropsSI("pcrit", fluido)
        omega = CP.PropsSI("acentric", fluido)
        return Tc, Pc, omega
    except ValueError:
        print(f"Error: El fluido '{fluido}' no está disponible en CoolProp.")
        return None, None, None

def calcular_a_b(T, Tc, Pc, omega):
    """Calcula los parámetros a y b de Peng-Robinson manualmente"""
    Tr = T / Tc
    kappa = 0.37464 + 1.54226 * omega - 0.26992 * omega**2
    alpha = (1 + kappa * (1 - np.sqrt(Tr)))**2
    
    a = 0.45724 * (R**2 * Tc**2) / Pc * alpha
    b = 0.07780 * (R * Tc) / Pc
    return a, b

def calcular_P_manual(V, T, Tc, Pc, omega):
    a, b = calcular_a_b(T, Tc, Pc, omega)
    P = (R * T) / (V - b) - a / (V * (V + b) + b * (V - b))
    return P

def calcular_V_manual(P, T, Tc, Pc, omega):
    a, b = calcular_a_b(T, Tc, Pc, omega)
    A = (a * P) / (R**2 * T**2)
    B = (b * P) / (R * T)
    
    c2 = -(1 - B)
    c1 = A - 2*B - 3*B**2
    c0 = -(A*B - B**2 - B**3)
    
    raices_Z = np.roots([1, c2, c1, c0])
    raices_reales = [z.real for z in raices_Z if np.isreal(z) and z.real > 0]
    
    if not raices_reales:
        return None
    return max(raices_reales) * R * T / P

def calcular_T_manual(P, V, Tc, Pc, omega):
    funcion_objetivo = lambda T_est: calcular_P_manual(V, T_est, Tc, Pc, omega) - P
    solucion = opt.root_scalar(funcion_objetivo, bracket=[Tc*0.1, Tc*3], method='brentq')
    return solucion.root
