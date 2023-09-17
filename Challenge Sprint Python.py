from unidecode import unidecode
import sys
#Criando funções para estilização
def ponti():
    print('-='*35)
    
def pontis():
    print('-'*55)

def linha():
    print(''*38)

def remover_acentos(x):
        return unidecode(x)

#Definindo o estoque que poderá ser usado em todas as funções
Estoque = {
    'Placa solar 30x24': 250,
    'Placa solar 100x94': 100,
    'Placa solar 66x60': 65,
    'Placa solar 200x194': 55,
    'Cabos': 2000,
    'Placa mãe': 1500,
    'Gerador de raios': 200,
    'Controle': 1000,
    'Base': 500
}
#Criando uma lista onde o for será rodado, para conferir a disponibilidade no estoque
conferirEstoque = ['Placa solar 30x24','Placa solar 100x94','Placa solar 66x60','Placa solar 200x194','Cabos','Placa mãe', 'Placa mae','Gerador de raios','Controle','Base']

#Criando a função do menu inicial
def menu():
    ponti()
    print('Olá, seja bem-vindo à loja IMSAC!')
    ponti()
    linha()
    print('1.| Acessar estoque | ')
    linha()
    print('2.| Comprar | ')
    linha()
    print('3.| Efetuar encomenda | ')
    linha()
    print('4.| O que podemos melhorar? | ')
    linha()
    pontis()
    linha()
    
    escolha = int(input('Escolha o número da sua opção!'))
    linha()

    match escolha:
        case 1:
            acessarEstoque()
        case 2:
            def comprar(*args):
                for i in args:
                    if i == 'placa mae' or i == 'Placa mae':
                        i = 'Placa mãe'
                    iUpper = i.capitalize()
                    if iUpper in conferirEstoque:
                        linha()
                        pontis()
                        qtdComprar = int(input(f'Qual a quantidade de {iUpper} você deseja comprar?'))
                        pontis()
                        if qtdComprar < Estoque[iUpper]:
                            Estoque[iUpper] -= qtdComprar
                            linha()
                            ponti()
                            print('Produto comprado, estoque atualizado...')
                            ponti()
                            linha()
                            for x,y in Estoque.items():
                                print(f'{x} -------- {y}')     
                        else:
                            print('Quantidade em estoque insuficiente...')
                    else:
                        print(f'Item {iUpper} não existente em nosso estoque ou entrada de dados errônea...')
            produtosComprar = input('Digite os produtos que você deseja comprar separados por vírgula e espaço: ').split(', ')
            comprar(*produtosComprar)
        case 3:
            efetuarEncomenda()
        case 4:
            melhorar()

#Criando as demais funções que orquestrarão o projeto
def acessarEstoque():

    print('Seja bem-vindo ao estoque IMSAC!')
    linha()
    pontis()

    for produtos, quantidade in Estoque.items():
        print(f'{produtos} ----- Quantidade: {quantidade} ')
        linha()


    #Estoque['Base p/ troca'] -= 10
    voltar = input('Você deseja ir ao setor de compras?(y/n)')
    match voltar:
        case 'y':
            def comprar(*args):
                for i in args:
                    iUpper = i.capitalize()
                    if i in conferirEstoque:
                        qtdComprar = int(input(f'Qual a quantidade de {iUpper} você deseja comprar?'))
                        if qtdComprar < Estoque[iUpper]:
                                Estoque[iUpper] -= qtdComprar
                                print(Estoque)
                                print('Produto comprado, estoque atualizado...')
                        else:
                            print('Quantidade em estoque insuficiente...')
                    else:
                        print(f'Item {iUpper} não existente em nosso estoque ou entrada de dados errônea...')
            produtosComprar = input('Digite os produtos que você deseja comprar separados por vírgula e espaço: ').split(', ')
            comprar(*produtosComprar)
            return comprar(*produtosComprar)
        case 'n':
            linha()
            voltarAoMenu = input('Você deseja voltar ao menu?(y/n)')
            match voltarAoMenu:
                case 'y':
                    menu()
                case 'n':
                    print('Ok, finalizando o programa...')
                    sys.exit()
            menu()
def melhorar():

    ponti()
    print('Bem vindo à página de avaliações da IMSAC')
    ponti()
    linha()
    Topicos = {
        'Demora no atendimento': 5,
        'Falta de contato': 4,
        'Mau funcionamento': 0,
        'Demora na entrega': 1,
        'Outros': 6
    }
    TopicosConferir = ['Demora no atendimento','Falta de contato', 'Falta de informacoes', 'Mau funcionamento', 'Demora na entrega', 'Outros']
    for motivo in Topicos:
        print(motivo)
        linha()
    oQueMelhorar = input('Digite qual foi o seu problema:').capitalize()
    linha()
    pontis()


    if oQueMelhorar in TopicosConferir:
        print('Ok, obrigado pela avaliação, iremos nos esforçar em melhorar!')
        pontis()
        linha()        
        
        Topicos[oQueMelhorar.capitalize()] += 1
        for motivo, contagem in Topicos.items():
            print(f'{motivo}: {contagem}')
            linha()
    else:
        print('Motivo não reconhecido. Por favor, escolha um motivo válido.')
        linha()
def efetuarEncomenda():
    print('Olá, seja bem-vindo à central de encomendas de placas solares da IMSAC')
    voltagemEncomenda = int(input('Qual seria a voltagem da placa desejada? (em V)'))
    linha()
    tamanhoEncomenda = int(input('Qual seria o tamanho da área da placa desejada? (em m²)'))
    preco = voltagemEncomenda * tamanhoEncomenda
    tempo = tamanhoEncomenda * 2
    linha()
    print(f'Correto, o preço da sua placa ficou em R${preco}')
    linha()
    confirmar = input('Você deseja confirmar e comprar esta placa? (y/n)')
    linha()
    match confirmar:
        case 'y':
            linha()
            print(f'Correto, obrigado por comprar conosco! Seu pedido chegará em aproximadamente {tempo} dias!')
            linha()
        case 'Y':
            linha()
            print(f'Correto, obrigado por comprar conosco! Seu pedido chegará em aproximadamente {tempo} dias!')
            linha()

        case 'n':
            print('Poxa, que pena!')
            linha()
            voltar = input('Você deseja voltar ao menu? (y/n)')
            match voltar:
                case 'y':
                    menu()
                case 'Y':
                    menu()
                case 'n':
                    linha()
                    print('Ok, finalizando o programa...')
                    linha()
                    sys.exit()
                case 'N':
                    linha()
                    print('Ok, finalizando o programa...')
                    linha()
                    sys.exit()

        case 'N': 
            print('Poxa, que pena!')
            linha()
            voltar = input('Você deseja voltar ao menu? (y/n)')
            match voltar:
                case 'y':
                    menu()
                case 'Y':
                    menu()
                case 'n':
                    linha()
                    print('Ok, finalizando o programa...')
                    linha()
                    sys.exit()
                case 'N':
                    linha()
                    print('Ok, finalizando o programa...')
                    linha()
                    sys.exit()

#Chamando o menu
menu()






