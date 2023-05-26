#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    dic = {}
    for linea in sys.stdin:
        columna = linea.split("\t")
        if len(columna) == 2:
            letra = columna[0] 
            val = int(columna[1])
            dic[letra] = val
            
    dic_sort = sorted(dic.items(), key=lambda x: x[1])
    for atributo,valor in dic_sort:
        sys.stdout.write(f"{atributo},{valor}\n")
