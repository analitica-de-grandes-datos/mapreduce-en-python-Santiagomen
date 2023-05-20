#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys 
dic = {}
for linea in sys.stdin:
    linea = linea.strip()
    valores = linea.split(',')
    r = valores[2]
    
    if r in dic:
       dic[valores[2]] += 1
    else:
       dic[valores[2]] = 1
dic_ordenado = dict(sorted(dic.items(), key=lambda x: x[0]))

for clave, valor in dic_ordenado.items():
    print(clave, valor)
