#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":
  
    for linea in sys.stdin:
        columna = linea.strip().split("\t")
        val = columna[0]
        letra = columna[1].split(",")
        
        for r in letra:
            sys.stdout.write(f"{val}\t{r}\n")
