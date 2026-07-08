
def ola(nome, genero):
    if genero == "feminino":
        return f"Olá {nome}, bem vinda!"
    elif genero == "masculino":
        return f"Olá {nome}, bem vindo!"
    elif genero == "neutro":
        return f"Olá {nome}, boas vindas!"
print (ola("leo","neutro"))
print(ola("mila","feminino"))
print(ola("luan", "masculino"))
