#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys 

for line in sys.stdin:
    letra, val = line.strip().split(',')
    sys.stdout.write("{},{}\n".format(letra,val))
