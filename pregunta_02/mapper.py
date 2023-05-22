#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for row in sys.stdin:
  fila = row.split(",")
  amount = elementos[4]
  purpose = elementos[3]
  linea = purpose + ";" + amount
  sys.stdout.write(linea+"\n")
