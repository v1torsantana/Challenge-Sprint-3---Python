import sys
#Criando funções para estilização
def ponti():
    print('-='*35)
    
def pontis():
    print('-'*55)

def linha():
    print(''*38)


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
            produtosComprar = input('Quais são os produtos que você deseja comprar? (Separados por vírgula)').split(',')
            comprar(*produtosComprar)
        case 3:
            efetuarEncomenda()
        case 4:
            melhorar()

Estoque = {
    '| Placa solar 30x24 |': 250,
    '| Placa solar 100x94 |': 100,
    '| Placa solar 66x60 |': 65,
    '| Placa solar 200x194 |': 55,
    '| Cabos |': 2000,
    '| Placa mãe |': 1500,
    '| Gerador de raios UV |': 200,
    '| Controle |': 1000,
    '| Base |': 500
}

#Criando as demais funções que orquestrarão o projeto
def acessarEstoque():

    print('Seja bem-vindo ao estoque IMSAC!')
    linha()
    pontis()

    for produtos, quantidade in Estoque.items():
        print(f'{produtos} Quantidade: {quantidade} ')
        linha()


    #Estoque['Base p/ troca'] -= 10
    voltar = input('Você deseja ir ao setor de compras?(y/n)')
    match voltar:
        case 'y':
            comprar()
            return Estoque
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
        'Falta de informações': 4,
        'Mau funcionamento': 0,
        'Demora na entrega': 1,
        'Outros': 6
    }
    for motivo in Topicos:
        print(motivo)
        linha()
    oQueMelhorar = input('Digite qual foi o seu problema:').lower()
    pontis()
    linha() 

    if oQueMelhorar in (motivo.lower() for motivo in Topicos):
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

    
        


def comprar(*args):
    print('')

def efetuarEncomenda():
    print('')



menu()



#||||||