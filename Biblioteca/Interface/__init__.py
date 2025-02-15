def leiaInt(msg):
    while True:
        try:
            m=int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mNenhum valor digitado.\033[m')
            return 0
        else:
            return m

def leiaStr(msg):
    while True:
        try: 
            m=str(input(msg)).strip()
            if not m.replace(' ', '').isalpha():
                print('\033[31mERRO! Por favor digite um nome válido.\033[m')
                continue
        except (KeyboardInterrupt):
            print('\n\033[31mNenhum valor digitado.\033[m')
            return 0
        else:
            return m
        
def linha(tam=42):
    return '-'*tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c=1
    for item in lista:
        print(f'\033[32m{c} - \033[34m{item}\033[m')
        c+=1
    print(linha())
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc      
