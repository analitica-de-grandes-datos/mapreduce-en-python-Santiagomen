#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    for linea in sys.stdin:
        columna = linea.split(" ")
        letra = columna[0]
        sys.stdout.write(f"{letra}\n")
