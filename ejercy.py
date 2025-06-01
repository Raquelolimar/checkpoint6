class User:
    def __init__ (self,nombre, contraseña):
        self.nombre= nombre
        self.contraseña= contraseña
usuario1= User('Raquel', 'baskenit')

print(usuario1.nombre)
print(usuario1.contraseña)