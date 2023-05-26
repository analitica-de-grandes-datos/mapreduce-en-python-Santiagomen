#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

  dict = {}
  for linea in sys.stdin:
      columna = linea.split("\t")
     
      letra = columna[0] 
      val = int(columna[1])
      dict[letra] = val

  dict_sort = sorted(dict.items(), key=lambda x: x[1])
  for atributo,valor in dict_sort:
      sys.stdout.write(f"{atributo},{val}\n")
