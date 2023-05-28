#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == "__main__":
  
    dic = {}
    for linea in sys.stdin:
        columna = linea.split(",")
        
        if len(columna) == 2:
            letra = columna[0]
            val = float(columna[1])
            
            if letra in dic:
                dic[letra][0] += val
                dic[letra][1] += 1
                #mean= 
                #verificar funcion para promedio
            else:
                dic[letra] = [val, 1]
    
    dic_sorted = sorted(dic.items(), key=lambda x: x[0])
    
    for atributo, values in dic_sorted:
        total = values[0]
        num = values[1]
        prom = total / num
        
        sys.stdout.write(f"{atributo}\t{total}\t{prom}\n")
