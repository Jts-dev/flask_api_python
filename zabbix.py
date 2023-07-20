from pyzabbix import ZabbixAPI
from operator import itemgetter


def login_no_zabbix():
    zapi = ZabbixAPI("http://179.190.52.148:4444/zabbix")
    zapi.login("Admin", "zabbix")
    return( zapi)



def pega_historico(zapi, tabela_host_item):


    item_sem_historico=[]
    tabela_final=[]

    filtro=lambda x : x["itemid"] ==  item
    filtro_tabela=lambda x : x["itemid"] ==  item

    for linha in tabela_host_item :
        item_sem_historico.append(linha["itemid"])

    tamanho_atual_da_lista=len(item_sem_historico)
    tamanho_anterior_da_lista=0
    while (tamanho_anterior_da_lista != tamanho_atual_da_lista):
        historico_da_key= zapi.history.get(output="extend" , history= 3 , sortfield =  "clock",sortorder = "DESC",  limit = len(item_sem_historico) , itemids= item_sem_historico)
        refazer=[]
        for item in  item_sem_historico : 
            busca_no_historico = list(filter(filtro, historico_da_key))
            if (len(busca_no_historico) ==0   ):
                refazer.append(item)
            else:
                ultimo_valor = sorted(busca_no_historico, key = itemgetter('clock') , reverse=True )[0] 
                tabela_final.append(list(filter(filtro_tabela, tabela_host_item))[0])
                tabela_final[-1]["value"]=ultimo_valor["value"]
        tamanho_anterior_da_lista = tamanho_atual_da_lista
        item_sem_historico =refazer
        # print(len(refazer))
        tamanho_atual_da_lista=len(item_sem_historico)




    for item in refazer :
        tabela_final.append(list(filter(filtro_tabela, tabela_host_item))[0])
        tabela_final[-1]["value"]="-1"
    print(tabela_final)
    print("\n\n\n\n\n\n\n\n\n")
                    

        
        #print(tabela_final)
    

    return(tabela_final)
        



    

 

    return(historico_da_key)
    

def pega_nome_do_host(zapi, tabela ):

    nova_tabela=[]
    filtro=lambda x : x["hostid"] ==  linha["hostid"]


    lista_de_host =[]
    for linha in tabela :
        lista_de_host.append(linha["hostid"])

    dados_dos_hosts= zapi.host.get(output="extend" , hostids=lista_de_host)

    for linha in tabela:
 
     
        dados_do_host = list(filter(filtro, dados_dos_hosts))
        print(dados_do_host)
        print(f"xxxxsss{len(dados_do_host)}----------------{len(dados_do_host) > 0}")
        if  (len(dados_do_host) > 0) :
            nova_tabela.append(linha)
            nova_tabela[-1]["host"]= list(filter(filtro, dados_do_host))[0]["host"]
            #print(linha)
     

    return(nova_tabela)




def pega_itens_com_key(zapi):
    hosts_com_key=[]

    tabela_host_item=[]

    itens_com_key= zapi.item.get(output="extend" , search= {"key_": "vfs.fs.size[c:,free]"})

    print(itens_com_key[2])
    print("--------")
    for item_com_key in itens_com_key :

        tabela_host_item.append({"hostid":item_com_key["hostid"], "itemid":item_com_key["itemid"]    }   )
        hosts_com_key.append(item_com_key["hostid"] )


    tabela_host_item = pega_historico(zapi, tabela_host_item)
    #pega_historico(zapi, tabela_host_item)
    tabela_host_item= pega_nome_do_host(zapi,tabela_host_item)
    return(tabela_host_item)




def zabbix():
    zapi=login_no_zabbix()
    hosts_com_key = pega_itens_com_key(zapi)
   
    return (hosts_com_key)


