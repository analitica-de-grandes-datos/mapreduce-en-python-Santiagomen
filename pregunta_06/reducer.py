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
                dic[letra] = {'max': max(dic[letter]['max'], val),'min': min(dic[letter]['min'], val)}
                #print(letra, val)
            else:
                dic[letra] = {'max': val, 'min': val}
                
    #maximo = max(lista_valores)
    #minimo = min(lista_valores)
    #print(dic[j], maximo, minimo)
    
    dic = sorted(dic.items(), key=lambda x: x[0])
    for atributo, valor in dic:
        sys.stdout.write(f"{atributo}\t{valor['max']}\t{valor['min']}\n")
