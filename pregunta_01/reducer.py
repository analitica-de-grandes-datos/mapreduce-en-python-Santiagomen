#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
dict = {}
for linea in sys.stdin:
  if linea in dict.keys():
    dict[linea] += 1
  else:
    dict[linea] = 1
for i in dict.keys():
   letra = i.strip()
   line =  letra + "\t" + str(dict[i]) + "\n"
   sys.stdout.write(line)  
