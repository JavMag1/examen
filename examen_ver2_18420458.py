'''
Tema: Examen version 2
Fecha: 07 de Noviembre del 2022
Autor: Francisco Javier Magallon Romero
'''
import json
from logging import exception

# Realice un método que reciba como argumento un municipio, por
# ejemplo “Jiquilpan” y regrese un arreglo de JSON, cada JSON
# contendrá: código Postal (d_codigo), tipo de asentamiento (d_tipo_asenta)
# y zona (d_zona).

def resive_municipio(municipio):

    try:
        codigosP={}
        arch = open('CPdescarga.txt', 'r')
        cad = arch.read()
        cad = cad.replace('||', '| |')
        lista = cad.split("\n")
    except exception as Error:
        print(f"no existe el archivo {arch}")
    else:
        arch.close()
    i = 1
    for x in lista:
            list = {}
            mnpaux = x.split("|")
            if len(mnpaux) > 1:
                if mnpaux[3] == municipio:
                    list["d_codigo"] = mnpaux[0]
                    list["d_tipo_asenta"] = mnpaux[2]
                    list["d_zona"] = mnpaux[-2]
                    codigosP[f"{i}"] = list
                    i = i + 1






    return json.dumps(list)
print(resive_municipio("jiquilpan"))





# Realice un método que reciba un estado, por ejemplo “Michoacán
# de Ocampo”, grabe en un archivo en formato JSON: Código Postal
# (d_codigo), y Municipio (D_mnpio). El archivo deberá contener todos los
# códigos que pertenezcan al estado.