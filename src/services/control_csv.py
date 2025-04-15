"""
Módulo para manejar busqueda del CSV y el conteo de materias por estudiante.
"""
import os
from collections import defaultdict

class ControlCSV:
    """
    Clase ControlCSV para manejar la lectura y procesamiento de un archivo CSV.
    """
    def __init__(self, ruta: str):
        self.ruta = ruta

    def leer_csv(self) -> list:
        """
        Lee un archivo CSV con formato: cedula,nombre,codigo_materia,nombre_materia
        Retorna una lista de diccionarios con los datos estructurados.
        """
        if not os.path.exists(self.ruta):
            raise FileNotFoundError(f"El archivo {self.ruta} no existe.")

        datos = []
        with open(self.ruta, mode='r', encoding='utf-8') as csvfile:
            # Leemos línea por línea (el formato no usa comas consistentes)
            for linea in csvfile:
                # Limpiamos y dividimos la línea
                campos = linea.strip().split(',')
                if len(campos) >= 4:  # Aseguramos que tenga todos los campos
                    datos.append({
                        'cedula': campos[0].strip(),
                        'nombre': campos[1].strip(),
                        'codigo_materia': campos[2].strip(),
                        'nombre_materia': campos[3].strip()
                    })
        return datos

    def cuenta_materias(self) -> dict:
        """
        Cuenta las materias por estudiante.
        Retorna un diccionario con: {nombre_estudiante: cantidad_materias}
        """
        datos = self.leer_csv()
        contador = defaultdict(int)
        for registro in datos:
            contador[registro['nombre']] += 1
        return dict(contador)
    
    def generar_informe(self) -> dict:
        """
        Genera un diccionario con el conteo de materias por estudiante.
        (Alias de cuenta_materias() con nombre más descriptivo)
        """
        return self.cuenta_materias()
