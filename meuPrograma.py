from time import sleep
import math
from os import system


def limpaTela():
    system('clear')


try:
    while True:
        limpaTela()
        print('''\033[1;30m
[1] Súper Calculadora
[2] Gerenciador de Loja
[3] Tabuada
[4] Calcular Média do aluno
[5] Numero par/ Ímpar
[6] Área do Triângulo
[7] Fatorial de um Número
[8] Jogo Adivinha
[9] Validaçâo de Dados
[10] Conversao de Número em bases diferentes
[0] Para saír
    ''')
        opcao = int(input("Escolha uma opçâo: "))
        if opcao == 0:
            print('Saindo...')
            sleep(2)
            break
        elif opcao > 1010:
            print("\033[1;31mOpçao Inválida\033[m ")

        elif opcao == 1:
            try:
                while True:
                      limpaTela()
                      print('\033[1;33m=' * 20, '{}'.format(' CALCULADORA INTELIGENTE '), '=' * 20)
                      print('Quer contar até quanto? ')
                      inicio = int(input('INICIO: '))
                      fim = int(input('FIM: '))
                      if inicio < fim:
                          print('========== CONTAGEM CRESCENTE: ==========')
                          for cont in range(inicio, fim + 1):
                              print('{}'.format(cont), end=' ')
                      elif inicio > fim:
                          print('========== CONTAGEM DECRESCENTE: ==========')
                          for cont in range(inicio, fim - 1, -1):
                              print('{}'.format(cont), end=' ')
                      while True:
                            opcao = str(input('\nQuer continuar? [S/N] ')).strip().upper()[0]
                            if opcao in 'SN':

                               break
                      if opcao == 'N':
                          break


            except ValueError:
                   print('ERRO! Opçao inválida')
        elif opcao == 2:
            limpaTela()
            while True:
                try:
                     print("\033[1;33m=" * 10, "GERENCIAMENTO DE LOJA ", "=" * 10)
                     print(" BEM VINDO AO GERENCIADOR DE FLUXO DE CAIXA ")
                     print("=" * 44)
                     total = 0

                     while True:
                         produto = float(input("Preço do produto: "))
                         quantidade = int(input("Quantidade: "))
                         total = total + produto * quantidade
                         while True:
                            resposta = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
                            if resposta in 'SN':
                                 break
                            print('Responda apenas S ou N')
                         if resposta == "N":
                             break
                     print("Total de compras {:.2f}MT".format(total))
                     valor = float(input("Valor a receber: "))
                     while valor < total:
                         valor = float(input("Valor a receber: "))
                     print("-=" * 20)
                     sleep(2)
                     print("=== RECIBO DE PAGAMENTO ===")
                     print("Total de compras {:.2f}MT".format(total))
                     print("Total pago {:.2f}MT".format(valor))
                     print("Troco {:.2f}MT".format(valor - total))
                     print()
                     print("==> Obrigado por fazer compras connosco <==")
                     print("Volte Sempre!")
                     print("-=" * 20)
                     sleep(2)
                except ValueError:
                    print('Ocorreu um Erro')
                while True:
                    try:
                      num = int(input('Pressione zero para Saír '))
                      if num == 0:
                          break
                    except ValueError:
                        print('Ocorreu um Erro')
                if num == 0:
                    break
        elif opcao == 3:
            limpaTela()
            while True:
                try:
                    print("\033[1;31m=" * 5, " TABUADA ", "=" * 5)
                    tab = int(input("Quer ver Tabuada de Quanto? "))
                    inicio = int(input("Início: "))
                    fim = int(input("Fim: "))
                    for c in range(inicio, fim + 1):
                        print("{} x {:2} = {:2}".format(tab, c, tab * c))
                    while True:
                         op = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
                         if op in 'SN':
                             break
                         print('Responda apenas S ou N ')
                    if op == "N":
                       break
                except ValueError:
                    print('ERRO! digite apenas um numeros inteiro: ')

        elif opcao == 4:
         while True:
             limpaTela()
             try:
                aluno = {}
                notas = []
                print("\033[1;34m-=" * 20)
                print("=== ESCOLA VAI QUEM QUER ===")
                print()
                while True:
                    try:
                         aluno["Nome"] = str(input("Nome do aluno: "))
                         if aluno['Nome'] != '':
                             break
                    except ValueError:
                        print('ERRO!')
                nota1 = float(input("1ª Nota: "))
                nota2 = float(input("2ª Nota: "))
                nota3 = float(input("3ª Nota: "))
                notas.append(nota1 + nota2 + nota3)
                media = notas[0]/3
                aluno["Notas"] = nota1, nota2, nota3
                aluno["Média"] = math.trunc(media)
                if media >= 16:
                    aluno["Situacao"] = "Dispensado"
                elif media >= 10:
                    aluno["Situacao"] = "Admitido"
                elif media < 10:
                    aluno["Situacao"] = "Excluído"
                print("-=" * 15)
                for k, v in aluno.items():
                    print("{}: {}".format(k, v))
                op = "S"
                while True:
                    op = str(input("\nQuer continuar? [S/N] ")).strip().upper()[0]
                    if op in 'SN':
                        break
                    print("\033[1;30mOpçâo Inválida. Tente novamente\033[m")
                if op == "N":
                    break
             except ValueError:
                 print('Informe os dados Válidos ')

        elif opcao == 5:
            limpaTela()
            while True:
                try:
                  print("\033[1;30m[1] Par ")
                  print("[2] Ímpar")
                  print("[0] para saír")
                  escolha = int(input("Sua opcao"))

                  if escolha == 0:
                      break

                  elif escolha == 1:
                      totpar = 0
                      print("== PAR ==")
                      print("Exemplo, ver números pares no intervalo de 2 até 20")
                      inter1 = int(input("Intervalo: "))
                      inter2 = int(input("Até quanto: "))
                      for cont in range(inter1, inter2 + 1):
                          if cont % 2 == 0:
                              totpar += 1
                              print("\033[1;31m{}\033[m".format(cont), end=" ")
                      if totpar > 1:
                          print("\nNesse intervalo ao todo sao{} números Pares".format(totpar))
                      elif totpar == 1:
                          print("\nNesse intervalo tem {} número Par".format(totpar))

                  elif escolha == 2:
                      totimp = 0
                      print("== ÍMPAR ==")
                      print("Exemplo, ver números ímpares no intervalo de 2 até 20")
                      inter3 = int(input("Intervalo: "))
                      inter4 = int(input("Até quanto: "))
                      for cont in range(inter3, inter4 + 1):
                          if cont % 2 == 1:
                              totimp += 1
                              print("\033[1;31m{}\033[m".format(cont), end=" ")
                      if totimp > 1:
                          print("\nNesse intervalo ao todo sao{} números Ímpares".format(totimp))
                      elif totimp == 1:
                          print("\nNesse intervalo tem {} número Ímpar".format(totimp))
                except ValueError:
                    print('Opçao Inválida')
        elif opcao == 6:
            limpaTela()
            area = 1
            while True:
                try:
                    base = float(input("\033[1;35mDigite a Base: "))
                    altura = float(input("Digite a Altura: "))
                    area = (base * altura) / 2
                    print("Área do Triângulo é {:.2f}".format(area))
                    print("Quer continuar? ")
                    print("[S/N]")
                    while True:
                        esc = str(input("Escolha: ")).strip().upper()[0]
                        if esc in 'SN':
                            break
                        print('Responda apenas S ou N')
                    if esc == 'N':
                        break

                except ValueError:
                    print('Informe Dados Válidos')
        elif opcao == 7:
             limpaTela()
             fatorial = 1
             while True:
                 while True:
                     try:
                        num = int(input("Informe un número: "))
                        if num < 0:
                            print('\033[1;31mNâo pode ser um número negativo. Tente de novo', '\033[m')
                        else:
                            break
                     except ValueError:
                         print('ERRO! Deve ser um número inteiro')
                 fatorial = math.factorial(num)
                 for cont in range(1, num + 1):
                     print("{}.".format(cont), end=" ")
                 print("Fim")
                 print("\nFatorial de {} é {}".format(num, fatorial))
                 while True:
                        res = str(input("Quer continuar? [S/N]")).strip().upper()[0]
                        if res in 'SN':
                            break
                        else:
                            print('ERRO! responda apenas S ou N.')

                 if res == "N":
                     break
        elif opcao == 8:
            limpaTela()
            from time import sleep
            from random import randint

            while True:
                print('\033[1;36m-=' * 30)
                print('{:^50}'.format(' JOGO DE ADIVINHA '))
                print('{:^50}'.format(' VERSÂO 1.0 '))
                print('-=' * 30)
                print()

                print('''
[1] Para Jogar
[2] Manual de Instruçao 
[0] Saír''')
                opcao = int(input('Sua opçâo: '))
                if opcao == 0:
                    break
                elif opcao == 1:
                    limpaTela()
                    print('Inicializando o Jogo... ')
                    sleep(3)
                    certo = errado = 0
                    while True:
                        certo += 1
                        computador = randint(1, 20)
                        while True:
                            jogador = int(input('Qual é o número que o Computador pensou? '))
                            if jogador > 20 or jogador < 1:
                                print('O numero deve estar no intervalo de 1 até 20')
                            else:
                                break
                        print('Analizando sua jogada...')
                        sleep(1)
                        if jogador == computador and certo - 1 < 10:
                            print('\033[1;34mPensei no número {} e você e você no número {}'.format(computador, jogador))
                            print('Parabéns!')
                            print('Você acertou com {} Tentativas!\033[m'.format(certo - 1))
                            break
                        elif jogador == computador and certo - 1 > 10:
                            print('Voce é Péssimo no jogo de adivinha ^_^. Acertou com {} Tentativas'.format(certo - 1))
                            break
                        elif jogador != computador:
                                print('Pensei no número {} e você no número {}'.format(computador, jogador))
                                print('\033[1;31m Você errou!\033[m ')

                elif opcao == 2:
                    limpaTela()
                    print('#' * 80)
                    print('''\033[1;30m
O jogo funciona da seguinte forma: o computador vai 'pensar' num número entre 1 e 20
e voce vai tentar adivinhar qual é o número que o computador pensou
se você inserir um número igual ao que computador pensou você ganha,
se o número nâo for igual você perde
e o programa vai mostrar quantas tentativas  você deu até ganhar
e quantas vezes você perdeu!!!\033[m''')
                    print('\033[1;36m#' * 80)

                    while True:
                        try:
                            num = int(input('Digite Zero [ 0 ] para Saír '))
                            if num == 0:
                                break
                        except ValueError:
                            print('ERRO! deve ser um número inteiro ')

                else:
                    print('Opcao inválida ')

        elif opcao == 9:
            limpaTela()
            # O programa cadastra uma pessoa num dictionário
            # e joga os dados dentro duma lista

            cadastro = list()
            pessoa = dict()
            soma = media = 0
            while True:
                limpaTela()
                pessoa.clear()
                pessoa['Nome'] = str(input('Nome: '))
                while True:
                    pessoa['sexo'] = str(input('Sexo: [M/F]')).strip().upper()[0]
                    if pessoa['sexo'] in 'MF':
                        break
                    print('ERRO! por favor, digite apenas M ou F.')
                pessoa['Idade'] = int(input('Idade: '))
                soma += pessoa['Idade']
                cadastro.append(pessoa.copy())
                while True:
                    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
                    if opcao in 'SN':
                        break
                    print('ERRO! por favor responda apenas S ou N.')
                if opcao == 'N':
                    break

            print('-=' * 30)
            print('A) Ao todo temos {} pessoas cadastradas'.format(len(cadastro)))
            media = soma / len(cadastro)
            print('B) A média de idade é de {:.2f}'.format(media))
            print('C) As mulheres cadastradas foram ', end=' ')
            for p in cadastro:
                if p['sexo'] in 'F':
                    print(', {}'.format(p["Nome"]), end=' ')
            print('\nD) Lista das pessoas que estâo acima da média ')
            for p in cadastro:
                if p['Idade'] >= media:
                    for k, v in p.items():
                        print('{} = {};'.format(k, v), end=' ')
                    print()
            print('<<< ENCERRADO >>>')

        elif opcao == 10:
            limpaTela()
            # conversao de número em difenrentes Bases numéricas

            num = int(input("Digite um numero inteiro: "))
            print(""" 
    Escolha uma das Bases para conversao:
    [ 1 ] converter para BINARIO
    [ 2 ] converter para OCTAL
    [ 3 ] converter para HEXADECIMAL""")
            opcao = int(input("Sua opçao: "))
            print()
            if opcao == 1:
                print("{} convertido para BINÁRIO é igual a {}".format(num, bin(num)[2:]))
            elif opcao == 2:
                print("{} convertido em OCTAL é igual a {}".format(num, oct(num)[2:]))
            elif opcao == 3:
                print("{} convertido em HEXADECIMAL é igual a {}".format(num, hex(num)[2:]))
            else:
                print("Opçâo Inválida, Tente novamente")

except ValueError:
    print('\033[1;31mERRO! caracter Inválido\033[m')
