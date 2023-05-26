#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
if __name__ == "__main__":
    dic = {}
    for linea in sys.stdin:
        columna = line.split("\n")
        letra = columna[0]
        if letra in dic:
            dic[letra]+= 1
            
        else:
            dic[letra]= 1
            
    dic_sort= sorted(dic.items())
    for atributo,valor in dic_sort:
        sys.stdout.write(f"{atributo},{valor}\n")
