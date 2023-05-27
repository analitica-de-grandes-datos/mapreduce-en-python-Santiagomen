#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    lista = []
    for linea in sys.stdin:
        columna = linea.split(",")
        
        if len(columna)==3:
            letra = columna[0]
            #date = columna[1].split('-')
            fecha = columna[1]
            val = int(columna[2])
            lista.append((letra, fecha, val))

    lista_sorted = sorted(lista, key = lambda x: (x[0], x[2]))

    for k in lista_sorted:
        sys.stdout.write(f"{k[0]}   {k[1]}   {k[2]}\n")
