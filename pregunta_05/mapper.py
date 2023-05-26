#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    for linea in sys.stdin:
        columna = linea.split(" ")
        fecha = columna[1].split("-")
        mes = fecha[1]
        sys.stdout.write(f"{mes}\n")
