from io import open


class registrar:
    def __init__(self,servicio,usuario,contrasena):
        self.servicio = servicio
        self.usuario = usuario
        self.contrasena = contrasena
    
    def agregar_contrasena(self):
        data_base = open("Registro_datos.txt","a")
        data_base.seek(0)
        data_base.write("*----------------------------*")
        data_base.write("\n")
        data_base.write("\n")
        data_base.write("Servicio:    ")
        data_base.write(self.servicio)
        data_base.write("\n")
        data_base.write("\n")
        data_base.write("Usuario:  ")
        data_base.write(self.usuario)
        data_base.write("\n")
        data_base.write("\n")
        data_base.write("Contrasena:   ")
        data_base.write(self.contrasena)
        data_base.write("\n")
        data_base.write("\n")
        data_base.write("*----------------------------*")
        data_base.write("\n")
        data_base.write("\n")
        data_base.close()
    
    
   
    



    
        

        
