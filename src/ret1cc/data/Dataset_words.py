def get_text(cantidad):
    RUTA = "src/ret1cc/data/Dataset_palabras.txt"
    palabras = []
    total = 0

    with open(RUTA, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            tokens = linea.split()
            if total + len(tokens) <= cantidad:
                palabras.extend(tokens)
                total += len(tokens)
            else:
                faltantes = cantidad - total
                palabras.extend(tokens[:faltantes])
                break

    return " ".join(palabras).lower()
