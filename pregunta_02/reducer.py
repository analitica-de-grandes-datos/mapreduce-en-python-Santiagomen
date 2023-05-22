#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
dict2 = {}

for row in sys.stdin:
  linea = row.strip()
  linea = linea.split(";")
  if linea[0] in dict2.keys():
    if int(linea[1]) > dict2[linea[0]]:
      dict2[linea[0]] = int(linea[1])
    
    else:
      continue
  else:
    dict[linea[0]] = int(linea[1])
for i in dict2.keys():
   a = i 
   line =  a + "\t" + str(dict2[i]) + "\n"
   sys.stdout.write(line) 
