#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

  for linea in sys.stdin:
      linea = linea.strip()
      valores = linea.split(',')
      credit_history = valores[2]
      print(credit_history)
