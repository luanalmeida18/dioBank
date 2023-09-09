import os

menu = """

[1] - Depositar
[2] - Sacar
[3] - Extrato
[0] - Sair

=> """

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
tentativas_opcao = 0
LIMITE_SAQUES = 3


while True:
  opcao = input(menu)
  
  if opcao == "1":
    valor = float(input("Digite o valor a ser depositado: "))
    
    if valor > 0:
      saldo += valor
      extrato += f'+ R$ {valor:.2f}\n'  
    
    else:
      print('Falha na operação. Verifique o valor informado!')
      
    print(f'Saldo atual: R$ {saldo:.2f}')
    
    
  elif opcao == "2":
    
    valor = float(input('Digite o valor a ser sacado: '))  
    
    excedeu_saldo = valor > saldo
    
    excedeu_limite = valor > limite
    
    excedeu_saques = numero_saques >= LIMITE_SAQUES
    
    if excedeu_saldo:
      print('Falha na operação. Você não possui saldo suficiente para esta operação.')
      print(f'Saldo: R$ {saldo:.2f}')
      continue
      
    if excedeu_limite:
      print(f'O valor de saque excedeu o limite permitido. Tente um valor até R$ {limite:.2f}')
      print(f'Saldo: R$ {saldo:.2f}')
      continue
      
    if excedeu_saques:
      print('Falha na operação. Você ja fez saques o suficiente por hoje. Volte amanhã!')
      print(f'Saldo: R$ {saldo:.2f}')
      continue
    
    if valor > 0:
      saldo -= valor
      extrato += f'- R$ {valor:.2f}'
      numero_saques += 1
    else:
      print('Operação falhou! Verifique o valor informado!')
      
    print(f'Saldo: R$ {saldo:.2f}')
      
  elif opcao == "3":
    
    if saldo > 0:
      print('============================EXTRATO===========================')
      print(extrato, '\n')
      print(f'Saldo atual: R$ {saldo:.2f}')
      print('===============================================================')
    else:
      print(f'Saldo R$ {saldo:.2f}')
    
    
  elif opcao == "0":
    sair = input('Deseja realmente sair ? [S]im [N]ão: ')
    sair.upper()

    if sair == 'S' or sair == 's':
      os.system('cls') or None
      print('===============================================================')
      print('Muito obrigado por utilizar nossos serviços. Até mais!\n')
      print('===============================================================')
      break
    
    if sair == 'N' or sair == 'n':
      continue
    else:
      os.system('cls') or None
      print('===============================================================')
      print('Muito obrigado por utilizar nossos serviços. Até mais!\n')
      print('===============================================================')
    
  
  else:
    tentativas_opcao += 1
    
    if tentativas_opcao < 4:
      print('Opção inválida! Tente novamente!!')
      continue
    else:
      print('Muito obrigado por utilizar nossos serviços. Até mais!')
      break
  