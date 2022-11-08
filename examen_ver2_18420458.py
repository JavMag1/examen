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
        aux={}
        arch = open('CPdescarga.txt', 'r')
        cad = arch.read()
        cad = cad.replace('||', '| |')
        lista = cad.split("\n")
    except exception as Error:
        print(f"no existe el archivo {arch}")
    arch.close()
    i = 1
    for x in lista:
        mnpaux = x.split("|")
        list = {}

        if len(mnpaux) > 1:
            if mnpaux[3] == municipio:
                list["d_codigo"] = mnpaux[0]
                list["d_tipo_asenta"] = mnpaux[2]
                list["d_zona"] = mnpaux[-2]
                aux[f"{i}"] = list
                i = i + 1
    returnolist = json.dumps(aux)
    print(returnolist)
resive_municipio('Jiquilpan')



# Realice un método que reciba un estado, por ejemplo “Michoacán
# de Ocampo”, grabe en un archivo en formato JSON: Código Postal
# (d_codigo), y Municipio (D_mnpio). El archivo deberá contener todos los
# códigos que pertenezcan al estado.

def codigospostales2(estado):
    try:
        fin = {}
        arch = open('CPdescarga.txt', 'r')
        cad = arch.read()
        cad = cad.replace('||', '| |')
        lista = cad.split("\n")
    except exception as Error:
        print(f"no existe el archivo {arch}")

    arch.close()

    retornoList = []

    for mnp in lista:
        codigos = mnp.split("|")
        cp = {}
        if len(codigos)>1 :
            if codigos[4] == estado:
                cp["d_codigo"] = codigos[0]
                cp["D_mnpio"] = codigos[3]
                retornoList.append(cp)
    fin[estado] = retornoList
    retornoList = json.dumps(fin)
    print(retornoList)

codigospostales2("Michoacán de Ocampo")
