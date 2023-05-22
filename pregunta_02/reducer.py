#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':
    purpose = None
    max_value = 0
    for line in sys.stdin:
        purpose, valor_act = line.split("\t")
        valor_act = int(max_value)
        if key == purpose:
            if valor_act > max_value:
                max_value = valor_act
        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\n".format(purpose, max_value))

            purpose = key
            max_value = val
    sys.stdout.write("{}\t{}\n".format(purpose, max_value))
