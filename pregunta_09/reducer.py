#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    dic = {}
    contador = 0
    
    for linea in sys.stdin:
        columna = linea.split(",")
        
        if len(columna) >= 3:
            letra = columna[0]
            fecha = columna[1]
            val = int(columna[2])
            
            if val in dic:
                if dic[val] > (letra, fecha):
                    dic[val] = (letra, fecha)
            else:
                dic[val] = (letra, fecha)
    
    dic_sorted = sorted(dic.items())
    
    for val, (letra, fecha) in dic_sorted:
        sys.stdout.write(f"{letra}   {fecha}   {val}\n")
        contador += 1
        
        if contador == 6:
            break
