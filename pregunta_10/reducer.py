#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    dic = {}
    
    for linea in sys.stdin:
        columna = linea.split("\t")
        if len(columna) == 2:
            val = columna[0]
            colletras = columna[1].strip()
            
            for letra in colletras:
                if letra in dic:
                    dic[letra].append(val)
                else:
                    dic[letra] = [val]

    dic_sorted = sorted(dic.items(), key=lambda x: x[0])
    
    for letra, values in dic_sorted:
        values_sorted = sorted(values, key=lambda x: int(x))
        values_str = ",".join(values_sorted)
        sys.stdout.write(f"{letra}\t{values_str}\n")
