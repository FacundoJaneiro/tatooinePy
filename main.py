from config import app, create_tables
from Controllers.usuariosController import usuariosController
from Controllers.componentesController import componenteController


app.register_blueprint(usuariosController, url_prefix='/users')
app.register_blueprint(componenteController, url_prefix='/componentes')



if __name__ == "__main__":
    try:
        create_tables()
        print("Conexión a la base de datos establecida exitosamente")
    except Exception as e:
        print("Error al conectarse a la base de datos: ", e)
    app.run()
