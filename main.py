from flask import Flask, render_template, request, redirect, url_for
import db
from models import Proyecto

app = Flask(__name__)

@app.route("/")
def home():
    todos_los_proyectos = db.session.query(Proyecto).all()
    return render_template("index.html", lista_de_proyectos = todos_los_proyectos) # para comunicar python con html

@app.route("/crear-proyecto", methods=["POST"])
def crear():
    proyecto = Proyecto(titulo=request.form["titulo_proyecto"], descripcion=request.form["descripcion_proyecto"], hecho=False) #conectar html con python
    db.session.add(proyecto)
    db.session.commit()
    return redirect(url_for("home")) #Esto nos redirecciona a la función home

@app.route("/eliminar-proyecto/<id>") # id es una variable
def eliminar(id):
    proyecto = db.session.query(Proyecto).filter_by(id=int(id))
    proyecto.delete()
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == "__main__":
    # En la siguiente linea estamos indicando a SQLAlchemy que cree, si no existen,
    # las tablas de todos los modelos que encuentre en models.py
    db.Base.metadata.create_all(db.engine)
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)