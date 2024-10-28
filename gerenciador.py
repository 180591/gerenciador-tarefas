# PROJETO - FAKE CRUD (Create - Read - Update - Delete)
# GERENCIADOR DE TAREFAS
# TAREFA - NOME, DESCRIÇÃO, PRIORIDADE, CATEGORIA, CONCLUÍDO
# FUNÇÕES - ADICIONAR TAREFAS, LISTAR TAREFAS, ALTERAR NOME DAS TAREFAS, DELETAR TAREFAS
# LISTE TAREFAS POR PRIORIDADE / LISTE TAREFAS POR CATEGORIA
# MARCAR UMA TAREFA COMO CONCLUÍDA

banco_de_dados = []

def adicionar_tarefa():

  tarefa = {
      'Nome': input("Digite o nome da tarefa: "),
      'Descrição': input("Digite a descrição da tarefa: "),
      'Prioridade': int(input("Digite a prioridade (1 - 5): ")),
      'Categoria': input("Digite a categoria da tarefa: "),
      'Concluído': False
    }

  banco_de_dados.append(tarefa)
  print("TAREFA ADICIONADA COM SUCESSO!")
  print("-------------------------")

def listar_tarefas():

  for tarefa_cadastrada in banco_de_dados:
    for chave, valor in tarefa_cadastrada.items():
      print(f"{chave}: {valor}")
    print("-------------------------")

def listar_prioridade():

  prioridade = int(input('Digite a prioridade (1 - 5): '))
  for tarefa_cadastrada in banco_de_dados:
    if tarefa_cadastrada['Prioridade'] == prioridade:
      for chave, valor in tarefa_cadastrada.items():
        print(f'{chave}: {valor}')
      print("-------------------------")

def listar_categoria():
  
  categoria = str(input('Digite a categoria: '))
  for tarefa_cadastrada in banco_de_dados:
    if tarefa_cadastrada['Categoria'] == categoria:
      for chave, valor in tarefa_cadastrada.items():
        print(f'{chave}: {valor}')
      print("-------------------------")

def editar_tarefas():
  
  edicao = input("Digite o nome da tarefa a ser editada: ")
  editar = input('Tem certeza que deseja editar essa tarefa? [S/N] ')
  if editar in 'Ss':
    for tarefa_cadastrada in banco_de_dados:
      if tarefa_cadastrada['Nome'] == edicao:
        novo_nome = input("Digite o novo nome da tarefa: ")
        tarefa_cadastrada['Nome'] = novo_nome
        print("NOME DA TAREFA EDITADO COM SUCESSO!")
  else:
    print('TAREFA NÃO EDITADA')
  print("-------------------------")

    
def deletar_tarefas():
  
  nome_delete = input("Digite o nome da tarefa que deseja deletar: ")
  deletar = input('Tem certeza que deseja deletar essa tarefa? [S/N] ')
  if deletar in 'Ss':
    for tarefa_cadastrada in banco_de_dados:
      if tarefa_cadastrada['Nome'] == nome_delete:
        banco_de_dados.remove(tarefa_cadastrada)
        print('TAREFA EXCLUÍDA COM SUCESSO!!!')
  else:
    print('TAREFA MANTIDA NO GERENCIADOR')
  print("-------------------------")

def concluir_tarefa():
  
  tarefa = input('Digite o NOME da tarefa que você deseja marcar como concluída: ')
  for tarefa_cadastrada in banco_de_dados:
    if tarefa_cadastrada['Nome'] == tarefa:
      tarefa_cadastrada['Concluído'] = True
      print(f'TAREFA CONCLUÍDA!!!')
    else:
      print(f'Não existe tarefa com o nome {tarefa}.')
  print("-------------------------")
    
print('=-=' * 7)
print("BEM-VINDO AO GT v1.0")
print('=-=' * 7)

while True:
  print("O QUE DESEJA FAZER HOJE?")
  print("1 - Adicionar nova tarefa")
  print("2 - Listar tarefa")
  print("3 - Listar por prioridade")
  print("4 - Listar por categoria")
  print("5 - Editar tarefa")
  print("6 - Deletar tarefa")
  print("7 - Concluir tarefa")
  print("8 - Sair do programa")
  op = int(input("-> "))

  if op == 1:
    adicionar_tarefa()
  
  elif op == 2:
    listar_tarefas()

  elif op == 3:
    listar_prioridade()

  elif op == 4:
    listar_categoria()

  elif op == 5:
    editar_tarefas()

  elif op == 6:
    deletar_tarefas()

  elif op == 7:
    concluir_tarefa()   
  
  elif op == 8:
    break

print('=-=' * 9)  
print('OBRIGADO!!! VOLTE SEMPRE!!!')
print('=-=' * 9)
