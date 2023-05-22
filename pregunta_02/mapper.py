#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for linea in sys.stdin:
    linea = linea.strip()
    valores = linea.split(',')
    amount = valores[4]
    print(amount)
