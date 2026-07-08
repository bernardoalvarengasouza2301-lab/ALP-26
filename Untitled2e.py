def imprimir_mensagem():
    print ("A INFO1A é top")

def exibir_elogio(nome):
    print(f"{nome} é top")
    
def  classificar_nota(nota):
    if nota > 60:
        print("aprovado")
    else:
        print ("reprovado") 
        
def contagem_regressiva(a):
    for i in range(a):
        print (i)
        time.sleep(1)


imprimir_mensagem()
exibir_elogio("alva")
