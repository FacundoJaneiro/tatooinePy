
# TatooinePy


## Variables de Entorno 🦾

Debemos crear en la raiz del proyecto un archivo .env que contenga las siguientes variables de entorno
- DATABASE_URI = (URI de nuestra base de datos)


## Deployment 🦾

Para deployar este proyecto

- Abrimos el entrono virtual desde la ruta del proyecto

MAC/LINUX
```bash
    . venv/bin/activate
```

Windows
```bash
    . venv/Scripts/activate
```

-  Instalamos las dependencias

```bash
    pip install -r requirements.txt
```

-  Corremos la API

```bash
    python main.py
```


## Extras WorkFlow 🧑‍🔧

Para añadir una nueva dependencia al proyecto ejecutar el siguiente comando

```bash
    pip freeze > requirements.txt
```

## Authors ✍️

- [@FacundoJaneiro](https://www.github.com/FacundoJaneiro)
