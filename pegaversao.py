from pyzabbix import ZabbixAPI


xzapi = ZabbixAPI("http://179.190.52.148:4444/zabbix")
xzapi.login("Admin", "zabbix")

def y():

    itemsAgentVersion= zapi.item.get(output="extend" , search= {"key_": "vfs.fs.size[F:,used]"})
    tabela_grafico=[]

    tabela="Host\tVersao\n"
    for itemAgentVersion in itemsAgentVersion:
        historicoItemAgentVersion= zapi.history.get(output="extend" , history= 3 , sortfield =  "clock" , limit = 1 , itemids= itemAgentVersion["itemid"])
        hostItemAgentVersion= zapi.host.get(output="extend" , itemids=itemAgentVersion["itemid"])
        if (len(historicoItemAgentVersion) > 0 ) :
            tabela += hostItemAgentVersion[0]["name"] + "\t" +  itemAgentVersion["name"] +"\t" + historicoItemAgentVersion[0]["value"]+"\n"
            tabela_grafico.append([hostItemAgentVersion[0]["name"],itemAgentVersion["name"] ,historicoItemAgentVersion[0]["value"] ])
        


# print(historicoItemAgentVersion)

    return tabela_grafico



def x():

    tabela=y()
    print(tabela)
    tabela_html="<table><thead><tr><td>Host</td><td>Versao</td></tr></thead>"

    for linha in tabela:
        tabela_html+=  "<tr>"
        #for celula in linha :
        tabela_html+="<td>" + linha[0] + "</td>" + "<td>" + formata_byte(linha[2]) + "</td>"
        tabela_html+="</tr>\n"
    tabela_html+="</table>"
    
    return   tabela_html 


#f=open("tabelaVersao.txt","w")
#f.write(tabela)
#f.close()



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