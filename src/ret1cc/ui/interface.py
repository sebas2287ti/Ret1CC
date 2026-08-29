from ret1cc.algoritms.Boyer_Moore import find_word_BM
from ret1cc.algoritms.Knuth_Morris_Pratt import find_word_KMP
from dotenv import load_dotenv
import time
import os

def main_interface():
    while True:
        os.system("cls")
        print("Bienvenido a cual punto del reto quieres acceder" )
        print("1 | Busqueda de texto")
        print("2 | Es palindromo")
        try:
            opcion=int(input("Ingresa la opcion deseada: "))
        except:
            input("Digite unicamente numeros")
            continue 
        match opcion:
            case 1:
                reto1_interface() 
                break 
            case 2:
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
        try:
            opcion=int(input("Ingresa la opcion deseada: "))
        except:
            input("Digite unicamente numeros")
            continue 
        match opcion:
            case 1:
                start_time = time.perf_counter()
                find_word_BM(os.getenv("TEXT"), word)
                end_time = time.perf_counter()
                input(f"El tiempo de ejecucion fue de {(end_time-start_time) * 1000} ms")
                #break
            case 2:
                start_time = time.perf_counter()
                res = find_word_KMP(os.getenv("TEXT"), word)
                end_time = time.perf_counter()
                for i in range(len(res)):
                    print(res[i], end=" ")
                input(f"El tiempo de ejecucion fue de {(end_time-start_time) * 1000} ms")
                #break
            case _:
                input("Opcion no valida")

     
