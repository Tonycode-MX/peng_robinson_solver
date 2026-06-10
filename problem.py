# problem.py
class ProblemaFluido:
    """
    Estructura de datos pura para definir el estado de un fluido.
    No realiza cálculos; solo almacena las variables del sistema.
    """
    def __init__(self, fluido: str, P=None, V=None, T=None):
        self.fluido = fluido  # String con el nombre del fluido para CoolProp
        self.P = P            # Presión (en bar o Pascales, según lo decidan usar)
        self.V = V            # Volumen molar
        self.T = T            # Temperatura (en Kelvin)