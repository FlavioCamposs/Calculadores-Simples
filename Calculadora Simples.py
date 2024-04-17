from unidecode import unidecode

''' \033[m,        # 0 - sem cores
    \033[1;91m     # 1 - vermelho
    \033[1;92m     # 2 - verde
    \033[1;93m     # 3 - amarelo
    \033[1;94m     # 4 - azul
    \033[1;97m     # 5 - Branco
    \033[1;37m     # 6 - Cinza
'''

per1 = int(input('\033[1;97mDigite um numero: \033[m'))


def chamada(cor=0):
    print('\n\033[1;97mDeseja ver qual operação deste numero?\033[m')
    print('\033[1;91mAdição\033[m - \033[1;92mSubtração\033[m - \033[1;93mMultiplicação\033[m - \033[1;94mDivisão\033[m')
    per2 = str(input('\033[1;97mResp: \033[m')).upper()
    return per2


#Armazenando o retorno da função em uma variavel para evitar que seja chamada mais de uma vez!
cham = chamada()
resp = unidecode(cham)


def tabuada(num):
    print('=' * 39)
    f = '\033[1;97mTabuada de\033[m {}{}{} \033[1;97mdo numero {}:\033[m'
    if resp == 'ADICAO':
        print(f.format('\033[1;91m',cham,'\033[m',num))
        for c in range(1, 11):
            print(f'\033[1;97m{num} + {c} = {num+c}\033[m')
    elif resp == 'SUBTRACAO':
        print(f.format('\033[1;92m',cham,'\033[m',num))
        for c in range(1, 11):
            print(f'\033[1;97m{num} - {c} = {num-c}\033[m')
    elif resp == 'MULTIPLICACAO':
        print(f.format('\033[1;93m',cham,'\033[m',num))
        for c in range(1, 11):
            print(f'\033[1;97m{num} x {c} = {num*c}\033[m')
    elif resp == 'DIVISAO':
        print(f.format('\033[1;94m',cham,'\033[m',num))
        for c in range(1, 11):
            print(f'\033[1;97m{num} / {c} = {num/c:.1f}\033[m')
    else:
        print('\033[1;91mRESPOSTA INVÁLIDA!!!\033[m')


tabuada(per1)