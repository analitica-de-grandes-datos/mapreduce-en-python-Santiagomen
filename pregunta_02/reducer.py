#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':
    purpose = None
    val_max = 0
    for line in sys.stdin:
        key, val_act = line.split("\t")
        val_act = int(val_act)
        if key == purpose:
            if val_act > total:
                val_max = val_act
        else:
            if purpose is not None:
                sys.stdout.write("{}\t{}\n".format(purpose, val_max))
            purpose = key
            val_max = val_act
    sys.stdout.write("{}\t{}\n".format(purpose, val_max))
