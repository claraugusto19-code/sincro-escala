    
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
    print(f"O nome cadastrato foi:{funcionario}")  
   
   
def listar_funcionario():
    print("Listando funcionários")
    
 def sair():
     print("Saindo do sitema de Gestão de Escala👋")   
    
    
    
     

#================================================================

opcao_menu = apresenta_menu() 


match opcao_menu:
    case "1":
        cadrasta_funcionario()
    case "2":
        listar_funcionario()
    case 0:
        print("0. Sair❌")
    case _:
        print("Opção inválida!")
