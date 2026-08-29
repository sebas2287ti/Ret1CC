from ret1cc.algoritms.Boyer_Moore import find_word_BM
from dotenv import load_dotenv
import time
import os

def main_interface():
    while True:
        os.system("cls")
        print("Bienvenido a cual punto del reto quieres acceder" )
        print("1 | Busqueda de texto")
        print("2 | Es palindromo")
        opcion=int(input("Ingresa la opcion deseada: "))
        match opcion:
            case 1:
                reto1_interface() 
                break 
            case 2:
                pass
                break
            case _:
                print("Opcion no valida")
                input("Presiona para continuar")


def reto1_interface():
    while True:
        os.system("cls")
        print("Bienvenido por favor digita la palabra que quieres buscar")
        
        word_input = input("Ingresa la palabra: ").strip()
        if len(word_input) == 0:
            continue
        
        reto1_algoritm_interace(word_input)
        break


def reto1_algoritm_interace(word):
    while True:
        os.system("cls")
        load_dotenv()
        print("Palabra Seleccionado es:" + word)
        print("Elige que algoritmo quieres usar")
        print("1 | Boyer_Moore")
        print("2 | Knuth_Morris_Pratt")
        opcion = int(input("Ingresa la opcion deseada: "))
        match opcion:
            case 1:
                start_time = time.perf_counter()
                find_word_BM(os.getenv("TEXT"), word)
                end_time = time.perf_counter()
                break
            case 2:
                print ("se acabo")
                break
            case _:
                print("Opcion no valida")

     
