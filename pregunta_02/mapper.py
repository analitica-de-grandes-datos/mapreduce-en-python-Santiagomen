#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for row in sys.stdin:
  fila = row.split(",")
  amount = fila[4]
  purpose = fila[3]
  linea = purpose + ";" + amount
  sys.stdout.write(linea+"\n")
