
#///////////////////////////////////#
#archivos y librerias importadas.
#Archivo principal de la aplicacion.
#///////////////////////////////////#
from tqdm import tqdm
from registro import registrar
from menu import mostrar_menu

from colorama import *
init(autoreset=True)
import os
import time




def cargando():
    for i in tqdm(range(10), total = 10, 
        desc ="cargando"): 
        time.sleep(.1) 

def barra_guardando():
    for i in tqdm(range(10), total = 10, 
        desc ="Guardando"): 
        time.sleep(.1) 

cargando()
print(Fore.GREEN +"presione la tecla enter para continuar despues de escoger una opcion")
print(Fore.YELLOW +"Si el programa no reacciona presione la tecla enter")
time.sleep(5)
os.system('cls')

while True:
    print(Fore.GREEN+"en caso de querer mostrar todas las contrasenas")
    print(Fore.GREEN+"El programa borrara la pantalla en 50 segundos esto")
    print(Fore.GREEN+"esto para fines de seguridad")
    time.sleep(3)
    os.system('cls')

    print(Fore.CYAN + "1 -- Agregar contrasena") #option 1 for add a password
    print(Fore.GREEN+ "2 -- mostrar todas las contrasenas ") #option 2 for show passwords
    print("\n")
    print(Fore.RED + "Favor escribir el numero correspondiente a la opcion")
    main_menu = input("Que deseas hacer:   ") #enter the number 1 or 2
    try:
        if main_menu == "1":
            servicio = input("servicio:   ") #Service
            usuario = input("usuario:   ") #username
            contrasena = input("password:  ") #password
            barra_guardando()
            re = registrar(servicio,usuario,contrasena) # this is the class that save the information at text file
            re.agregar_contrasena()
        
        
        
            os.system('cls')
            continue


        elif main_menu =="2":
            mostrar = mostrar_menu()
            mostrar.mostrar_todas_las_contrasenas() #show all passwords for 50 seconds
            time.sleep(50)
            os.system("cls")

            continue
       
        else:
            print("valor invalido") #this a exeption if the user try to take other number
            time.sleep(2)
            os.system('cls')
            continue
    except: #exception if the user try to show all passwords and dont have passwords
        print("hubo un error")
        time.sleep(2)
        os.system('cls')
    
    finally:
        os.system("cls") #clear the screen
    

    

    
    

    








