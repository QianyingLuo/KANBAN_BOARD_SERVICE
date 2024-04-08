from sqlalchemy import Column, Integer, Boolean, String

import db

class Proyecto(db.Base):

    __tablename__ = "proyecto"
    __table_args__ = {'sqlite_autoincrement': True} # quiero que haya una columna actúe como identificador que autoincremente
    id = Column(Integer, primary_key=True)
    titulo = Column(String(150), nullable=False)
    descripcion = Column(String(200), nullable=False)
    hecho = Column(Boolean)

    def __init__(self, titulo, descripcion, hecho):
        self.titulo = titulo
        self.descripcion = descripcion
        self.hecho = hecho
        print("Proyecto creado con éxito")

    def __str__(self):
        return "Proyecto {}: {} -> {} ({})".format(self.id, self.titulo, self.descripcion, self.hecho)