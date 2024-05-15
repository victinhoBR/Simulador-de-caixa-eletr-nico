capital=5000.00
extrato = ""
numero_saques = 0
seguimentador=0
excedeu_limite=500
excedeu_saques=3
excedeu_saldo = capital
LIMITE_EXTRATOS=3
LIMITE_SAQUES = 3

#apresentação do banco
print("+-Bem vindo ao Banco Saint, entre com login e senha-+")

#Para testes a senha e login é 123
login=float(input("Login: "))
senha=float(input("Senha: "))

#Apresentação de operações
menu= """+-Deseja fazer mais uma operação para hoje?-+
|        Digite [D] para Deposito           |
|        Digite [S] para Saque              |
|        Digite [E] para Extrato            |
|        Digite [X] para Sair               |
+-------------------------------------------+
    Digite a letra de sua operação:"""

while login==123 and senha==123  :
    opcao=input(menu)
    
    if opcao == "D" :
        deposito = float(input("Qual seu deposito desejado?:"))
        if deposito>0:
            capital+=deposito
            extrato=f"Deposito : R${deposito:.2f}\n"
                
        else:
             print("o deposito tem que ser maior que 0")
                
    elif opcao == "S":
            saque = float(input("Qual seu saque desejado?:"))

            excedeu_saldo = capital < saque
            excedeu_limite = saque >= capital 
            excedeu_saques = numero_saques > LIMITE_SAQUES
            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")
            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")    

            if saque>0:
                    capital-=saque
                    extrato=f"Saque : R${saque:.2f}\n"
                        
            else:
                print("o saque tem que ser maior que 0R$")   
                   
    elif opcao == "E":
        print("\n================ EXTRATO ================")
        print(f"\nSaldo: R$ {capital:.2f}")
        print("==========================================")
    
    else:
        print("Digite um comando válido")