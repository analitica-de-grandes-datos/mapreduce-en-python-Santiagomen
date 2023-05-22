#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
dic = {}
for linea in sys.stdin:
    #linea = linea.strip()
    #valores = linea.split(',')
    if len(valores) >= 3:
        r = valores[2]
        if r in dic:
           dic[r] += 1
        else:
           dic[r] = 1

dic_ordenado = dict(sorted(dic.items(), key=lambda x: x[0]))
    
#output = ""
for key, value in dic_ordenado.items():
    print(f"{key}\t{value}")
