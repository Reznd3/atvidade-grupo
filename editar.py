import csv
def cadastrar_clientes(pessoas,nome,telefone,email):
    pessoa = {
        'Nome': nome,
        'Telefone': telefone,
        'Email': email
    }
    pessoas.append(pessoa)
    print("Cliente cadastrado com Sucesso!")
    print("_______________________________")
    print("\n")
pessoas=[]

def atualizar_linha(pessoas,email):
    for pessoa in pessoas:   
        if email=='Email':
            pessoas[email]['Nome']=nome
            pessoas[email]['Telefone']=telefone
            pessoas[email]['Email']=email
            
def criar_arquivo_csv():
    with open('arquivo.csv', mode="w", newline="") as arquivo_csv:
        writer=csv.writer(arquivo_csv)
        writer.writerow(["Nome","Telefone","Email"])

        for pessoa in pessoas:
            writer.writerow([pessoa["Nome"], pessoa["Telefone"], pessoa["Email"]])

def ler_dados_csv():
    with open('arquivo.csv', mode="r", newline="") as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        print(" Nome    |   Telefone    |   Email   ")
        for linha in leitor_csv:
            print(f"    {pessoa["Nome"]}    |   {pessoa["Telefone"]}    |   {pessoa["Email"]}    ")

def excluir_pessoa(pessoas, email):
    pessoa_registrada = None
    for pessoa in pessoas:
        if pessoa['Email'] == email:
            pessoa_registrada = pessoa
            break
    if pessoa_registrada:
        pessoas.delete(pessoa_registrada)
        print(f"A pessoa com o email {email} foi excluída.")
    else:
        print("Esta pessoa não esta registrada")
