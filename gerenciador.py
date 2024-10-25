# PROJETO - FAKE CRUD (Create - Read - Update - Delete)
# GERENCIADOR DE TAREFAS
# TAREFA - NOME, DESCRIÇÃO, PRIORIDADE, CATEGORIA, CONCLUÍDO
# FUNÇÕES - ADICIONAR TAREFAS, LISTAR TAREFAS, ALTERAR NOME DAS TAREFAS, DELETAR TAREFAS
# LISTE TAREFAS POR PRIORIDADE / LISTE TAREFAS POR CATEGORIA
# MARCAR UMA TAREFA COMO CONCLUÍDA

banco_de_dados = []

def adicionar_tarefa():
  # Construir um dicionário com dados do usuário e inserir no banco de dados que é uma lista
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
  # Percorra a lista banco_de_dados, recuperando um dicionário (tarefa) por vez
  # Em seguida, percorra o dicionário para imprimir os pares de chave/valor
  for tarefa_cadastrada in banco_de_dados:
    for chave, valor in tarefa_cadastrada.items():
      print(f"{chave}: {valor}")
    print("-------------------------")

def listar_prioridade():
  # Percorra a lista de banco_de_dados, recuperando um dicionário (tarefa) por vez
  # Em seguida, percorra o dicionário para imprimir as tarefas por prioridade.
  prioridade = int(input('Digite a prioridade (1 - 5): '))
  for tarefa_cadastrada in banco_de_dados:
    if tarefa_cadastrada['Prioridade'] == prioridade:
      for chave, valor in tarefa_cadastrada.items():
        print(f'{chave}: {valor}')
      print("-------------------------")

def listar_categoria():
  # Percorra a lista de banco_de_dados, recuperando um dicionário (tarefa) por vez
  # Em seguida, percorra o dicionário para imprimir as tarefas por categoria.
  categoria = str(input('Digite a categoria: '))
  for tarefa_cadastrada in banco_de_dados:
    if tarefa_cadastrada['Categoria'] == categoria:
      for chave, valor in tarefa_cadastrada.items():
        print(f'{chave}: {valor}')
      print("-------------------------")

def editar_tarefas():
  # Procurar a tarefa que o usuário requisitar o nome
  # Percorrer banco_de_dados para encontrar a tarefa pelo nome passado
  # Ao encontrar a tarefa, requisitar um novo nome para a tarefa

  edicao = input("Digite o nome da tarefa a ser editada: ")
  for tarefa_cadastrada in banco_de_dados:
    if tarefa_cadastrada['Nome'] == edicao:
      novo_nome = input("Digite o novo nome da tarefa: ")
      tarefa_cadastrada['Nome'] = novo_nome
      print("NOME DA TAREFA EDITADO COM SUCESSO!")
    print("-------------------------")

    
def deletar_tarefas():
  # Procurar a tarefa que o usuário requisitar o nome
  # Percorrer banco_de_dados para encontrar a tarefa pelo nome passado
  # Ao encontrar a tarefa, remover o item de banco_de_dados

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
  # Procurar a tarefa que o usuário requisitar o nome
  # Percorrer banco_de_dados para encontrar a tarefa
  # Ao encontrar a tarefa, marcar como concluída

  tarefa = input('Digite o NOME da tarefa que você deseja marcar como concluída: ')
  for tarefa_cadastrada in banco_de_dados:
    if tarefa_cadastrada['Nome'] == tarefa:
      tarefa_cadastrada['Concluído'] = True
      print(f'TAREFA CONCLUÍDA!!!')
    else:
      print(f'Não existe tarefa com o nome {tarefa}.')
  print("-------------------------")
    

print("BEM-VINDO AO GT v1.0")

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
