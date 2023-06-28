from config import app, create_tables
from Controllers.usuariosController import usuariosController
from Controllers.materiasPrimasController import materiasPrimasController


app.register_blueprint(usuariosController, url_prefix='/users')
app.register_blueprint(materiasPrimasController, url_prefix='/materiasPrimas')


if __name__ == "__main__":
    try:
        create_tables()
        print("Conexión a la base de datos establecida exitosamente")
    except Exception as e:
        print("Error al conectarse a la base de datos: ", e)
    app.run()
