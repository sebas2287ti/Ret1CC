from ret1cc import algoritms
import os

def main_interface():
    os.system("cls")
    print("Bienvenido a cual punto del reto quieres acceder" )
    print("1 | Busqueda de texto")
    print("2 | Es palindromo")
    opcion=int(input("Ingresa la opcion deseada: "))
    match opcion:
        case 1:
            reto1_interface() 
        case 2:
            pass
        case _:
            main_interface()


def reto1_interface():
    os.system("cls")
    print("Bienvenido por favor digita la palabra que quieres buscar")
    condition_loop = True
    while condition_loop:
        try:
            word_input = input("Ingresa la palabra")
            if len(word_input) == 0:
                raise ValueError("No escribio nada el usuario")
        except ValueError:
            reto1_interface()
        else:
            #Eliminar para hacer las pruebas reiteradas veces 
            reto1_algoritm_interace(word_input)
            condition_loop = False


def reto1_algoritm_interace(word):
    os.system("cls")
    print("Palabra Seleccionado es:" + word)
    print("Elige que algoritmo quieres usar")
    print("1 | Boyer_Moore")
    print("2 | Knuth_Morris_Pratt")
    opcion = int(input("Ingresa la opcion deseada: "))
    match opcion:
        case 1:
            print ("se acabo")
        case 2:
            print ("se acabo")
        case _:
            reto1_algoritm_interace(word)


     
