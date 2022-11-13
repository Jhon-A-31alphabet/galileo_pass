from io import open
from colorama import *

init(autoreset=True)

class mostrar_menu:

    def mostrar_todas_las_contrasenas(self):
        self.data = open("Registro_datos.txt","r")
        self.registro =self.data.read()
        self.data.close()
        print(Fore.RED +self.registro)

    
