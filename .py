# variaveis
historico = []
concluidas = []
while True:
    opcoes = input(
    '(1)Adicionar Tarefas.\n(2)Listra de tarefa.' 
    '\n(3)concluir tarefas.\n(4)Remover tarefas.'
    '\n(5)tarefas concluidas.'
     '\n(6)sair.'
     '\n:'
    ) 
    if not opcoes.isdigit():
        print('erro digite apenas um numero. ')
    elif opcoes == '1':
        nome_da_tarefa = input('adicione o nome da sua nova teréfa: ')
        historico.append(nome_da_tarefa)
    elif opcoes == '2':
        if not historico:
            print("nenhuma tarefa")
        else:
            print('sua lista de tarefas. ')
            for item in historico:
                print(item)
    elif opcoes == '3':
        conclui = input('concluir tarefa\n(s)\n: ')
        if conclui == 's':
            print('suas tarefas para concluir.')
            for item in historico:
                print(item)
            tare = input('qual tarefa voce deseja concluir: ')
            if tare in historico:
                historico.remove(tare)
                concluidas.append(tare)
                print(f'sua tarefa "{tare}" concluida')
            else:
                print('digite a terefa que voce adiciono.')     
        else:
            print('digite a opção valida. ')
    elif opcoes == '4':
        print('tarefas para remover.')
        if not historico:
            print('nenhuma tarefa para remover')
        elif historico:
            for numero, tarefa in enumerate(historico):
                print(numero + 1, tarefa)
            numero = input('qual número deseja remover? ')
            if numero.isdigit():
                numero =  int(numero)
                if 1 <= numero <= len(historico):
                    numero -= 1
                    removido = historico.pop(numero)
                    print(f'tarefa removido: {removido}')
                else:
                    print('digite apenas a quantidade de tarefas. ')
            else:
                print('digite um numero')
    elif opcoes == '5':
        if not concluidas:
            print('nenhuma tarefa concluida.')
        else:
            for item in concluidas:
                print(item)
    elif opcoes == '6':
        break
    
    


    