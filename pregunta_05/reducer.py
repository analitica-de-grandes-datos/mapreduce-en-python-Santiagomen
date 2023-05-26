#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    meses = {}
    for linea in sys.stdin:
        columna = linea.split("\n")
        mes = columna[0]
        if mes in meses:
            meses[mes]+= 1
            
        else:
            meses[mes]= 1
            
    resume_sort= sorted(meses.items())
    for atributo,valor in resume_sort:
        sys.stdout.write(f"{atributo}\t{valor}\n")
