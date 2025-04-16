"""Modulo para manejar el frontend de la aplicacion"""
import flet as ft
from services.archivo import Archivo

def pantalla_pedir_archivo(page: ft.Page):
    """
    Nos permite manejar la pantalla de seleccion de archivos y mostrar el informe del Archivos CSV.
    """
    archivo_seleccionado = None

    def seleccionar_archivo(e): # Se conserva la variable e para evitar más de una seleccion de Archivos
        nonlocal archivo_seleccionado
        # Abre el selector de archivos
        file_picker.pick_files(allow_multiple=False)

    def mostrar_seleccion(e: ft.FilePickerResultEvent):
        nonlocal archivo_seleccionado
        if e.files:
            archivo_seleccionado = e.files[0]
            print(f"Archivo seleccionado: {archivo_seleccionado.name}")
            print(f"Ruta: {archivo_seleccionado.path}")
            datos = Archivo(archivo_seleccionado.path)
            datos = datos.generar_informe()
            for key, value in datos.items():
                page.add(
                    ft.Text(f"Estudiante: {key}, Materias: {value}"),
                    ft.Divider()
                )
        else:
            print("Selección cancelada")

    # Configura el FilePicker
    file_picker = ft.FilePicker(on_result=mostrar_seleccion)
    page.overlay.append(file_picker)

    # Añade un botón simple
    page.add(
        ft.ElevatedButton(
            "Seleccionar Archivos",
            icon=ft.Icons.FOLDER_OPEN,
            on_click=seleccionar_archivo
        )
    )

ft.app(pantalla_pedir_archivo)
