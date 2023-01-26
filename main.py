from config import app, create_tables
from Controllers.usuariosController import usuariosController


app.register_blueprint(usuariosController, url_prefix='/users')


if __name__ == "__main__":
    try:
        create_tables()
        print("Conexión a la base de datos establecida exitosamente")
    except Exception as e:
        print("Error al conectarse a la base de datos: ", e)
    app.run()
