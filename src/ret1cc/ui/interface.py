from ret1cc.algoritms.Boyer_Moore import find_word_BM
from ret1cc.algoritms.Knuth_Morris_Pratt import find_word_KMP
from ret1cc.algoritms import Palindromo
from ret1cc.data.Dataset_words import get_text
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
                reto1_interface_text() 
                break 
            case 2:
                reto2_interface()
                break
            case _:
                print("Opcion no valida")
                input("Presiona para continuar")


def reto1_interface():
    while True:
        global word_input
        os.system("cls")
        print("Bienvenido por favor digita la palabra que quieres buscar")
        
        word_input = input("Ingresa la palabra: ").strip().lower()
        if len(word_input) == 0:
            continue
        
        reto1_algoritm_interace()

def reto1_interface_text():
    while True:
        global n_text
        os.system("cls")
        print("Bienvenido por favor en que cantidad de palabras quieres buscar la palabra")
        try:
            n=int(input("Ingresa la cantidad deseada: "))
            n_text = get_text(n)
        except:
            input("Digite unicamente numeros")
            continue
        reto1_interface()
        break
    

def reto1_algoritm_interace():
    while True:
        os.system("cls")
        print("Palabra Seleccionado es:" + word_input)
        print("Elige que algoritmo quieres usar")
        print("1 | Boyer_Moore")
        print("2 | Knuth_Morris_Pratt")
        print("3 | Elegir otra palabra")
        try:
            opcion=int(input("Ingresa la opcion deseada: "))
        except:
            input("Digite unicamente numeros")
            continue 
        match opcion:
            case 1:
                start_time = time.perf_counter()
                find_word_BM(n_text, word_input)
                end_time = time.perf_counter()
                input(f"El tiempo de ejecucion fue de {(end_time-start_time) * 1000} ms")
                #break
            case 2:
                start_time = time.perf_counter()
                res = find_word_KMP(n_text, word_input)
                end_time = time.perf_counter()
                for i in range(len(res)):
                    print(res[i], end=" ")
                input(f"El tiempo de ejecucion fue de {(end_time-start_time) * 1000} ms")
                #break
            case 3:
                break
            case _:
                input("Opcion no valida")

     
def reto2_interface():
    while True:
        os.system("cls")
        print("Ingresa la palabra que quieres volver palindromo")
        word = input("Ingresa la palabra: ")
        if len(word) <= 2:
            continue

        if Palindromo.is_palindromo(word):
            print(f"La palabra: {word} ya es un palindromo")
            break

        print(Palindromo.convert_palindromo(word))
        input(f"Presiona para salir")


