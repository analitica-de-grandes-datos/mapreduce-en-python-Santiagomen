#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

dict = {}
for row in sys.stdin:
  r = row.strip()
  r = r.split(";")
  if r[0] in dict.keys():
    if int(r[1]) > dict[r[0]]:
      dict[r[0]] = int(r[1])
    else:
      continue
  else:
    dict[r[0]] = int(r[1])
for i in dict.keys():
   letra = i
   linea =  letra + "\t" + str(dict[i]) + "\n"
   sys.stdout.write(linea)  
