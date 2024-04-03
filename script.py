import json
from datetime import datetime
class Usuario():
    def __init__(self, nombre: str, apellido: str, email: str, genero: str) -> None:
        self.nombre = nombre
        self.apellidos = apellido
        self.email = email
        self.genero = genero


    def __str__(self):
        return f"Nombre:{self.nombre} , Apellido:{self.apellidos}, Email: {self.email}, Genero:{self.genero}" 



instancias = [] 
with open("usuarios.txt") as usuarios:
    linea = usuarios.readline()
    while linea:
        try:
            usuario = json.loads(linea) # dict
        # print(type(producto))
            instancias.append(Usuario(usuario.get("nombre"), usuario.get("apellidos"), usuario.get("email"), usuario.get("genero")))
        except Exception as e:
            with open(f"error.log","a+") as log:
                now = datetime.now()
                log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] Error: {e}\n")
                print(log.read())
        finally:
            linea = usuarios.readline() 


for i in instancias:
    print(i)
