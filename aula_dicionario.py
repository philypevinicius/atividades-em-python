#dados = {'nome':'philype','idade':25}
#dados.clear() #limpar o dicionario
#dados.pop('nome') #remover chave
#print(dados)
#print(len(dados)) #tamanho do dicionaro
#print('O nome é: ',dados['nome'])
#print('A idade é: ',dados['idade'])
dados = {'nome':'nome','idade':10,'empresa':'empresa'}
dados['nome'] = input('Digite o nome: ')
dados['idade'] = int(input('Digite a idade: '))
dados['empresa'] = input('Digite a empresa: ')
print(dados)
print('Cadastro realizado com sucesso!!')
x = input('Deseja alterar um produto? ').lower()
if x == 'sim':
 print('\033[34m' + 'opções:\n1 Nome\n2 Idade\n3 Empresa \n3 cancelar' + '\033[0;0m')
opcao = int(input('\033[32m' + 'Escolha: ' + '\033[0;0m'))
while opcao != 4:
  if opcao == 1:
   dados['nome'] = input('Digite o nome: ')
   print('\033[31m' + 'Feito' + '\033[0;0m')
   print(dados)

  elif opcao == 2:
   dados['idade'] = int(input('Digite a idade: '))
   print('\033[31m' + 'Feito' + '\033[0;0m')
   print(dados)

  elif opcao == 3:
   dados['empresa'] = input('Digite a empresa: ')
   print('\033[31m' + 'Feito' + '\033[0;0m')
   print(dados)

print(dados)
