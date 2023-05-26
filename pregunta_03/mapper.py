#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
    for linea in sys.stdin:
        columna = linea.split(",")
        letra = columns[0]
        valor = int(columna[1])
        sys.stdout.write(f"{letra}\t{valor}\n")
