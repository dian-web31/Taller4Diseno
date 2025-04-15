import flet as ft
from services.control_csv import ControlCSV

def pantalla_pedir_archivo(page: ft.Page):
    # Variable para almacenar el archivo seleccionado
    archivo_seleccionado = None

    def seleccionar_archivo(e):
        nonlocal archivo_seleccionado
        # Abre el selector de archivos
        file_picker.pick_files(allow_multiple=False)

    def cuando_selecciona(e: ft.FilePickerResultEvent):
        nonlocal archivo_seleccionado
        if e.files:
            archivo_seleccionado = e.files[0]  # Guarda el archivo seleccionado
            print(f"Archivo seleccionado: {archivo_seleccionado.name}")
            print(f"Ruta: {archivo_seleccionado.path}")
            datos = ControlCSV(archivo_seleccionado.path)
            datos = datos.generar_informe()
            for key, value in datos.items():
                page.add(
                    ft.Text(f"Estudiante: {key}, Materias: {value}"),
                    ft.Divider()
                )           
        else:
            print("Selección cancelada")

    # Configura el FilePicker
    file_picker = ft.FilePicker(on_result=cuando_selecciona)
    page.overlay.append(file_picker)

    # Añade un botón simple
    page.add(
        ft.ElevatedButton(
            "Seleccionar archivo",
            icon=ft.Icons.FOLDER_OPEN,
            on_click=seleccionar_archivo
        )
    )

ft.app(pantalla_pedir_archivo)