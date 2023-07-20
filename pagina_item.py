from zabbix import zabbix
from zabbix import pega_nome_do_host



def formata_byte(valor):
    valor=int(valor)

    grandesas = ["B","KB","MB","GB","TB"]

    if valor == -1 :
        return("NaN")
    
    for grandesa in grandesas:
        if valor >= 1024 :
            valor= valor/1024
        else:
            return ("%.2f %s" % (valor, grandesa))

def gera_pagina_item():

    pagina="<table>"

    tabela=zabbix()
  
    for linha in tabela: 
        print(linha)
  
        pagina+="<tr>"
        pagina+= "<td>" + linha["host"]  + "</td>"
        pagina+= "<td>" + formata_byte(linha["value"])  + "</td>"
        pagina+= "<td>" + linha["value"] + "</td>"
        pagina+="</tr>\n"
    pagina+="</table>"

    # pega_nome_do_host(zapi,tabela_host_item)





    return (pagina)