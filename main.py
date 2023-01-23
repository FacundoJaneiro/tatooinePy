from Dtos.usuario import UserSchema
from config import db, app, create_tables
from Entities.usuario import User
from flask import jsonify


@app.route("/")
def hello():
    users = User.query.all()
    user_schema = UserSchema(many=True)
    result = user_schema.dump(users)
    return jsonify(result)


if __name__ == "__main__":
    try:
        create_tables()
        print("Conexión a la base de datos establecida exitosamente")
    except Exception as e:
        print("Error al conectarse a la base de datos: ", e)
    app.run()
