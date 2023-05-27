#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    for linea in sys.stdin:
        columna = linea.split("   ")
        letra = columna[0]
        fecha = columna[1]
        val = columna[2]
       
        sys.stdout.write(f"{letra},{fecha},{val}\n")
