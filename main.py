    
funcionarios = []
sair_do_sistema = False

def apresenta_menu():
    print("=====================================") 
    print("    Sistema de Gestão de Escalas     ")
    print("=====================================") 
    print("")
    print("1. Cadastrar funcionário👨")  
    print("2. Listar funcionário🖥️")  
    print("0. Sair❌  ")
    print("")
    opcao_menu = input("Escolha uma opção: ")
    return opcao_menu


def cadrasta_funcionario():
    funcionario = input("Digite o nome do funcionário: ")
    funcionarios.append(funcionario)
    print(f"O nome cadastrato foi:{funcionario}")  
    print("=====================================") 
    
    print("Você gostaria de adiconar um novo funcionário?")
    print("1. Sim✅")  
    print("2. Não❎")
    
    seguir_cadastro = input("Escolha uma opção:")
    print("=====================================") 
    if seguir_cadastro == "1":
        cadrasta_funcionario()
    if seguir_cadastro == "2":
        print("Cadastro concluído!!")

def listar_funcionario():
    print("Listando funcionários")
    
def sair():
    print("Saindo do sitema de Gestão de Escala👋")   



#================================================================

while not sair_do_sistema:
    
    opcao_menu = apresenta_menu() 
    
    match opcao_menu:
        case "1":
            cadrasta_funcionario()
        case "2":
            listar_funcionario()
        case 0:
            sair()
        case _:
            print("Opção inválida!")

