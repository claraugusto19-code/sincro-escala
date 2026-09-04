from pathlib import Path

path_bd = Path("BD") / "escala_bd.txt"
escalas = []

def cadastrar_escala():
    escala = input("digite o nome da escala: ")
    with open(path_bd,"a", encoding="utf-8") as arquivo:
            arquivo.write(f"{escala}\n")
    escalas.append(escala)
    print(f"O nome cadastrado foi: {escala}")
    print("======================================")
    print("você gostaria de cadrastar uma nova escala?")
    print("1. Sim ✅")
    print("2. Não ❌")
    seguir_cadastro = input("Escolha uma opção: ")
    print("======================================")
    if seguir_cadastro  == "1":    
        cadastrar_escala()
    if seguir_cadastro == "2":
        print("cadastro concluido ✅")