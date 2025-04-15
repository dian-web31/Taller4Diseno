# Taller4diseno app
Para ejecutar la aplicacion, primero debemos instanciar nuestro entorno virtual, así:
``` powershell
py -m venv venv
```

Activamos nuestro entorno virtual, así:
``` powershell
venv\Scripts\activate
```

E instalaremos los requirements para ejecutar nuestra interfaz
``` powershell
pip install -r requirements.txt
```

## Run the app

### uv

Run as a desktop app:

```
uv run flet run
```

Run as a web app:

```
uv run flet run --web
``